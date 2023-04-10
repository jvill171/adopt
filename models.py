from flask_sqlalchemy import SQLAlchemy
"""Models for Blogly."""

db = SQLAlchemy()

def connect_db(app):
    '''Connect to database.'''
    db.app = app
    db.init_app(app)

class Pet(db.Model):
    '''Pet.'''
    __tablename__ = 'pets'

    def __repr__(self):
        p = self
        return f'<Pet id={p.id}, name={p.name}, species={p.species}, photo_url={p.photo_url}, age={p.age}, notes={p.notes}, availabe={p.availabe}>'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.Text, nullable=False)
    species = db.Column(db.Text, nullable=False)
    photo_url = db.Column(db.Text, nullable=True)
    age = db.Column(db.Integer, nullable=True)
    notes = db.Column(db.Text, nullable=True)
    available = db.Column(db.Boolean, nullable=True, default=True)
