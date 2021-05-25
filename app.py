from flask import Flask,render_template,redirect,flash
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db,Pet
from forms import AddPet

app = Flask(__name__)

app.config['SECRET_KEY'] = "oh-so-secret"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///pet_details'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

debug = DebugToolbarExtension(app)

connect_db(app)
db.create_all()

@app.route('/')
def home():
    """show all Pets"""
    pets = Pet.query.filter(Pet.Is_available == True).all()
    Nopets = Pet.query.filter(Pet.Is_available == False).all()
    return render_template('home.html',pets=pets,nopets=Nopets)
    
@app.route('/pet/new',methods=["POST","GET"])
def pet_new():
    """Add New Pet"""
    form = AddPet()
    
    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        photo_url = form.photo_url.data
        age = form.age.data
        notes = form.notes.data
        Is_available = form.Is_available.data
        
        pet = Pet(name=name,species=species,photo_url=photo_url,age=age,notes=notes,Is_available=Is_available)
        
        db.session.add(pet)
        db.session.commit()
        flash('New Pet Added')
        return redirect('/')
    else :
        return render_template('petForm.html',form=form)

@app.route('/pet/edit/<int:p_id>', methods=["POST","GET"])
def pet_edit(p_id):
    """Edit Pet Through Pet Id"""
    pet = Pet.query.get(p_id)
    form = AddPet()
    if form.validate_on_submit():
        pet.name = form.name.data
        pet.species = form.species.data
        pet.photo_url = form.photo_url.data
        pet.age = form.age.data
        pet.notes = form.notes.data
        pet.Is_available = form.Is_available.data
        
        db.session.commit()
        flash(f'{pet.name} is edited')
        return redirect('/')
    else :
        form.name.data = pet.name
        form.species.data = pet.species
        form.photo_url.data = pet.photo_url
        form.age.data = pet.age
        form.notes.data = pet.notes
        form.Is_available.data = pet.Is_available
        return render_template('petEdit.html',form=form,pet=pet)

    
