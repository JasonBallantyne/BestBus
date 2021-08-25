"""
This file is for scraping and storing the transport gtfs_data necessary to populate
our database of stops and routes
"""

import os
import pandas as pd
import requests
from urllib.request import urlopen
from zipfile import ZipFile

print("Downloading primary dataset.")
zipurl = 'https://transitfeeds.com/p/transport-for-ireland/782/latest/download'

# Download the file from the URL
print("Accessing zip.")
zipresp = urlopen(zipurl)
tempzip = open("tempfile.zip", "wb")

# Write the contents of the downloaded file into the new file
tempzip.write(zipresp.read())

# Close the newly-created file
tempzip.close()
# Re-open the newly-created file with ZipFile()
zf = ZipFile("tempfile.zip")

# Extract its contents into <extraction_path>
print("Writing dataset to path.")
zf.extractall(path='gtfs_datafiles/')

# close the ZipFile instance
zf.close()


# download our gtfs_data from another source
print("Downloading supplement excel sheet.")
route_sequences = "https://www.transportforireland.ie/transitData/route_sequences_report_20210511_ALL.xlsx"
resp = requests.get(route_sequences)

# write excel file to gtfs_data directory
print("Writing supplement excel sheet to path.")
output = open('gtfs_datafiles/route_seqs.xls', 'wb')
output.write(resp.content)
output.close()

print("Coverting excel sheet to csv.")
# convert file to csv
read_file = pd.read_excel("gtfs_datafiles/route_seqs.xls")

# Write the dataframe object into csv file
read_file.to_csv("gtfs_datafiles/route_seqs.csv",
                 index=None,
                 header=True)

print("Deleting redundant excel file")
os.remove("gtfs_datafiles/route_seqs.xls")
os.remove("gtfs_datafiles/agency.txt")
os.remove("gtfs_datafiles/calendar.txt")
os.remove("gtfs_datafiles/calendar_dates.txt")
os.remove("gtfs_datafiles/shapes.txt")
os.remove("gtfs_datafiles/routes.txt")
os.remove("gtfs_datafiles/trips.txt")
os.remove("tempfile.zip")

print("Finshed.")
