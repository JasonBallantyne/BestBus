# A django-graphQL implementation.

## 1. Essential commands and requirements

### request and include appropriate config file in:
django_graphQL/bus_routes/weather/weather_config.py and
django_graphQL/gtfs_data/api_config.py

### run `pip install -r requirements.txt` from project root folder.

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

`data/`
contains sourcing and parsing scripts for various data sources used in the application.

`db.sqlite3`
SQLite database containing routes and customers information.

`manage.py`
Provision of django functionality.

`requirements.txt`
Package requirements for django implementation.

  
## 3. Tutorials and resources involved in the creation of this application

https://blog.logrocket.com/creating-an-app-with-react-and-django/

https://zoejoyuliao.medium.com/django-graphql-react-1-integrate-graphql-into-your-django-project-ff51237bb5d9

https://stackoverflow.com/questions/55442189/delete-mutation-in-django-graphql

https://docs.graphene-python.org/en/latest/types/objecttypes/#resolvers
