from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, BooleanField, SelectField
from wtforms.validators import InputRequired, Optional, URL, NumberRange

class AddPetForm(FlaskForm):
    """Form for adding pets."""

    name = StringField("Pet's Name", validators=[InputRequired("Pet Name required")])
    species = SelectField("Species", choices=[("cat","Cat"), ("dog","Dog"), ("porcupine","Porcupine"),("fish","Fish")])
    photo_url = StringField("Photo URL",validators=[URL(), Optional()])
    age = IntegerField("Age",validators=[NumberRange(min=0, max=30, message="Age must be between 0 - 30"),Optional()])
    notes = StringField("Notes",validators=[Optional()])
    available = BooleanField("Is available for adoption")

class EditPetForm(FlaskForm):
    """Form for edintg pet details."""

    photo_url = StringField("Photo URL",validators=[URL(), Optional()])
    notes = StringField("Notes",validators=[Optional()])
    available = BooleanField("Is available for adoption")