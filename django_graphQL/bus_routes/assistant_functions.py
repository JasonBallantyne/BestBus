import datetime
import pytz
from .schema import *


def to_timestamp(time_in_seconds):
    second = str(int(time_in_seconds % 60))
    remainder = time_in_seconds // 60
    minute = str(int(remainder % 60))
    hour = str(int(remainder // 60))

    return leading_0_timestamp(hour, minute, second)


def leading_0_timestamp(hour, minute, second):
    # eliminate single digits in timestamp
    if len(hour) == 1:
        hour = f"0{hour}"
    if len(minute) == 1:
        minute = f"0{minute}"
    if len(second) == 1:
        second = f"0{second}"
    return hour + ":" + minute + ":" + second


def timestamp_to_seconds(time_list):
    ftr = [3600, 60, 1]
    times_in_seconds = []

    for time in time_list:
        time_units = time.split(':')
        total_secs = (int(time_units[0]) * ftr[2]) + (int(time_units[1]) * ftr[1]) + (int(time_units[0]) * ftr[0])
        times_in_seconds.append(total_secs)

    times_in_seconds.sort()
    return times_in_seconds


def departure_times(route, direction, hour, minute):
    # timezone = pytz.timezone('Europe/Dublin')
    # current = datetime.datetime.now(timezone).time()
    time_format = "%H:%M:%S"
    time_seconds = (int(hour)*3600) + (int(minute)*60)
    timestamp = to_timestamp(time_seconds)
    timestamp = datetime.datetime.strptime(timestamp, time_format).time()
    all_departure_times = []

    # check every route and assess its departure times vs user's inputted time
    for unique_route in UniqueRoutes.objects.all():
        if unique_route.line_id == route and unique_route.direction == direction:
            dep_time = unique_route.first_departure_schedule.split(',')
            for time in dep_time:
                time = time.strip(" ")

                # preventing error thrown when time returned passes midnight
                time = correcting_midnight(time)
                time_stamp = datetime.datetime.strptime(time, time_format).time()
                # only return times past current time
                if time_stamp > timestamp:
                    all_departure_times.append(time)

    return all_departure_times


def predicted_travel_times(time, model, day, month):
    #weather = weather_parser.weather_forecast()

    # current_day = 0
    # hour = time.split(":")[0].strip("0")
    # key = str(current_day) + "-" + hour
    # if key in weather:
    #     hourlyWeather = weather[key]
    # else:
    #     current = "0-" + str(datetime.datetime.now().hour + 2)
    #     hourlyWeather = weather[current]
    #
    # rain = hourlyWeather["precip"]
    # temp = hourlyWeather["temp"]
    # return model.predict([[day, hour, month, rain, temp]])[0]
    return model.predict([[day, 12, month, 0.5, 16]])[0]


def data_and_direction(stop_num):
    return_data = []
    remove_chars = ["[", "]"]

    for item in StopSequencing.objects.all():
        if item.stop_num == stop_num:
            stop_data = item.stop_route_data
            stop_data = stop_data.split("], [")
            for character in remove_chars:
                for data in stop_data:
                    data = data.replace(character, "")
                    data = data.replace(", ", "_")
                    return_data.append(data)

    return return_data


def correcting_midnight(time):
    time_units = time.split(":")
    if int(time_units[0]) > 23:
        hour = int(time_units[0]) - 24
    else:
        hour = int(time_units[0])
    timestamp = leading_0_timestamp(str(hour), time_units[1], time_units[2])
    return timestamp


def correct_position(predictions):
    temp = []
    print(predictions)
    for prediction in predictions:
        time = prediction.split("_")[-1]
        if len(temp) == 0:
            temp.append(prediction)
        else:
            for item in range(len(temp)):
                compare_time = temp[item].split("_")[-1]
                if time < compare_time:
                    temp.insert(item, prediction)
                    break
                if time > compare_time:
                    if temp[item] == temp[-1]:
                        temp.append(prediction)
                    else:
                        pass
    return temp
