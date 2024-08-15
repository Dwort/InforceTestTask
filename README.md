# **InforceTest**

### How to run the project:

```
docker compose build

docker compose up

docker-compose run app python manage.py createsuperuser 

docker-compose run app python manage.py makemigrations 

docker-compose run app python manage.py migrate
```

### How to run the tests:

```
docker compose exec web bash

pytest
```

### API Endpoints (Test using Postman or Web):

#### API Endpoints (employee actions):
* For testing tokens, first of all register test a user via admin.
```
api/token/ - Receive JWT token
api/token/refresh/ - Refresh JWT token

api/user/register/ - Register "employee" (not user for tokens).
api/user/all/ - Get all employees from DB.
api/user/<int:user_id>/ - CRUD operations for employees.
api/user/vote/<int:employee_id>/<int:menu_id>/ - vote for menu.
```

#### API Endpoints (restaurant actions):

```
api/rest/add/restaurant/ - Create new restaurant (add new to DB).
api/rest/add/menu/ - Create new menu (add new to DB).
api/rest/all/restaurant/ - Get all restaurants from DB.
api/rest/restaurant/<int:rest_id>/ - CRUD operations for restaurant.
api/rest/all/menu/ - Get all menus from DB.
api/rest/menu/<int:menu_id>/ - CRUD operations for menus.
api/rest/menu/today/ - Get current date menus.
api/rest/menu/today/count/ - Get current date results with number of votes.
```

### TODO list:
1. Authentication Upgrades: The user authentication and registration system can be improved, adding more security and entitlement checks.
2. Adding an .env file (to save and limit the use of sensitive data such as database data, environment passwords...)
3. Creation of deeper logic (various programs and functionality) for employees, restaurants and menus. More distribution of logic to microservices.
4. Implementation of the interaction of different versions of the application api v1 / v2 with similar logic. It is possible to implement verification and processing of application versions through MiddleWare (there is not enough time to do this).