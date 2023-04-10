from models import db, Pet
from app import app

db.drop_all()
db.create_all()

#Pet
p1 = Pet(
    name='Spot',
    species='Dog',
    age=4,
    available=False)

p2 = Pet(
    name='Segan',
    species='Cat',
    photo_url='https://images.unsplash.com/photo-1611915387288-fd8d2f5f928b?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=880&q=80',
    age=2,
    notes='Timid to new people',
    available=False)

p3 = Pet(
    name='Astro',
    species='Dog',
    photo_url='https://images.unsplash.com/photo-1616567214738-22fc0c6332b3?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxzZWFyY2h8OXx8aHVza3l8ZW58MHx8MHx8&auto=format&fit=crop&w=400&q=60',
    age=1,
    notes='Very friendly')

p4 = Pet(
    name='Goldy',
    species='Fish',
    photo_url='https://images.unsplash.com/photo-1539236754983-085fe1449ba4?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=718&q=80',
    notes='Loves swimming')

db.session.add_all([p1, p2, p3, p4])
db.session.commit()