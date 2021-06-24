# A basic django-graphQL implementation.

## Requirements
run `pip install django, graphene, graphene_django`

### `python manage.py runserver` 
Run the development server on windows, from the project root folder (django_graphQL).

### `python3 manage.py runserver`
Run the development server on Mac, from the project root folder (django_graphQL)..

The corresponding url is the http://127.0.0.1:8000/, but this may differ on another machine. 

![graphQL_display](https://user-images.githubusercontent.com/71881578/122923945-1f91cc00-d35d-11eb-87c9-f255b29205c0.PNG)

It should be possible to use a front end language to pull this graphQL data as JSON. There is currently
only one entry in the array, a dummy entry for testing purposes. 

## Contents
### `manage.py`
For primary functionality execution - adding users, running the server, etc.

### `db.sqlite3`
A dummy sqlite file with a single data entry for testing purposes

### `django_graphQL`
Primary settings and url routing is located here.

### `customers`
Settings for a customers schema here. The data is located on the root address. 
  
