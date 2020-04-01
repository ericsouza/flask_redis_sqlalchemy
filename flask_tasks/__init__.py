__version__ = '0.1.0'

from flask import Flask
from os import environ

from rq import Queue
from worker import conn

q = Queue(connection=conn)


from flask_tasks.database import db
from flask_tasks.api.resource import api_bp

from flask_tasks.commands import create_database

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = environ.get('SECRET_KEY')
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    db.init_app(app)

    app.register_blueprint(api_bp)
    app.cli.add_command(create_database)
    
    return app

