# SB Admin 2 + Flask + Flask Login + SQL Alchemy + Blueprints


## Prerequisites & Setup
There are three main packages we need for this project
- Flask
- Flask-Login
- Flask-SQLAlchemy

We’ll be using SQLite to avoid having to install any extra dependencies for the database.

Clone the repo using git, run on a terminal

    git clone git@github.com:peastuti/sb-admin-2-flask-login.git

navigate on it using

    cd sb-admin-2-flask-login

then, run

    python3 -m venv sb-admin

with sb-admin which will be the name of our virtual environment, call it as you wish, then

    source sb-admin/bin/activate

to activate the virtual environment.

At this point, we are able to install the packages needed

    python -m pip install flask flask-sqlalchemy flask-login jinja2

Now, you can initialize the database opening a python shell using

    python

from there

    from project import db, create_app
    db.create_all(app=create_app()) # pass the create_app result so Flask-SQLAlchemy gets the configuration.
 
At this point, you are ready to start. Type

    python application.py