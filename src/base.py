from abc import ABC, abstractmethod


class WeatherAPIBase(ABC):
    def __init__(self, lat, long, **kwargs):
        pass

    @abstractmethod
    def get_weather_temp(self):
        pass
