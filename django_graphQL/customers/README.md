The customers app is repsonsible for the creation of the bus_routes schema in our database.

The graphQL interface for this django app is found at http://127.0.0.1:8000/.

The application contains the following files and directories:

`migrations/`
Contains a record of migrations applied by Django to the customers schema.

`admin.py`
Creates functionality for this app at localhost:8000/admin (login required).

`apps.py`
Creates the application customers.

`models.py`
Creates the Customers model class.

`schema.py`
This provides functionality for the provision of graphQL mutations and queries. One query
and three mutations are provided. They are listed here:

### Queries
-resolve_all_customers: returns all data of all customers
![showAllCust](https://user-images.githubusercontent.com/71881578/125189642-fca65980-e230-11eb-8914-5f064d3e78d2.PNG)

NOTE: Future creation of selective queries to be made!!

### Mutations
-create_customer: Add an additional entrant to the schema.
![createCust](https://user-images.githubusercontent.com/71881578/125189647-06c85800-e231-11eb-85fb-c710fe182e20.PNG)

-update_customer: Alter an existing entrants data. Id is a required parameter.
![updateCust](https://user-images.githubusercontent.com/71881578/125189649-0cbe3900-e231-11eb-84b0-9e4ec34f5282.PNG)

-delete_customer: Remove a previous included entrant.
![deleteCust](https://user-images.githubusercontent.com/71881578/125189658-19db2800-e231-11eb-8859-27ece8ed4cdb.PNG)

`urls.py`
Url routing provided for our app, directing to our graphQL portal.

`views.py`
Provision available for page "views" for our app. None currently implemented.
