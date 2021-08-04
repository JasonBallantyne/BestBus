import pandas as pd
import sqlite3
from parsing_functions import *
import warnings
warnings.filterwarnings('ignore')

print("Reading in gtfs_data gtfs_datafiles...")
stop_times = pd.read_csv("gtfs_datafiles/stop_times.txt")
stops_df = pd.read_csv("gtfs_datafiles/stops.txt")
all_routes_sequences = pd.read_csv("gtfs_datafiles/route_seqs.csv")
print("all gtfs_datafiles read in.")

# I need a list of all "shapes"
all_shapes = []
all_trips = stop_times["trip_id"].tolist()
for route_id in all_trips:
    id_strings = route_id.split('.')
    shape_id = id_strings[2] + '.' + id_strings[3] + '.' + id_strings[4]
    if shape_id not in all_shapes:
        all_shapes.append(shape_id)
print("shapes list made")

# create an empty dataframe to fill from the stop_times df
# this may take some time
new_df = stop_times.iloc[0:0]
print("""
Empty gtfs_data frame ready.
Appending parsed gtfs_data to new dataframe.
This is the longest part of the script, please be patient.""")

remaining = len(all_shapes)
for shape_id in all_shapes:
    current_shape_df = stop_times[stop_times["trip_id"].str.contains(shape_id)]
    no_repeats = current_shape_df.drop_duplicates(subset=['stop_sequence'], keep='first')
    new_df = new_df.append(no_repeats, ignore_index=True)
    remaining -= 1
    print(f"Appended gtfs_data from shapeID {shape_id}")
    print(f"{remaining} shapes left.")

new_df = new_df.drop(['arrival_time',
                      'departure_time',
                      'pickup_type',
                      'drop_off_type',
                      'shape_dist_traveled'], axis=1)
print("Excess gtfs_data cleared from new dataframe.")

merged_df = pd.merge(new_df, stops_df, left_on='stop_id', right_on='stop_id', how='left')
print("stops and new df merged")

# we need some gtfs_data from an extra file containing more info per each stop
db_routes_sequences = all_routes_sequences[all_routes_sequences["Operator"] == "DB"]
db_stops_filtered = db_routes_sequences[["AtcoCode", "ShortCommonName_ga"]]
print("dublin bus irish stop names filtered and ready to merge in.")


# And now we need to merge in the irish name and make some other changes
# !! warning !! some of these functions take a long time to run,

# we need a list of stops paired with their irish names to match with the dataframe
first_list = [tuple(r) for r in db_stops_filtered.to_numpy()]
filtered_list = []
for item in first_list:
    filtered_list.append(item[0])

modify_merged_df(merged_df, first_list, filtered_list)

print("Creating unique stops dataframe.")
unique_stops = merged_df.drop_duplicates(subset=['stop_num'], keep='first')
unique_stops = unique_stops[["stop_id",
                             "latitude",
                             "longitude",
                             "stop_name",
                             "ainm",
                             "stop_num"]].sort_values(by='stop_id')

print("Creating unique routes dataframe.")
unique_routes = merged_df.drop_duplicates(subset=['route_num',
                                                  "direction",
                                                  "stop_sequence"], keep='first')

all_routes = merged_df["route_num"].unique().tolist()

route1 = merged_df[merged_df["route_num"] == "1"]
route_shapes = find_longest(route1)

# given a dummy shape, just so we can produce the skeleton df
append_df = modify_df(route1, route_shapes[0])
append_df = append_df.iloc[0:0]

for route in all_routes:
    current_route = unique_routes[unique_routes["route_num"] == route]
    route_shapes = find_longest(current_route)
    for route_shape in route_shapes:
        temp_df = modify_df(current_route, route_shape)
        append_df = append_df.append(temp_df)

append_df = drop_columns(append_df)
append_df = append_df.drop_duplicates(subset=['id'], keep="first")

print("Complete. Loading to database now.")
db = sqlite3.connect("../db.sqlite3")
unique_stops.to_sql("bus_routes_uniquestops", db, if_exists="replace", index=False)
merged_df.to_sql("bus_routes_busroute", db, if_exists="replace", index=False)
append_df.to_sql("bus_routes_uniqueroutes", db, if_exists="replace", index=False)
print("Finished. Whew, that was long...")
