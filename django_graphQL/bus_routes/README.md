The bus_routes app is repsonsible for the creation of the bus_routes schema in our database.

The graphQL interface for this django app is found at http://127.0.0.1:8000.

The application contains the following files and directories:

`route_models/`
Linear regression models for bus route predictions.
- Inputs for the prediction: Hour, Day, Month, Rain & Temperature.
- Outputs of the prediction: Journey Time.

`migrations/`
Contains a record of migrations applied by Django to the bus_routes schema.

`weather/`
Data parsing function for provision of current weather information to be sent to the front-end.

`admin.py`
Creates functionality for this app at localhost:8000/admin (login required).

`apps.py`
Creates the application bus_routes.

`models.py`
Creates the BusRoute model class.

`types.py`
Contains graphene object types

`schema.py`
Creates a BusRoute object that can be queried by graphQL. Querys housed here are as follows:

- resolve_unique_stops: returns every unique stop

- resolve_unique_routes: returns every unique route
![route1in](https://user-images.githubusercontent.com/71881578/126664189-0173cf28-a8f2-45e9-b0b3-b1d0119149a1.PNG)
![route1out](https://user-images.githubusercontent.com/71881578/126664199-8751caf9-cad0-4f65-9133-de88ebc01493.PNG)

-resolve_all_bus_routes: catch all. returns all data for all routes, no parameters required.
![allQ](https://user-images.githubusercontent.com/71881578/125189397-ce744a00-e22f-11eb-9914-c4a44b18ce2f.PNG)

-resolve_route_by_num: returns all data for a give route number (string: 155, 37, 70, etc). Route
number is a required parameter.
![routeByNumQ](https://user-images.githubusercontent.com/71881578/125189423-ec41af00-e22f-11eb-8661-c9c3e35683e8.PNG)

-resolve_route_by_stop: returns all data for a given stop (string: 7698, 4747, etc). Stop number 
a required parameter.
![routeByStopQ](https://user-images.githubusercontent.com/71881578/125189419-e946be80-e22f-11eb-99d7-97d16a0746fe.PNG)

- resolve_weather
![image](https://user-images.githubusercontent.com/71881578/128151494-e791a60a-9a25-4cee-9f96-c8746aebc598.png)

`tests.py`
Space for unittesting. No unittests currently applied.

`urls.py`
Url routing provided for our app, directing to our graphQL portal.

`views.py`
Provision available for page "views" for our app. None currently implemented.
