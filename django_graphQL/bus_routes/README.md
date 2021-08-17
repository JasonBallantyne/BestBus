The bus_routes app is repsonsible for the creation of the bus_routes schema in our database.

The graphQL interface for this django app is found at http://127.0.0.1:8000.

The application contains the following files and directories:

## `route_models/`
Linear regression models for bus route predictions.
- Inputs for the prediction: Hour, Day, Month, Rain & Temperature.
- Outputs of the prediction: Journey Time.

## `migrations/`
Contains a record of migrations applied by Django to the bus_routes schema.

## `weather/`
Data parsing function for provision of current weather information to be sent to the front-end.

## `admin.py`
Creates functionality for this app at localhost:8000/admin (login required).

## `apps.py`
Creates the application bus_routes.

## `models.py`
Creates the BusRoute model class.

## `types.py`
Contains graphene object types

## `schema.py`
Creates a BusRoute object that can be queried by graphQL.

Querys housed here are as follows:

- resolve_unique_stops: returns every unique stop

- resolve_unique_routes: returns every unique route
![route1in](https://user-images.githubusercontent.com/71881578/126664189-0173cf28-a8f2-45e9-b0b3-b1d0119149a1.PNG)
![route1out](https://user-images.githubusercontent.com/71881578/126664199-8751caf9-cad0-4f65-9133-de88ebc01493.PNG)

- resolve_all_bus_routes: catch all. returns all data for all routes, no parameters required.
![allQ](https://user-images.githubusercontent.com/71881578/125189397-ce744a00-e22f-11eb-9914-c4a44b18ce2f.PNG)

- resolve_route_by_num: returns all data for a give route number (string: 155, 37, 70, etc). Route
number is a required parameter.
![routeByNumQ](https://user-images.githubusercontent.com/71881578/125189423-ec41af00-e22f-11eb-8661-c9c3e35683e8.PNG)

- resolve_route_by_stop: returns all data for a given stop (string: 7698, 4747, etc). Stop number 
a required parameter.
![routeByStopQ](https://user-images.githubusercontent.com/71881578/125189419-e946be80-e22f-11eb-99d7-97d16a0746fe.PNG)

- `resolve_weather`
This query returns a dictionary of hourly weather data for the next 24hrs.
The key for each dictionary entry follows the following format: "day from current day" + "-" + "hour"
Only 3 weather data items are included as this is all we require so far, this can be changed easily in the future if required
![image](https://user-images.githubusercontent.com/25707613/129356397-3ef299c8-0564-43af-a81e-11b7270a6bfd.PNG)

- `resolve_prediction`
This query is used to return a prediction of bus arrival times at all stops along a given route, the list size parameter tis used to filter the number of upcoming buses returned. The predictions are made using our previously trained random forest models, accounting for weather and time in making their predictions. An example query can be seen below:
![image](https://user-images.githubusercontent.com/25707613/129721425-6751b261-f7d3-4f81-a8dd-e2cfa0916f17.PNG)

- `resolve_stop_predictions`
This query is used to predict arrival times of all buses to a given stop, again list size filters to reutrn only a given number of buses. an example query can be seen below:
![image](https://user-images.githubusercontent.com/25707613/129721753-dd65a499-402e-4f2b-a297-016ffbb4cb0f.PNG)

## `tests.py`
Space for unittesting. No unittests currently applied.

## `urls.py`
Url routing provided for our app, directing to our graphQL portal.

## `views.py`
Provision available for page "views" for our app. None currently implemented.
