import requests
from .weather_config import api_key


def weather_info():
    current_weather = {"temp": 0,
                       "feels_like": 0,
                       "pressure": 0,
                       "wind_speed": 0,
                       "uvi": 0,
                       "weather": 0,
                       "icon": ""}

    forecast = requests.get(api_key)
    response = forecast.status_code
    if response != 200:
        raise ValueError("url not reached.")

    forecast_data = forecast.json()
    i = forecast_data["current"]
    current_weather["temp"] = i["temp"]
    current_weather["feels_like"] = i["feels_like"]
    current_weather["uvi"] = i["uvi"]
    current_weather["pressure"] = i["pressure"]
    current_weather["wind_speed"] = i["wind_speed"]

    j = (i["weather"])
    j = (j[0])
    current_weather["weather"] = j["main"]
    current_weather["icon"] = j["icon"]
    return current_weather
