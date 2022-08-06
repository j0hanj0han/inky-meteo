#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import requests
import geocoder

class MeteoAgent:

    def __init__(self, location):
        self.location = location
        self.weather = self._get_weather()
    

    def get_coords(self, address):
        # Convert a city name and country code to latitude and longitude
        g = geocoder.arcgis(address)
        coords = g.latlng
        return coords



    def _get_weather(self):
        coords = get_coords(address)
        weather = {}
        res = requests.get("https://darksky.net/forecast/{}/uk212/en".format(",".join([str(c) for c in coords])))
        if res.status_code == 200:
            soup = BeautifulSoup(res.content, "lxml")
            curr = soup.find_all("span", "currently")
            weather["summary"] = curr[0].img["alt"].split()[0]
            weather["temperature"] = int(curr[0].find("span", "summary").text.split()[0][:-1])
            press = soup.find_all("div", "pressure")
            weather["pressure"] = int(press[0].find("span", "num").text)
            return weather
        else:
            return weather