import requests
from datetime import datetime
from .weather_config import weatherbitio


# def weather_info():
#     current_weather = {"temp": 0,
#                        "feels_like": 0,
#                        "pressure": 0,
#                        "wind_speed": 0,
#                        "uvi": 0,
#                        "weather": 0,
#                        "icon": ""}
#
#     forecast = requests.get(api_key)
#     response = forecast.status_code
#     if response != 200:
#         raise ValueError("url not reached.")
#
#     forecast_data = forecast.json()
#     i = forecast_data["current"]
#     current_weather["temp"] = i["temp"]
#     current_weather["feels_like"] = i["feels_like"]
#     current_weather["uvi"] = i["uvi"]
#     current_weather["pressure"] = i["pressure"]
#     current_weather["wind_speed"] = i["wind_speed"]
#
#     j = (i["weather"])
#     j = (j[0])
#     current_weather["weather"] = j["main"]
#     current_weather["icon"] = j["icon"]
#     return current_weather


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
        forecast_data = forecast.json()

        # create a dictionary to return data
        return_dict = {}
        for i in forecast_data["data"]:
            # get local time for creating dict key, (key = "day from current" + "-" + "hour")
            local_timestamp = i["timestamp_local"]
            day_from_current = str(
                int(local_timestamp.split("T")[0].split("-")[2]) - int(datetime.date(datetime.now()).strftime("%d")))

            hour_of_day = local_timestamp.split("T")[1].split(":")[0]
            key = day_from_current + "-" + hour_of_day

            # get all required weather data, currently only require temperature, precipitation and weather desciption info
            temp = i["temp"]
            precip = i["precip"]
            weather = i["weather"]

            # now build dictionary entry
            return_dict[key] = {'temp': temp, 'precip': precip, 'weather': weather}

        return return_dict
