import urllib.parse
import urllib.error
import requests
import json
from . import api_config
import pandas as pd


def live_data(dubbus_route, direction):
    if direction == "inbound":
        direction = "I"
    else:
        direction = "outbound"

    headers = {
            # Request headers
            'Cache-Control': 'no-cache',
            'x-api-key': api_config.apikey,
        }

    params = urllib.parse.urlencode({
    })

    gtfs = 'https://gtfsr.transportforireland.ie/v1/?format=json'
    r = requests.get(gtfs, params=params, headers=headers)
    data = json.loads(r.content)

    # convert the api data to a dataframe
    df = pd.json_normalize(data)
    df = df.drop(["header.timestamp", "header.gtfs_realtime_version"], axis=1)

    current_running_dubbus = []

    parsed = df.iloc[0][0]
    # find all the routes managed by operator "60" - Dublin Bus
    for entry in parsed:
        current_id = entry.get("id").split(".")

        # dublin bus route trip_id has a specific format, including a 60-, we want those routes only
        if len(current_id) == 5:
            id_sub_string = current_id[2]
            route_manager = id_sub_string.split("-")[0]

            if route_manager == "60":
                current_running_dubbus.append(id_sub_string)

    unique_routes = []
    for route in current_running_dubbus:
        route_num = route.split("-")[1]
        if route_num not in unique_routes:
            unique_routes.append(route_num)

    return_values = []

    for test in parsed:
        current_id = test.get("id").split(".")

        if len(current_id) == 5 and current_id[-1] == direction:
            route_sub_string = current_id[2]
            current_route = test.get("id").split("-")[1]
            route_manager = route_sub_string.split("-")[0]

            if route_manager == "60" and current_route == dubbus_route:
                trip_update_dict = test.get("trip_update")
                for key, value in trip_update_dict.items():
                    if key == "trip":
                        temp_list = []
                        for k, v in value.items():
                            if k == "start_time" or k == "route_id":
                                temp_list.append(v)
                        return_values.append(temp_list)

    return return_values

