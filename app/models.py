from . import db,login_manager
from flask_login import UserMixin
from werkzeug.security import generate_password_hash,check_password_hash
from datetime import datetime


@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))
    
class User(db.Model,UserMixin):
    __tablename__='users'
    id=db.Column(db.Integer,primary_key=True)
    username=db.Column(db.String(),unique=True)
    email=db.Column(db.String())
    password_secure=db.Column(db.String)
    gender=db.Column(db.String)

    @property
    def password(self):
        raise AttributeError('Cannot access password!')

    @password.setter
    def password(self,password):
        self.password_secure=generate_password_hash(password)
    
    def verify_password(self,password):
        return check_password_hash(self.password_secure,password)

    def __repr__(self):
        return self.username


