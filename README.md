django-leaderboard-template
===========================

A Django leaderboard app template, using redis as its backend. This app is a wrapper for the python-leaderboard api `https://github.com/agoragames/leaderboard-python`

The app uses Redis key-value pairs for its back-end and stores the scores on its 'sorted set' data structure, which keeps the data ordered and allows us to retrieve, update and delete scores efficiently.

With this app, you can get the leaderboard with pagination, create scores, update or delete them. Even get rankings around the given score.

Features
--------

* RESTful api for creating, updating, deleting and retrieving high scores or scores around the user
* Standard view for displaying high scores with pagination

Not implemented features
------------------------

* delete method for the api

Requirements
------------

Python leaderboards module `pip install leaderboard`, note that this module will install redis and hiredis modules as its dependancy djangorestframework `pip install djangorestframework` for providing the rest behavior. `pip freeze > requirements.txt` to save all dependency requirements into a text file.

Usage
-----

Thanks to `djangorestframework`, you can just visit `http://localhost:8000/leaderboard/api/<game-identifier>/` to create, update or get the leaderboard.

Other urls are `http://localhost:8000/leaderboard/api/<game-identifier>/user/<user-id>/` for scores around the user, and `http://localhost:8000/leaderboard/api/<game-identifier>/<page-id>/` for pagination. Please see `urls.py` to see the full list or urls.

To create new ranking using the api, send a POST request to `http://localhost:8000/leaderboard/api/<game-identifier>/`. Game identifier is the key to determine your game to the system. it can be anything. Parameters are `user_id`and `score`.

To see the html table of leaderboard, go to `http://localhost:8000/leaderboard/highscores/<game-identifier>/` page.

Example
-------

There is an example project in the source to make it easy to start.

A sample project to try `django_leaderboard`

Dependencies
------------

Please see `requirements.txt` file for the complete dependancy list.

Installation
------------

Dependencies are added to the `requirements.txt` file. Usage of virtualenv is highly recommended. Please use the following steps to run this sample django project. Following steps requires using a terminal.

Use following to set up the project

    git clone `https://github.com/xxl4tomxu98/ttb-django-leaderboard-template/tree/master`
    cd ./ttb-django-leaderboard-template
    python3 -m venv venv
    source venv/bin/activate
    pip install --upgrade pip
    pip install wheel
    pip install -r requirements.txt
    cd ./samplegame
    python manage.py makemigrations
    python manage.py migrate      
    python manage.py runserver     

Open `settings.py` file and do the necessary changes (i.e. db settings, etc).

* Add `django_leaderboard` to APPS list in settings.py
* Make sure that your redis server is running.
* Add following lines to your urls.py file.

    url(r'^leaderboard/', include('django_leaderboard.urls')),
    url(r'^restframework', include('djangorestframework.urls', namespace='djangorestframework')) # auth support for rest framework

Go to `http://localhost:8000/` to use the project. Make sure that you create some users first.
