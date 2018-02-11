Django RESTful Api Example
=
In this example i followed [this](https://simpleisbetterthancomplex.com/tutorial/2018/02/03/how-to-use-restful-apis-with-django.html)
tutorial, but i did many things on my own and in my way. I think my version is much cleaner and easier to read. Also i worked a lot with all possible errors, so server should run smoothly.

Anton Demkin, 2018
antondemkin@yandex.ru

# How to install

Python3 is required.

1. Clone this repository
2. (optional) create virtual enviroment
3. install packages from requirements.txt
4. get api keys and create sercet key in .env file
6. make migrations to create fresh database
7. finally, run project!

```
git clone https://github.com/ADemkin/django-restful-api.git
cd django-restful-api/
pip3 install -r requirements.txt
touch djangorestfulapi/.env
nano djangorestfulapi/.env
```
Paste your keys into template. Ctrl + O to write file. Ctrl + x to exit Nano.
```
python3 python3 manage.py migrate
```

# Run project:
When in project folder run:
```
python3 manage.py runserver
```
Go to your browser and visit [local server](http://127.0.0.1:8000/)

# How to get api keys
To run this project you need some API keys.

#### Google API key
Get a key on [this](https://developers.google.com/maps/documentation/embed/) page.

#### Oxford Dictionary API key
1. register [here](https://developer.oxforddictionaries.com)
2. go to Api Credentials page
3. get Application ID
4. get Application Keys

#### Installing API keys
1. create .env file in /djangorestulapi/djangorestfulapi folder (near settings.py)
2. use template for variables
3. place your api keys into template

```
SECRET_KEY = [django secret key]
DEBUG = True
GOOGLE_MAPS_API_KEY = [google maps api key]
OXFORD_API_ID = [oxford application ID]
OXFORD_API_KEY = [oxford Application Keys]
```

# Project goal
This is educational project. I learned how to use restful api's with django templates.