# function to find and append the irish name for the stop
def agus_ainm(row, first_list, filtered_list):
    if row['stop_id'] in filtered_list:
        item = first_list[filtered_list.index(row['stop_id'])]
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


def route_direction(row):
    trip_string = row['trip_id']
    direction = trip_string[-1]
    if direction == "O":
        return "outbound"
    if direction == "I":
        return "inbound"


# and one more to change the trip_id to a shape_id as we have no need of unique trip info here
# this whole process has been about removing duplicated "shape" gtfs_data, so unique trips don't help
def trip_to_shape_id(row):
    id_string = row['trip_id'].split('.')
    shape_id = id_string[2] + '.' + id_string[3] + '.' + id_string[4]
    return shape_id


def stops(row, df):
    current_route = row['route_num']
    stops_df = df[df['route_num'] == current_route]
    outbound_stops = stops_df[stops_df['direction'] == "outbound"]
    inbound_stops = stops_df[stops_df['direction'] == "inbound"]
    outbound_stops = outbound_stops["stop_num"].unique().tolist()
    inbound_stops = inbound_stops["stop_num"].unique().tolist()

    if row["direction"] == "outbound":
        stops = outbound_stops
    if row["direction"] == "inbound":
        stops = inbound_stops

    if len(stops) == 0:
        stops = "None"
    else:
        stops = ", ".join(stops)
    return stops


def names(row, df):
    current_route = row['route_num']
    current = df[df['route_num'] == current_route]
    inbound_names = current[current["direction"] == "inbound"]
    outbound_names = current[current["direction"] == "outbound"]
    inbound_names = inbound_names['stop_name'].unique().tolist()
    outbound_names = outbound_names['stop_name'].unique().tolist()

    if row["direction"] == "outbound":
        names = outbound_names
    if row["direction"] == "inbound":
        names = inbound_names

    if len(names) == 0:
        names = "None"

    else:
        names_modified = []
        for item in names:
            names_modified.append(item.split(",")[0])
        names = names_modified
        names = ([str(x) for x in names])
        names = ", ".join(names)
    return names


def coordinates(row, df, coordinate):
    current_route = row['route_num']
    current = df[df['route_num'] == current_route]
    inbound_coordinate = current[current["direction"] == "inbound"]
    outbound_coordinate = current[current["direction"] == "outbound"]
    inbound_coordinate = inbound_coordinate[coordinate].unique().tolist()
    outbound_coordinate = outbound_coordinate[coordinate].unique().tolist()

    if row["direction"] == "outbound":
        coord = outbound_coordinate
    if row["direction"] == "inbound":
        coord = inbound_coordinate

    if len(coord) == 0:
        coord = "None"
    else:
        coord = ([str(x) for x in coord])
        coord = ", ".join(coord)
    return coord


def create_uniques_id(row):
    return row["route_num"] + "_" + row["direction"]


def gach_ainm(row, df):
    current_route = row['route_num']
    ainm_df = df[df['route_num'] == current_route]
    gach_ainm = ainm_df['ainm'].unique().tolist()

    if len(gach_ainm) == 0:
        ainms = "None"
    else:
        gach_ainm = ([str(x) for x in gach_ainm])
        ainms = ", ".join(gach_ainm)
    return ainms


def find_longest(df):
    route_shapes = df["shape_id"].unique().tolist()
    longest_inbound = ""
    longest_outbound = ""
    length_inbound = 0
    length_outbound = 0

    for shape in route_shapes:
        temp_df = df[df["shape_id"] == shape]
        direction = temp_df["direction"].unique().tolist()

        if direction[0] == "inbound" and temp_df.shape[0] > length_inbound:
            longest_inbound = shape
            length_inbound = temp_df.shape[0]
        elif direction[0] == "outbound" and temp_df.shape[0] > length_outbound:
            longest_outbound = shape
            length_outbound = temp_df.shape[0]

    return [longest_outbound, longest_inbound]


def modify_merged_df(df, first_list, filtered_list):
    print("Merging and altering dateframe, this may take some time...")
    df['ainm'] = df.apply(agus_ainm, first_list=first_list, filtered_list=filtered_list, axis=1)
    df['route_num'] = df.apply(route_finder, axis=1)
    df['shape_id'] = df.apply(trip_to_shape_id, axis=1)
    df['stop_num'] = df.apply(stop_finder, axis=1)
    df["id"] = df.apply(create_id, axis=1)
    df["direction"] = df.apply(route_direction, axis=1)

    print("Data successfully merged. Altering column headers...")

    df.rename(columns={"stop_headsign": "destination",
                       "stop_lat": "latitude",
                       "stop_lon": "longitude"}, inplace=True)


def modify_df(df, shape):
    df = df[df["shape_id"] == shape]
    if df.empty:
        pass
    else:
        df['stops'] = df.apply(stops, df=df, axis=1)
        df['longitudes'] = df.apply(coordinates, df=df, coordinate="longitude", axis=1)
        df['latitudes'] = df.apply(coordinates, df=df, coordinate="latitude", axis=1)
        df['names'] = df.apply(names, df=df, axis=1)
        df['gach_ainm'] = df.apply(gach_ainm, df=df, axis=1)
        df['id'] = df.apply(create_uniques_id, axis=1)

    return df


def drop_columns(df):
    df = df[["id",
             "route_num",
             "stops",
             "latitudes",
             "longitudes",
             "direction",
             "destination",
             "names",
             "gach_ainm"]].sort_values(by='route_num')
    return df
