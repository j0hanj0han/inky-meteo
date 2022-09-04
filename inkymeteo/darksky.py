#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from xml.dom.expatbuilder import theDOMImplementation
import requests
import geocoder
from bs4 import BeautifulSoup

class MeteoAgent:

    def __init__(self, location):

        self.weather = self._get_weather(location)
    

    def get_coords(self, address):
        # Convert a city name and country code to latitude and longitude
        g = geocoder.arcgis(address)
        coords = g.latlng
        return coords

    def _get_weather(self, address):
        coords = self.get_coords(address)
        weather = {}
        url = f"https://darksky.net/forecast/{(','.join([str(c) for c in coords]))}/uk212/en"
        res = requests.get(url=url)
        if res.status_code == 200:
            soup = BeautifulSoup(res.content, "lxml")
            curr = soup.find_all("span", "currently")
            weather["summary"] = curr[0].img["alt"].split()[0]
            weather["temperature"] = int(curr[0].find("span", "summary").text.split()[0][:-1])
            press = soup.find_all("div", "pressure")
            weather["pressure"] = int(press[0].find("span", "num").text)
            weather["uv"] = soup.find("span", "uv__index__value").text          
            print(weather)

            soup = BeautifulSoup(res.content, "html.parser")
            forecast = soup.select('a[data-day="1"]')[0]
            tempMin = forecast.select('span[class="minTemp"]')[0].text
            tempMax = forecast.select('span[class="maxTemp"]')[0].text
            print(f"tomorrow: max: {tempMax} min: {tempMin} ")
            breakpoint()




            return weather
        else:
            return weather


if __name__ == "__main__":
    meteoagent = MeteoAgent("Montpellier")