def time_data():
    import requests

    time_api = 'https://www.timeapi.io/api/Time/current/zone?timeZone=Europe/Dublin'
    time = requests.get(time_api)
    response = time.status_code

    if response != 200:
        raise ValueError("url not reached.")

    time_data = time.json()
    #print(time_data)

    timestamp = time_data["time"]
    return timestamp
