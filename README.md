# URL shortening with authorization

This is yest task.
It is necessary to write a service for shortening long links.

The service should include 4 pages:

1. User registration page.
2. User authorization page.
3. A page for shortening links.

   How it should work:
     + The site visitor enters any original URL in the input field as http://example.com/verylongurl...;
     + Presses the "Shorten" button;
     + Receives a unique short URL in response (example: http://yourdomain/8U7VuC).
   
   Don't use external Api like vk.cc etc.
   The short URL must be unique, redirect to the original link and be relevant forever, no matter how many times it has been used.
4. View the list of abbreviated links for the authorized user.


Non-functional requirements:
1. Programming language: Python 3.6+
2. Django 3+
3. Minimum required number of dependency libraries
4. Source code compliance PEP 8

It will be a plus:
1. Python 3.10 + Django 3.2.9
2. Deployed project

## Install

- git@github.com:ieasycat/URL-shortening-with-authorization.git
- virtualenv -p python3 env
- source env/bin/activate
- pip install -r requirements.txt

## Launching the application

- python manage.py runserver

## Heroku

[Heroku](https://url-short-v2.herokuapp.com/)
