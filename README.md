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


## Deploying on Heroku

Well, it is now time to move our app somewhere in the Cloud. Here's how to deploy in Heroku.

First, install Heroku (if you're on MacOs run `brew tap heroku/brew && brew install heroku`).

Add gunicorn to our virtualenv using and add it to our requirements

    source sb-admin/bin/activate
    python -m pip install gunicorn
    python -m pip freeze > requirements.txt

we have to tell Heroku how to run the app once deployed, using gunicorn which uses a Procfile

    echo "web: gunicorn application:application" > Procfile

in the main folder of the project.

Notice that we have to push an instance of our `db.sqlite` file which could be empty or not empty. The most important thing is that it is already initialized, e.g., with the user table already writted inside. If you deleted it, do initiliaze it as before, run `python`:

    from project import db, create_app
    db.create_all(app=create_app()) 
    exit()

Now that we got the database file, the gunicorn is defined, we can deploy it in Heroku.

First, login in your heroku and create your app choosing a name for the application and choosing a region of where you'd like to host it.

To upload the code, first you have to login in heroku-cli

    heroku login -i

then

    heroku git:remote -a sb-admin-demo

where `sb-admin-demo` is the name of the heroku app that you created just before.

add the virtualenv folder to your `.gitignore` using

    echo "sb-admin" > .gitignore

then

    git add *
    git commit -m "first commit"
    git push heroku master

and you should see something like this

```bash
...
remote: -----> Discovering process types
remote:        Procfile declares types -> web
remote:
remote: -----> Compressing...
remote:        Done: 45.1M
remote: -----> Launching...
remote:        Released v4
remote:        https://{your-project-name}.herokuapp.com/ deployed to Heroku
remote:
remote: Verifying deploy... done.
To https://git.heroku.com/{your-project-name}.git
   ae85864..4e63b46  master -> master
```


