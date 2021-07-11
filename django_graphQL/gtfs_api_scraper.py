import urllib.parse, urllib.error
import requests, json


headers = {
        # Request headers
        'Cache-Control': 'no-cache',
        'x-api-key': '4e576c9c2e4045c7b060cf591a172fbf',
    }

params = urllib.parse.urlencode({
})

gtfs = 'https://gtfsr.transportforireland.ie/v1/?format=json'
r = requests.get(gtfs, params=params, headers=headers)
data = json.loads(r.content)
print(data)