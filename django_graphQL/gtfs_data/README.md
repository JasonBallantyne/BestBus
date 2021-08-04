`route_data_parser.py`
A script for parsing route data information from multiple web sources and inserting it to 
the SQLite db. Takes some time to run.

`gtfs_api_scraper.py`
Capacity for scraping the transport for ireland live gtfs data via api. Requires api_config.py

`gtfs_static_scraper.py`
Scrapes, unzips, and stores gtfs static data for use in route_data_parser.py. Some of these files are
large, sp they are listed in the .gitignore. Scraping them does not take too long and is only
necessary if updating the db with fresh routes data.

`parsing_functions.py`
Contains functions for parsing data for `route_data_parser`

`weatherinfo.py`
Contains functions for parsing data from openweather api

`api_config.py`
Contains the api key for api_config.py (not hosted on github)
