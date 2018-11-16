============
BrokenChains
============
.. image:: https://travis-ci.org/bunya017/brokenChains.svg?branch=master
    :target: https://travis-ci.org/bunya017/brokenChains

BrokenChains is a habit tracking api built with ``django``
and ``djangoRestFramework``. Its an attempt to learn API
development with djangorestframework.


Requirements
------------

* Python 3.6+
* Django 2.2+
* djangorestframework 3.7+


Installation
------------
1. Create and activate a python virtual environment:
    * venv --your-env--
2. Activate the virtual environment:
    * --your-env--/Scripts/activate
    * pip install -r requirements.txt
3. Make and run migrations:
    * python manage.py makemigrations
    * python manage.py migrate


Usage
-----
Run ``python manage.py runserver`` to start the server and
open ``http://localhost:8000/api`` on your browser

``Note``: All actions require authentication/authorization.


API Endpoints
------------
* ``POST /api-token-auth`` - Get authorization token
* ``POST /api/users/signup`` - User registration
* ``GET /api/habits`` - List habits
* ``POST /api/habits`` - Create habit
* ``GET /api/habits/{id}`` - Show habit detail
* ``DELETE /api/habits/{id}`` - Delete habit
* ``GET /api/sessions`` - List sessions
* ``POST /api/sessions`` - Create session
* ``GET /api/sessions/{id}`` - Show session detail
* ``DELETE /api/sessions/{id}`` - Delete session


ToDo
----
* Web front-end client
* Android client
* iOs client
