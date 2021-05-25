from models import Pet,db,connect_db
from app import app

connect_db(app)
db.drop_all()
db.create_all()

pet1 = Pet(name="puppy",
            species="dog",
            photo_url="https://images.unsplash.com/photo-1537151625747-768eb6cf92b2?ixid=MXwxMjA3fDB8MHxzZWFyY2h8MXx8ZG9nfGVufDB8fDB8&ixlib=rb-1.2.1&auto=format&fit=crop&w=600&q=60",
            age=10)

pet2 = Pet(name="carly",
            species="dog",
            photo_url="https://images.unsplash.com/photo-1568572933382-74d440642117?ixid=MXwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHw%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=675&q=80",
            age=20)

pet3 = Pet(name="dodge",
            species="dog",
            photo_url="https://images.unsplash.com/photo-1541599540903-216a46ca1dc0?ixid=MXwxMjA3fDB8MHxzZWFyY2h8MTZ8fGRvZ3N8ZW58MHx8MHw%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=600&q=60",
            age=5)

pet4 = Pet(name="doggy",
            species="dog",
            photo_url="https://images.unsplash.com/photo-1541599540903-216a46ca1dc0?ixid=MXwxMjA3fDB8MHxzZWFyY2h8MTZ8fGRvZ3N8ZW58MHx8MHw%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=600&q=60",
            age=5,
            Is_available=False)

pet5 = Pet(name="carlos",
            species="dog",
            photo_url="https://images.unsplash.com/photo-1541599540903-216a46ca1dc0?ixid=MXwxMjA3fDB8MHxzZWFyY2h8MTZ8fGRvZ3N8ZW58MHx8MHw%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=600&q=60",
            age=5,
            Is_available=False)

db.session.add(pet1)
db.session.add(pet2)
db.session.add(pet3)
db.session.add(pet4)
db.session.add(pet5)

db.session.commit()