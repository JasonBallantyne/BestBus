# function to find and append the irish name for the stop
def agus_ainm(row, first_list, filtered_list):
    if row['stop_id'] in filtered_list:
        item = first_list[filtered_list.index(row['stop_id'])]
        print(item[1])
        return item[1]


# function to find and match the row with its correct customer facing route number
def line_id(row):
    shape_id = row['shape_id']
    line_id = shape_id.split('-')[1]
    return line_id


# function to create id column values
def create_id(row):
    return row["shape_id"] + "_" + row["stop_num"]


def stop_sequencing_id(row):
    return row["line_id"] + "_" \
           + row["stop_num"] + "_" \
           + row["direction"] + "_" \
           + str(row["stop_sequence"])


# function for isolating the stop number for each row
def stop_number(row):
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
def shape_id(row):
    trip_id = row['trip_id']
    shape_strings = trip_id.split('.')
    shape_id = shape_strings[2] + '.' + shape_strings[3] + "." + shape_strings[4]
    return shape_id


def stops(row, df):
    all_stops = df["stop_num"]

    if len(all_stops) == 0:
        stops = "None"
    else:
        stops = ", ".join(all_stops)
    return stops


def names(row, df):
    all_names = df["stop_name"].tolist()
    names = ", ".join(all_names)
    return names


def stop_name(row):
    name = row["stop_name"].split(",")[0]
    return name


def coordinates(row, df, coordinate):
    all_coords = df[coordinate].unique().tolist()

    if len(all_coords) == 0:
        coord = "None"
    else:
        all_coords = ([str(x) for x in all_coords])
        coord = ", ".join(all_coords)
    return coord


def create_uniques_id(row):
    return row["line_id"] + "_" + row["direction"]


def gach_ainm(row, df):
    gach_ainm = df['ainm'].tolist()
    gach_ainm = ([str(x) for x in gach_ainm])
    gach_ainm = ", ".join(gach_ainm)

    return gach_ainm


def modify_df(df):
    if df.empty:
        pass
    else:
        df['stops'] = df.apply(stops, df=df, axis=1)
        df['longitudes'] = df.apply(coordinates, df=df, coordinate="longitude", axis=1)
        df['latitudes'] = df.apply(coordinates, df=df, coordinate="latitude", axis=1)
        df['names'] = df.apply(names, df=df, axis=1)
        df['gach_ainm'] = df.apply(gach_ainm, df=df, axis=1)
        df['id'] = df.apply(create_uniques_id, axis=1)

    df = df.drop(["stop_num", "latitude", "longitude",
                  "stop_name", "ainm", "stop_sequence",
                  "departure_time", "arrival_time", "stop_id"], axis=1)
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


def sorting_seconds(time_list):
    ftr = [3600, 60, 1]
    times_in_seconds = []

    for time in time_list:
        time_units = time.split(':')
        total_secs = (int(time_units[0]) * ftr[2]) + (int(time_units[1]) * ftr[1]) + (int(time_units[0]) * ftr[0])
        times_in_seconds.append(total_secs)

    times_in_seconds.sort()
    return times_in_seconds


def to_timestamp(seconds):
    hour = 3600
    minute = 60

    hours = str(int(seconds / hour))
    minutes = str(int((seconds % hour) / minute))

    if len(hours) == 1:
        hours = f"0{hours}"
    if len(minutes) == 1:
        minutes = f"0{minutes}"

    seconds = f"00"

    timestamp = f"{hours}:{minutes}:{seconds}"

    return timestamp


def sorted_timestamps(times_in_seconds):
    sorted_timestamps = []

    for time in times_in_seconds:
        sorted_timestamps.append(to_timestamp(time))

    return sorted_timestamps


def departure_times(df):
    first_stop = df[df["stop_sequence"] == 1]
    first_stop_times = first_stop["departure_time"].unique().tolist()
    sorted_seconds = sorting_seconds(first_stop_times)
    first_stop_times = sorted_timestamps(sorted_seconds)
    first_stop_times = ([str(x) for x in first_stop_times])
    first_stop_times = ", ".join(first_stop_times)
    return first_stop_times


def destination_whitespace(row):
    return row["destination"].lstrip()


def make_string(row):
    return int(row["stop_sequence"])


def sort_by_sequence(df):
    df['sort'] = df.apply(make_string, axis=1)
    df.sort_values('sort', inplace=True, ascending=True)
    df = df.drop('sort', axis=1)

    return df


def all_routes(row, df, pruned_df):
    all_lines_for_stop = df["line_id"].unique().tolist()

    return_list = []
    for line in all_lines_for_stop:
        # print(f"----{line}----")
        line_df = pruned_df[pruned_df["line_id"] == line]
        all_stops_seqs = line_df["stop_sequence"].unique().tolist()
        route_length = 0
        for stop in all_stops_seqs:
            if stop > route_length:
                route_length = stop

        # print("line length: ", route_length)
        filtered_df = df[df["line_id"] == line]
        sequence = filtered_df["stop_sequence"].unique().tolist()[0]
        destination = filtered_df["destination"].unique().tolist()[0]
        direction = filtered_df["direction"].unique().tolist()[0]
        # print("sequence: ", sequence)
        divisor = round(route_length / sequence, 2)

        return_list.append(f"[{line}, {divisor}, {direction}, {destination}]")

    return_list = ", ".join(return_list)
    return return_list