def to_time(seconds):
    hour = 3600
    minute = 60

    hours = str(int(seconds/hour))
    minutes = str(int((seconds % hour)/minute))
    seconds = str(int((seconds % hour) % 60))

    if len(hours) == 1:
        hours = f"0{hours}"
    if len(minutes) == 1:
        minutes = f"0{minutes}"
    if len(seconds) == 1:
        seconds = f"0{seconds}"

    timestamp = f"{hours}:{minutes}:{seconds}"

    return timestamp
