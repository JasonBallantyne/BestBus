import datetime
import pytz
from .schema import *
import pickle
from .apis import time_data


def seconds_to_timestamp(time_in_seconds):
    second = str(int(time_in_seconds % 60))
    remainder = time_in_seconds // 60
    minute = str(int(remainder % 60))
    hour = str(int(remainder // 60))

    return correcting_midnight(units_to_timestamp(hour, minute, second))


def units_to_timestamp(hour, minute, second):
    # eliminate single digits in timestamp
    if len(hour) == 1:
        hour = f"0{hour}"
    if len(minute) == 1:
        minute = f"0{minute}"
    if len(second) == 1:
        second = f"0{second}"
    return hour + ":" + minute + ":" + second


def unit_to_seconds(hour, minute):
    ftr = [3600, 60, 1]
    total_secs = (int(hour) * ftr[0]) + (int(minute) * ftr[1])

    return total_secs


def timestamp_to_seconds(time_list):
    ftr = [3600, 60, 1]
    times_in_seconds = []

    for time in time_list:
        time_units = time.split(':')
        total_secs = (int(time_units[0]) * ftr[0]) + (int(time_units[1]) * ftr[1]) + (int(time_units[0]) * ftr[2])
        times_in_seconds.append(total_secs)

    times_in_seconds.sort()
    return times_in_seconds


def departure_times(route, direction):
    all_departure_times = []

    # check every route and assess its departure times vs user's inputted time
    for unique_route in UniqueRoutes.objects.all():
        if unique_route.line_id == route and unique_route.direction == direction:
            dep_time = unique_route.first_departure_schedule.split(',')
            for time in dep_time:
                time = time.strip(" ")
                # preventing error thrown when time returned passes midnight
                time = correcting_midnight(time)
                all_departure_times.append(time)

    return all_departure_times


def return_weather(weather, time, current_day):
    current_time = time_data.time_data()
    hour = time.split(":")[0].strip("0")
    key = str(current_day) + "-" + hour
    if key in weather:
        hourly_weather = weather[key]
    else:
        hr = str(int(current_time.split(":")[0]) + 1)
        if (len(hr) == 1):
          current = "0-0" + str(int(current_time.split(":")[0]) + 1)
        else:
          current = "0-" + str(int(current_time.split(":")[0]) + 1)
        hourly_weather = weather[current]

    rain = hourly_weather["precip"]
    temp = hourly_weather["temp"]
    return rain, temp


def data_and_direction(stop_num):
    return_data = []
    remove_chars = ["[", "]"]

    for item in StopSequencing.objects.all():
        if str(item) == stop_num:
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
    timestamp = units_to_timestamp(str(hour), time_units[1], time_units[2])
    return timestamp


def ordering_predictions(list_size, predictions):
    output = [predictions[0]]
    for prediction in predictions:
        prediction = prediction.replace("]", "")
        if prediction not in output:
            temp_time = prediction.split("_")[-1]
            for item in range(len(output)):
                if prediction not in output:
                    check = output[item]
                    if temp_time < check.split("_")[-1]:
                        output.insert(item, prediction)
                    elif len(output) <= list_size and item == len(output) - 1:
                        output.append(prediction)
    return output


def return_departure_times(models):
    all_departure_times = {}
    for i in UniqueRoutes.objects.all():
        line_id = i.id
        for key, value in models.items():
            if key == line_id:
                destination = value[1]
                divisor = value[2]
                key_string = f"{line_id}_{destination}_{divisor}_{value[3]}"
                all_departure_times[key_string] = [x.strip() for x in i.first_departure_schedule.split(',')]
    return all_departure_times


def return_models(routes):
    models = {}
    for i in routes:
        info = i.split("_")
        route = info[0]
        divisor = float(info[1])
        direction = info[2]
        destination = info[3]
        ceann_scribe = info[4]
        exists = os.path.isfile(f'./bus_routes/route_models/{direction}/RandForest_{route}.pkl')
        if exists:
            models[route + "_" + direction] = [pickle.load(open(f'.'
                                                                f'/bus_routes/route_models'
                                                                f'/{direction}/RandForest_{route}'
                                                                f'.pkl', "rb")), destination, divisor, ceann_scribe]
        else:
            pass
    return models


def return_journey_time_and_key(day, hour, key, month, rain, temp):
    route_info = key.split("_")
    route = str(route_info[0])
    direction = str(route_info[1])
    destination = str(route_info[2])
    ceann_scribe = str(route_info[4])

    new_key = route + "_" + direction + "_" + destination + "_" + ceann_scribe
    divisor = float(route_info[3])
    model = pickle.load(open(f'./bus_routes/route_models/{direction}/RandForest_{route}.pkl', "rb"))
    prediction = model.predict([[day, hour, month, rain, temp]])[0]
    predicted_journey_time = prediction / divisor
    return new_key, predicted_journey_time


def return_cut_off_and_predicted_times(hour, item, minute, predicted_journey_time):
    time_units = item.split(":")
    item = unit_to_seconds(time_units[0], time_units[1])
    predicted_time = float(item + predicted_journey_time)
    cut_off_time = (int(hour) * 3600) + (int(minute) * 60)
    return cut_off_time, predicted_time


def predictions_list(all_departure_times, day, hour, minute, month, rain, temp, predictions, tomorrow):
    # predict travel time for each routes departure to chosen stop
    for key, value in all_departure_times.items():
        new_key, predicted_journey_time = return_journey_time_and_key(day, hour, key, month, rain, temp)

        # assessment for times in the past, or if tomorrow
        for item in value:
            cut_off_time, predicted_time = return_cut_off_and_predicted_times(hour, item, minute,
                                                                              predicted_journey_time)
            if (cut_off_time < predicted_time and tomorrow is False) or tomorrow is True:
                predicted_timestamp = seconds_to_timestamp(predicted_time)
                predicted_time = new_key + "_" + predicted_timestamp
                predictions.append(predicted_time)

    return predictions


def get_all_routes_for_stop(stop_num):
    routes = []
    characters = ["[", "]", "\\"]
    data = data_and_direction(stop_num)
    for information in data:
        for char in characters:
            information = information.replace(char, "")
        routes.append(information)
    return routes


def before_or_after_midnight(times_list):
    after_midnight_stamps = ["00", "01", "02", "03", "04"]
    before_midnight = []
    after_midnight = []

    for time in times_list:
        hour = time.split("_")[-1].split(":")[0]
        if hour in after_midnight_stamps:
            after_midnight.append(time)
        else:
            before_midnight.append(time)

    return before_midnight, after_midnight


def return_travel_times(all_departure_times, day, model, month, weather):
    all_travel_times = []
    current_day = 0
    current_time = time_data.time_data()

    for i in all_departure_times:
        hr = i.split(":")[0]
        key = str(current_day) + "-" + hr
        if key in weather:
            hourly_weather = weather[key]
        else:
            hourly_weather = weather["0-" + str(int(current_time.split(":")[0]) + 1)]
        rain = hourly_weather["precip"]
        temp = hourly_weather["temp"]
        all_travel_times.append("0_" + str(model.predict([[day, hr, month, rain, temp]])[0]))

    # if number of stops listed is less than 'list_size', get stops from next day
    current_day = 1
    for i in all_departure_times:
        hr = i.split(":")[0]
        key = str(current_day) + "-" + hr
        hourly_weather = weather[key]
        rain = hourly_weather["precip"]
        temp = hourly_weather["temp"]
        all_travel_times.append("1_" + str(model.predict([[day, hr, month, rain, temp]])[0]))
    return all_travel_times
