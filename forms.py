from flask_wtf import FlaskForm
from wtforms import BooleanField, StringField,IntegerField,SelectField
from wtforms.validators import InputRequired, Email, Optional,url,NumberRange

class AddPet(FlaskForm):
    name = StringField("Name :",validators=[InputRequired(message="Enter Name")])
    species = SelectField("Species :",choices=[('1','cat'),('2','dog'),('3','porcupine')])
    photo_url = StringField("Photo Url :",validators=[Optional(),url(message="Please Enter valid URL")])
    age = IntegerField("Age :",validators=[Optional(),NumberRange(min=0,max=30,message='Age should be between 0-30')])
    notes = StringField("Notes :",validators=[Optional()])
    Is_available = BooleanField("Pet Available",validators=[Optional()],default=False)