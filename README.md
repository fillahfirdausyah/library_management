# Library Management API
This is the API of Library Management using [Django](https://www.djangoproject.com/) and [Django Ninja](https://django-ninja.dev/) and for the database using mysql

## How to run?
first clone this repository then setup your enviroment, you can use [venv](https://docs.python.org/3/library/venv.html) or [anaconda](https://www.anaconda.com/) then follow this step :
- run this cmd on your terminal `pip install -r requirements.txt`
- copy file .env.example to .env then setup your database credential
- next you can make the migration using this command `python manage.py makemigrations api`
- then run the migrations using this command `python manage.py migrate`
- after that you can run the api service using `python manage.py runserver`
- open the API Docs with this url [http://localhost:8000/api/v1/docs](http://localhost:8000/api/v1/docs)
<img width="1462" alt="image" src="https://github.com/user-attachments/assets/cabdcc63-8c84-4f55-967c-72e4ba786482">


This project also includes unit tests. To run the unit tests, execute the following command : `python manage.py test api.v1.test`

## About the project
I created the database schema like this :
<img width="646" alt="image" src="https://github.com/user-attachments/assets/7df00874-f821-412d-8ad6-ce7b0384ee76">
