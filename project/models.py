from flask_login import UserMixin
from . import db

# class User(UserMixin):
class User(UserMixin, db.Model):
    id = db.Column(db.String, primary_key=True) # primary keys are required by SQLAlchemy
    email = db.Column(db.String(100), unique=True)
    firstName = db.Column(db.String(1000))
    lastName = db.Column(db.String(1000))
    password = db.Column(db.String(100))

    def __init__(self, id, email, firstName, lastName, password, active=True):
        self.id = id
        self.email = email
        self.firstName = firstName
        self.lastName = lastName
        self.password = password
        self.active = active
    
    def is_active(self):
        return self.is_active
    
    def is_anonymous(self):
        return False

    def is_authenticated(self):
        return True