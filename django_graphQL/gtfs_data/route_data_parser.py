import pandas as pd
import sqlite3
import warnings
from parsing_functions import *

warnings.filterwarnings('ignore')

print("reading in data files...")
stop_times = pd.read_csv("gtfs_datafiles/stop_times.txt")
stop_times = stop_times.rename(columns={"stop_headsign": "destination"})
stop_times = stop_times.drop(["pickup_type", "drop_off_type", "shape_dist_traveled"], axis=1)
stop_times["destination"] = stop_times.apply(destination_whitespace, axis=1)
stops_df = pd.read_csv("gtfs_datafiles/stops.txt")
stops_df = stops_df.rename(columns={'stop_lat': 'latitude',
                                    "stop_lon": "longitude"})
ceann_scribe = pd.read_csv("gtfs_datafiles/ainms_ceann_scribe.csv")

print("creating merged dataframe")
merged_df = pd.merge(stop_times, stops_df, left_on='stop_id', right_on='stop_id')

# we need some gtfs_data from an extra file containing more info per each stop
print("adding irish names to dataframe")
all_routes_sequences = pd.read_csv("gtfs_datafiles/route_seqs.csv")
db_routes_sequences = all_routes_sequences[all_routes_sequences["Operator"] == "DB"]
db_stops_filtered = db_routes_sequences[["AtcoCode", "ShortCommonName_ga"]]

first_list = [tuple(r) for r in db_stops_filtered.to_numpy()]
filtered_list = []
for item in first_list:
    filtered_list.append(item[0])

print("modifying merged dataframe")
merged_df['ainm'] = merged_df.apply(agus_ainm, first_list=first_list, filtered_list=filtered_list, axis=1)

print("adding shape_id")
merged_df["shape_id"] = merged_df.apply(shape_id, axis=1)

print("adding line_id")
merged_df["line_id"] = merged_df.apply(line_id, axis=1)

print("adding route direction")
merged_df["direction"] = merged_df.apply(route_direction, axis=1)

print("adding stop numbers")
merged_df["stop_num"] = merged_df.apply(stop_number, axis=1)

print("adding stop names")
merged_df["stop_name"] = merged_df.apply(stop_name, axis=1)

print("adding irish destination names")
merged_df["ceann_scribe"] = merged_df.apply(agus_ceann_scribe, df=ceann_scribe, axis=1)

print("removing null values where irish names not present. replace with english names.")
merged_df["ceann_scribe"].fillna(merged_df["destination"], inplace=True)
merged_df["ainm"].fillna(merged_df["stop_name"], inplace=True)

print("done. creating list of line_ids and an empty dataframe")
line_list = merged_df["line_id"].unique().tolist()

col_names = ['destination', 'ceann_scribe', 'first_departure_schedule',
             'stops', 'longitudes', 'latitudes', 'names',
             'id', 'gach_ainm', 'line_id', 'direction']
final_df = pd.DataFrame(columns=col_names)

print("creating final modifications and unique stops dataframe")
final_df = final_df.drop_duplicates(subset=["id"], keep='first')


for line in line_list:
    longest_outbound, longest_inbound = longest_shapes(line, merged_df)
    longest_outbound = merged_df[merged_df["shape_id"] == longest_outbound]
    longest_inbound = merged_df[merged_df["shape_id"] == longest_inbound]

    longest_outbound["first_departure_schedule"] = departure_times(longest_outbound)
    longest_inbound["first_departure_schedule"] = departure_times(longest_inbound)

    longest_outbound = longest_outbound.drop_duplicates(subset=['stop_sequence'], keep='first')
    longest_inbound = longest_inbound.drop_duplicates(subset=['stop_sequence'], keep='first')

    if not longest_outbound.empty:
        longest_outbound = sort_by_sequence(longest_outbound)
    if not longest_inbound.empty:
        longest_inbound = sort_by_sequence(longest_inbound)

    longest_outbound = longest_outbound.drop(["shape_id", "trip_id"], axis=1)
    longest_inbound = longest_inbound.drop(["shape_id", "trip_id"], axis=1)

    longest_inbound = modify_df(longest_inbound)
    longest_outbound = modify_df(longest_outbound)

    final_df = final_df.append(longest_inbound)
    final_df = final_df.append(longest_outbound)

final_df = final_df.drop_duplicates(subset=["id"], keep='first')

merged_df["id"] = merged_df.apply(create_id, axis=1)
merged_df = merged_df.drop(["arrival_time", "departure_time", "trip_id"], axis=1)

unique_stops = merged_df.drop_duplicates(subset=['stop_num'], keep='first')
unique_stops = unique_stops[["stop_id",
                             "latitude",
                             "longitude",
                             "stop_name",
                             "ainm",
                             "stop_num"]].sort_values(by='stop_id')

col_names = ["stop_id",
             "stop_sequence",
             "destination",
             "stop_name",
             "latitude",
             "longitude",
             "ainm",
             "shape_id",
             "line_id",
             "direction",
             "stop_num",
             "id"]

pruned_df = pd.DataFrame(columns=col_names)

for line in line_list:
    longest_outbound, longest_inbound = longest_shapes(line, merged_df)

    longest_outbound = merged_df[merged_df["shape_id"] == longest_outbound]
    longest_inbound = merged_df[merged_df["shape_id"] == longest_inbound]

    pruned_df = pruned_df.append(longest_inbound)
    pruned_df = pruned_df.append(longest_outbound)

all_stops = pruned_df["stop_num"].unique().tolist()

col_names = ["stop_sequence", "line_id", "direction", "destination", "stop_num", "stop_route_data"]
stop_sequencing = pd.DataFrame(columns=col_names)

pruned_df = pruned_df.drop(["stop_name",
                            "latitude",
                            "longitude",
                            "ainm",
                            "stop_id",
                            "id",
                            "shape_id"], axis=1)

pruned_df = pruned_df.drop_duplicates()

count = 1
for stop in all_stops:
    print(f"Processing stop {stop}. {count} of {len(all_stops) + 1}")
    stop_df = pruned_df[pruned_df["stop_num"] == stop]
    stop_df = stop_df.drop_duplicates()
    stop_df["stop_route_data"] = stop_df.apply(all_routes, df=stop_df, pruned_df=pruned_df, axis=1)
    stop_sequencing = stop_sequencing.append(stop_df)
    count += 1

stop_sequencing = stop_sequencing.drop(["line_id", "stop_sequence", "direction", "destination", "ceann_scribe"], axis=1)
stop_sequencing = stop_sequencing.drop_duplicates()

print("Complete. Loading to database now.")
db = sqlite3.connect("../db.sqlite3")
stop_sequencing.to_sql("bus_routes_stopsequencing", db, if_exists="replace", index=False)
unique_stops.to_sql("bus_routes_uniquestops", db, if_exists="replace", index=False)
final_df.to_sql("bus_routes_uniqueroutes", db, if_exists="replace", index=False)
print("Finished. Whew, that was long...")
