The bus_routes app is repsonsible for the creation of the bus_routes schema in our database.

The graphQL interface for this django app is found at http://127.0.0.1:8000/routes.

The application contains the following files and directories:

`migrations/`
Contains a record of migrations applied by Django to the bus_routes schema.

`admin.py`
Creates functionality for this app at localhost:8000/admin (login required).

`apps.py`
Creates the application bus_routes.

`models.py`
Creates the BusRoute model class.

`schema.py`
Creates a BusRoute object that can be queried by graphQL. Three querys are housed here:

-resolve_all_bus_routes: returns all data for all routes, no parameters required.
![allQ](https://user-images.githubusercontent.com/71881578/125189397-ce744a00-e22f-11eb-9914-c4a44b18ce2f.PNG)

-resolve_route_by_num: returns all data for a give route number (string: 155, 37, 70, etc). Route
number is a required parameter.
![routeByNumQ](https://user-images.githubusercontent.com/71881578/125189423-ec41af00-e22f-11eb-8661-c9c3e35683e8.PNG)

-resolve_route_by_stop: returns all data for a given stop (string: 7698, 4747, etc). Stop number 
a required parameter.
![routeByStopQ](https://user-images.githubusercontent.com/71881578/125189419-e946be80-e22f-11eb-99d7-97d16a0746fe.PNG)


`tests.py`
Space for unittesting. No unittests currently applied.

`urls.py`
Url routing provided for our app, directing to our graphQL portal.

`views.py`
Provision available for page "views" for our app. None currently implemented.
