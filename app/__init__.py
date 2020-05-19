from flask import Flask
from config import config_options
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager


db=SQLAlchemy()
login_manager=LoginManager()
login_manager.session_protection='strong'
login_manager.login_view='auth.login'

def create_app(config_name):
    app=Flask(__name__)

    #REGISTER CONFIGURATION
    app.config.from_object(config_options[config_name])

    #REGISTER EXTENTION
    db.init_app(app)
    login_manager.init_app(app)


    #REGISTER BLUEPRINT
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint,url_prefix='/authenticate')


    return app