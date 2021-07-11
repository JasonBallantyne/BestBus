import pandas as pd
import sqlite3

print("Reading in data files...")
stop_times = pd.read_csv("data/stop_times.txt")
stops_df = pd.read_csv("data/stops.txt")
all_routes_sequences = pd.read_csv("data/route_seqs.csv")
print("all files read in.")

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
Empty data frame ready.
Appending parsed data to new dataframe.
This is the longest part of the script, please be patient.""")

remaining = len(all_shapes)
for shape_id in all_shapes:
    current_shape_df = stop_times[stop_times["trip_id"].str.contains(shape_id)]
    no_repeats = current_shape_df.drop_duplicates(subset=['stop_sequence'], keep='first')
    new_df = new_df.append(no_repeats, ignore_index=True)
    remaining -= 1
    print(f"Appended data from shapeID {shape_id}")
    print(f"{remaining} shapes left.")

new_df = new_df.drop(['arrival_time',
                      'departure_time',
                      'pickup_type',
                      'drop_off_type',
                      'shape_dist_traveled'], axis=1)
print("Excess data cleared from new dataframe.")

merged_df = pd.merge(new_df, stops_df, left_on='stop_id', right_on='stop_id', how='left')
print("stops and new df merged")

# we need some data from an extra file containing more info per each stop
db_routes_sequences = all_routes_sequences[all_routes_sequences["Operator"] == "DB"]
db_stops_filtered = db_routes_sequences[["AtcoCode", "ShortCommonName_ga"]]
print("dublin bus irish stop names filtered and ready to merge in.")


# And now we need to merge in the irish name and make some other changes

# !! warning !! some of these functions take a long time to run,
# they will be optimised at a later point

# we need a list of stops paired with their irish names to match with the dataframe
my_list = [tuple(r) for r in db_stops_filtered.to_numpy()]
filtered_list = []
for item in my_list:
    filtered_list.append(item[0])


# function to find and append the irish name for the stop
def agus_ainm(row):
    if row['stop_id'] in filtered_list:
        item = my_list[filtered_list.index(row['stop_id'])]
        return item[1]


# function to find and match the row with its correct customer facing route number
def route_finder(row):
    id_strings = row['trip_id'].split('-')
    return id_strings[1]


# function to create id column values
def create_id(row):
    return row["shape_id"] + "_" + row["stop_num"]


# function for isolating the stop number for each row
def stop_finder(row):
    stop_string = row['stop_name'].split(' ')
    if stop_string[-1].isdigit:
        return stop_string[-1]
    else:
        return "No stop number."


# and one more to change the trip_id to a shape_id as we have no need of unique trip info here
# this whole process has been about removing duplicated "shape" data, so unique trips don't help
def trip_to_shape_id(row):
    id_string = row['trip_id'].split('.')
    shape_id = id_string[2] + '.' + id_string[3] + '.' + id_string[4]
    return shape_id


print("Merging and altering dateframe, this may take some time...")

merged_df['ainm'] = merged_df.apply(agus_ainm, axis=1)
print("Irish names added successfully.")

merged_df['route_num'] = merged_df.apply(route_finder, axis=1)
print("Route numbers added successfully.")

merged_df['shape_id'] = merged_df.apply(trip_to_shape_id, axis=1)
print("trip id removed and replaced with shape id.")

merged_df['stop_num'] = merged_df.apply(stop_finder, axis=1)
print("stop numbers added successfully.")

merged_df["id"] = merged_df.apply(create_id, axis=1)
print("row id value created successfully.")

print("Data successfully merged. Altering column headers...")

merged_df.rename(columns={"stop_headsign": "destination",
                          "stop_lat": "latitude",
                          "stop_lon": "longitude"}, inplace=True)

print("Complete. Loading to database now.")
db = sqlite3.connect("db.sqlite3")
merged_df.to_sql("bus_routes_busroute", db, if_exists="replace", index=False)
print("Finished. Whew, that was long...")
