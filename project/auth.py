# auth.py

from flask import Blueprint, render_template, request, redirect, flash, url_for
from flask_login import login_required, login_user, login_required, logout_user
from werkzeug.security import generate_password_hash, check_password_hash
from .models import User
from . import db
import uuid

bp = Blueprint('auth', __name__)


@bp.route('/login')
def login():
    return render_template('login.html')

@bp.route('/login', methods=['POST'])
def login_post():
    email = request.form.get('email')
    password = request.form.get('password')
    remember = True if request.form.get('remember') else False

    user = User.query.filter_by(email=email).first()

    # check if user actually exists
    # take the user supplied password, hash it, and compare it to the hashed password in database    
    if not user or not check_password_hash(user.password, password): 
        flash('Please check your login details and try again.')
        return redirect(url_for('auth.login')) # if user doesn't exist or password is wrong, reload the page

    # if the above check passes, then we know the user has the right credentials
    login_user(user, remember=remember)
    return redirect(url_for('index'))

@bp.route('/register')
def register():
    return render_template('register.html')

@bp.route('/register', methods=['POST'])
def register_post():

    email           = request.form.get('email')
    first_name      = request.form.get('firstName')
    last_name       = request.form.get('lastName')
    password        = request.form.get('password')
    rep_password    = request.form.get('repeatPassword')

    if password == rep_password:

        # if this returns a user, then the email already exists in database
        user = User.query.filter_by(email=email).first() # if this returns a user, then the email already exists in database

        if user: # if a user is found, we want to redirect back to signup page so user can try again  
            flash('Email address already exists')
            return redirect(url_for('auth.signup'))

        # create new user with the form data. Hash the password so plaintext version isn't saved.
        new_user = User(str(uuid.uuid4()), email, first_name, last_name, generate_password_hash(password, method='sha256'))

        # add the new user to the database
        db.session.add(new_user)
        db.session.commit()

        return redirect(url_for('auth.login'))
    else:
        flash('Passwords do not match.')
        return redirect(url_for('auth.register'))

@bp.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))
