## Tutorial Sources
    Django/GraphQL tutorial: https://www.codecademy.com/article/smyja/how-to-use-graphql-with-django 
    Postgres Integration: https://stackpython.medium.com/how-to-start-django-project-with-a-database-postgresql-aaa1d74659d8 


### Setup

- **Environment**
    - Install Python 3.11.1
    - Install pip 23.0
- **Dependecies**
    - run:
      - `pip install -r requirements.txt`
- **Create and migrate database** 
    - Create a local postgres database
    - Create an `.env` file in the `restaurant_graphql_api` directory. You can use `.env.example` as an example.
    - run:
      - `python manage.py migrate`
- **Start the server**
    - Run:
      - `python manage.py runserver`
-**Create Superuser and seed database**
    - Create a superuser account by running:
        - `python manage.py createsuperuser`
    - Log into our application as an admin by visiting:
        - `/admin`
    - Add restaurants to the database by interacting with the admin dashboard.


### Endpoints

- Visit `\graphql ` to query the data


### Example Queries and Mutations
```
    query {
        restaurants {
            id
            name
            address
        }
    }
```

``` 
    mutation {
        updateRestaurant(id: 2, name: "Kada Plaza Ltd", address: "Lekki Gardens") {
            ok
            restaurant {
            id
            name
            address
            }
        }
    }
```
