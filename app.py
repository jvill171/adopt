"""Blogly application."""
from flask import Flask, request, redirect, render_template, flash
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Pet
from forms import AddPetForm, EditPetForm

app = Flask(__name__)
app.app_context().push()
app.config['SECRET_KEY']="adoption-secret"

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///adoption'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

app.debug = True
debug=DebugToolbarExtension(app)
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

connect_db(app)
db.create_all()


@app.route('/')
def homepage():
    '''Homepage - Displays a pets name, photo, and availability'''
    pets = Pet.query.order_by(Pet.name).all()
    return render_template('home.html', pets=pets)

@app.route('/add', methods=['GET', 'POST'])
def add_pet():
    '''Form to add a new pet'''
    form = AddPetForm()

    if form.validate_on_submit():
        data = {k: v for k, v in form.data.items() if k != "csrf_token"}
        new_pet = Pet(**data)

        db.session.add(new_pet)
        db.session.commit()

        flash('Added {0} the {1}'.format(data['name'], data['species']))
        return redirect("/")
    else:
        return render_template('add-pet.html', form=form)
    
@app.route('/<int:pet_id>', methods=['GET', 'POST'])
def pet_info(pet_id):
    '''Displays pet information & allows the user to edit the photo_url, notse, and available status'''

    pet = Pet.query.get(pet_id)
    form = EditPetForm(obj=pet)

    if form.validate_on_submit():
        pet.photo_url = form.photo_url.data
        pet.notes = form.notes.data
        pet.available = form.available.data

        db.session.add(pet)
        db.session.commit()

        flash(f'Edited {pet.name}''s info')
        return redirect(f'/{pet_id}')

    else:
        return render_template('pet-info.html', pet=pet, form=form)