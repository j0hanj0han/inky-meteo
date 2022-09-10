#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pprint
import requests
import geocoder

from bs4 import BeautifulSoup


class MeteoAgent:

    def __init__(self, location):
        self.weather = self._get_weather(location)
        pprint.pprint(self.weather)
    
    def _make_request(self, address):
        coords = self.get_coords(address)
        url = f"https://darksky.net/forecast/{(','.join([str(c) for c in coords]))}/uk212/en"
        res = requests.get(url=url)
        return res

    def get_coords(self, address):
        # Convert a city name and country code to latitude and longitude
        g = geocoder.arcgis(address)
        coords = g.latlng
        return coords

    def _get_weather(self, address):
        ''' Return today and tomorrow weather'''
        weather = {'today': {}, 'tomorrow': {}}
        res = self._make_request(address=address)
        if res.status_code == 200:
            # today 
            soup = BeautifulSoup(res.content, "lxml")
            curr = soup.find_all("span", "currently")
            weather["today"]["summary"] = curr[0].img["alt"].split()[0]
            weather["today"]["temperature"] = int(curr[0].find("span", "summary").text.split()[0][:-1])
            press = soup.find_all("div", "pressure")[0]
            weather["today"]["pressure"] = int(press.find("span", "num").text)
            weather["today"]["uv"] = soup.find("span", "uv__index__value").text          

            # tomorrow
            # need the summary
            soup = BeautifulSoup(res.content, "html.parser")
            forecast = soup.select('a[data-day="1"]')[0]
            tempMin = forecast.select('span[class="minTemp"]')[0].text
            tempMax = forecast.select('span[class="maxTemp"]')[0].text
            weather["tomorrow"]["tempMin"] = tempMin
            weather["tomorrow"]["tempMax"] = tempMax
            return weather
        else:
            return weather


# if __name__ == "__main__":
#     meteoagent = MeteoAgent("Montpellier")