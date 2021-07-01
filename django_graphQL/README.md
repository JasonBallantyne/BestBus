# A basic django-graphQL implementation.

### Requirements
run `pip install -r requirements.txt` from project root folder.

### `python manage.py runserver` 
Run the development server on windows, from the project root folder (django_graphQL).

### `python3 manage.py runserver`
Run the development server on Mac, from the project root folder (django_graphQL)..

The corresponding url is the http://127.0.0.1:8000/, but this may differ on another machine. 

![graphQL_display](https://user-images.githubusercontent.com/71881578/122923945-1f91cc00-d35d-11eb-87c9-f255b29205c0.PNG)

It should be possible to use a front end language to pull this graphQL data as JSON. There is currently
only one entry in the array, a dummy entry for testing purposes. 

## 1. Contents
### 1.1 `manage.py`
For primary functionality execution - adding users, running the server, etc.

### 1.2 `db.sqlite3`
A dummy sqlite file with a single data entry for testing purposes

### 1.3 `django_graphQL`
Primary settings and url routing is located here.

### 1.4 `customers`
The customers directory is a django application. It handles the creation and control of the "customers" schema in the database. This is currently a dummy database.

#### 1.4.1 `customers/models.py`
Handles the creation and structure of the database models. We extend the django models class to create our own model class, in this case "customers." This

#### 1.4.2 `customers/schema.py`
This provides functionality for the provision of graphQL mutations. Currently implemented mutations are listed below, and an example of a representative GraphQL statement:

`CreateCustomer`
Add an additional entrant to the schema.

mutation {
  createCustomer (name:"Sample Entrant", gender: "male") {
    id
    name
    gender
  }
}

`UpdateCustomer`
Alter an existing entrants data. Id is a required parameter.

mutation {
  updateCustomer (id:7, name:"Sample Entrant", gender:"male") {
    id
    name
    gender
  }
}


`DeleteCustomer`
Remove a previous included entrant.

mutation {
  deleteCustomer (id:8) {
    id
  }
}

#### 1.4.3 `customers/urls.py`
Handles the url path of the customers application. Also provides the graphQL interactive graphical display at that path. Below is a sample graphQL query for all
information in the sample database.

{  
  allCustomers {  
    id  
    name  
    gender  
  }  
}  
  
## 2. Tutorials and resources involved in the creation of this application

https://blog.logrocket.com/creating-an-app-with-react-and-django/

https://zoejoyuliao.medium.com/django-graphql-react-1-integrate-graphql-into-your-django-project-ff51237bb5d9

https://stackoverflow.com/questions/55442189/delete-mutation-in-django-graphql