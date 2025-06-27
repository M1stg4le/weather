from datetime import datetime
from typing import NamedTuple

Celsius = int
meters_per_second = int
WeatherType = str

class Weather(NamedTuple):
    temperature: Celsius
    wind_speed: meters_per_second
    weather_type: WeatherType
    sunset: datetime
    sunrise: datetime

def structure_data(weather: dict) -> Weather:
    
    temperature = Celsius(weather['main']['temp'])
    wind_speed = meters_per_second(weather['wind']['speed'])
    weather_type = WeatherType(weather['weather'][0]['description'].title())
    sunset = datetime.fromtimestamp(weather['sys']['sunset'])
    sunrise = datetime.fromtimestamp(weather['sys']['sunrise'])

    return Weather(
        temperature,
        wind_speed,
        weather_type,
        sunset,
        sunrise
    )
