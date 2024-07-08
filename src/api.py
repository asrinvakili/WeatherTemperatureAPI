from base import WeatherAPIBase
import requests


class OpenMeteo(WeatherAPIBase):
    def __init__(self, lat, long, **kwargs):
        self.lat = lat
        self.long = long

    def get_weather_temp(self):
        params = {'latitude': self.lat, 'longitude': self.long, "current": "temperature_2m"}
        result = requests.get("https://api.open-meteo.com/v1/forecast", params=params)
        result_json = result.json()
        return result_json["current"]["temperature_2m"]



