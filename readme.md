Django RESTful Api Example
=
In this example i followed [this](https://simpleisbetterthancomplex.com/tutorial/2018/02/03/how-to-use-restful-apis-with-django.html)
tutorial, but i did many things on my own and in my way. I think my version is much cleaner and easier to read. Also i worked a lot with all possible errors, so server should run smoothly.

#How to install

1. Clone this repository
2. (optional) create virtual enviroment
3. install packages from requirements.txt
4. create migrations for Django database
5. make migrations to create fresh database
6. get api keys 
7. place api keys in .env file
8. finally, run project!

```
git clone 
```

#How to get api keys
To run this project you need some API keys.

####Google API key
Get a key on [this](https://developers.google.com/maps/documentation/embed/) page.

####Oxford Dictionary API key
1. register on [developer.oxforddictionaries.com](https://developer.oxforddictionaries.com)
2. go to Api Credentials page
3. get Application ID
4. get Application Keys

####Installing API keys
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