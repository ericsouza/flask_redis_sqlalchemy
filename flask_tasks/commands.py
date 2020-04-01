import click 
from flask.cli import with_appcontext 
from flask_tasks.database import db

@click.command(name='create_database')
@with_appcontext
def create_database():
    db.create_all()