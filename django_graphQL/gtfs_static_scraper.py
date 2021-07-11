"""
This file is for scraping and storing the transport data necessary to populate
our database of stops and routes
"""


from urllib.request import urlopen
from zipfile import ZipFile

zipurl = 'https://transitfeeds.com/p/transport-for-ireland/782/latest/download'
# Download the file from the URL
zipresp = urlopen(zipurl)
# Create a new file on the hard drive
tempzip = open("/tmp/tempfile.zip", "wb")
# Write the contents of the downloaded file into the new file
tempzip.write(zipresp.read())
# Close the newly-created file
tempzip.close()
# Re-open the newly-created file with ZipFile()
zf = ZipFile("/tmp/tempfile.zip")
# Extract its contents into <extraction_path>
# note that extractall will automatically create the path
zf.extractall(path='data/')
# close the ZipFile instance
zf.close()
