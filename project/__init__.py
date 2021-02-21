from flask import Flask, app
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

# init SQLAlchemy so we can use it later in our models
db = SQLAlchemy()

def create_app():
    application = Flask(__name__)

    application.config['SECRET_KEY'] = '9OLWxND4o83j4K4iuopO'
    application.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
    application.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(application)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(application)

    from .models import User

    # blueprint for auth routes in our app
    from . import auth
    application.register_blueprint(auth.bp)

    @login_manager.user_loader
    def load_user(id):
        # since the user_id is just the primary key of our user table, use it in the query for the user
        return User.query.get(id)
    
    return application