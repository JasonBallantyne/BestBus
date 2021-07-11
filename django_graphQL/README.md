# A django-graphQL implementation.

## 1. Key Commands
### Requirements
run `pip install -r requirements.txt` from project root folder.

### `python manage.py runserver` 
Run the development server on windows, from the project root folder (django_graphQL).

### `python3 manage.py runserver`
Run the development server on Mac, from the project root folder (django_graphQL).

The corresponding url is the http://127.0.0.1:8000/, but this may differ on another machine. 

## 2. Directory Contents
`bus_routes/`
Django bus_routes application. Further readme details within.

`customers/`
Django customers application. Further readme details within.

`django_graphgQL/`
General django settings files, including url routing and provision for the above applications.

`db.sqlite3`
SQLite database containing routes and customers information.

`manage.py`
Provision of django functionality.

`requirements.txt`
Package requirements for django implementation.

`route_data_parser.py`
A script for parsing route data information from multiple web sources and inserting it to 
the SQLite db. Takes some time to run.

`gtfs_api_scraper.py`
Capacity for scraping the transport for ireland live gtfs data via api. Possibly redundant.

`gtfs_static_scraper.py`
Scrapes, unzips, and stores gtfs static data for use in route_data_parser.py. Some of these files are
large, sp they are listed in the .gitignore. Scraping them does not take too long and is only
necessary if updating the db with fresh routes data.

  
## 3. Tutorials and resources involved in the creation of this application

https://blog.logrocket.com/creating-an-app-with-react-and-django/

https://zoejoyuliao.medium.com/django-graphql-react-1-integrate-graphql-into-your-django-project-ff51237bb5d9

https://stackoverflow.com/questions/55442189/delete-mutation-in-django-graphql

https://docs.graphene-python.org/en/latest/types/objecttypes/#resolvers