import requests
from datetime import datetime
from .weather_config import api_key, weatherbitio


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


# new weather request function (old function did not get full forecast data,
# and did not include rain, which is required for our models)
def weather_forecast():
  # get forecast
  forecast = requests.get(weatherbitio)
  
  # handle bad request, else process data
  response = forecast.status_code
  if response != 200:
    raise ValueError("url not reached.")
  else:
    # convert to json
    forecastData = forecast.json()

    # create a dictionary to return data
    returnDict = {}
    for i in forecastData["data"]:
      # get local time for creating dict key, (key = "day from current" + "-" + "hour")
      localTimestamp = i["timestamp_local"]
      dayFromCurrent = str(int(localTimestamp.split("T")[0].split("-")[2]) - int(datetime.date(datetime.now()).strftime("%d")))
      hourOfDay = localTimestamp.split("T")[1].split(":")[0]
      key = dayFromCurrent + "-" + hourOfDay
      
      # get all required weather data, currently only require temperature, precipitation and weather desciption info
      temp = i["temp"]
      precip = i["precip"]
      weather = i["weather"]

      # now build dictionary entry
      returnDict[key] = {'temp': temp, 'precip': precip, 'weather': weather}

    return returnDict
