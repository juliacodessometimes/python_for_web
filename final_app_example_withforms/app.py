# importing our libaries
from flask import Flask, render_template, request, jsonify, abort
from flask_sqlalchemy import SQLAlchemy

#instantiating the flask object
app = Flask(__name__)

# this line points to where your database file is
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pets.db'

# creating the database object
db = SQLAlchemy(app)

# defining the database model, or columns
class Pets(db.Model):
    pet_id = db.Column(db.String, primary_key=True, unique=True)
    Image = db.Column(db.String, nullable=False)
    Name = db.Column(db.String, nullable=False)
    Breed = db.Column(db.String)
    Age = db.Column(db.Integer)

# this creates the model
db.create_all()

# now we create an object for each row, or item in our database!

# once we have run our code once and created the .db file, everything from here to line 70 can be deleted!
pet_1 = Pets(
    pet_id = "1",
    Image = "../static/1.jpg", 
    Name = "Spotty", 
    Breed = "Cat",
    Age = 3,
)
pet_2 = Pets(
    pet_id = "2",
    Image = "../static/2.jpg", 
    Name = "Ralph",
    Breed = "Dog",
    Age = 6,
)
pet_3 = Pets(
    pet_id = "3",
    Image = "../static/3.jpg", 
    Name = "Amber",
    Breed = "Dog",
    Age = 10,
)
pet_4 = Pets(
    pet_id = "4",
    Image = "../static/4.jpg", 
    Name = "Sarah",
    Breed = "Cat",
    Age = 9,
)

# our database has 4 objects in it, or 4 rows
# adding each row to the session
db.session.add(pet_1)
db.session.add(pet_2)
db.session.add(pet_3)
db.session.add(pet_4)

# and committing them to our pets.db file!
try:
    db.session.commit()
except Exception as e:
    db.session.rollback()
finally:
    db.session.close()
# once we have run our code once and created the .db file, everything from line 27 to here can be deleted!


# here is our "default" or homepage route
@app.route("/")
def index():
    # .query.all() creates a list of objects of the class Pets
    pet_data = Pets.query.all()
    # then we pass this list to the index.html template
    return render_template("index.html", all_pets=pet_data)

# here is our "about" route
@app.route("/about")
def about():
    return render_template("about.html")

# here is our dynamic route
# it's dynamic because it assigns whatever the user puts after /details/ as a variable called pet_id
@app.route("/details/<pet_id>", methods=["GET", "POST"])
def pet_details(pet_id):
    # .query.get() returns the database object (or row) with the matching primary key
    # in the line below, it's looking for the database object with the same primary key as pet_id
    pet_item = Pets.query.get(pet_id)
    # once it has found the object, it save it as the variable pet_item

    # this if statement checks if the integer version of pet_id is more than the number of pets in our list of pets
    if int(pet_id) > len(Pets.query.all()):
        # if it is, we get a message
        abort(404, description="No pet with that id was found")


    # the line below checks if the method being used is POST
    if request.method == "POST":
        # if it is, it creates 2 variables  called form_age and form_bio
        # using whatever the user entered in the inputs named "age" and "bio"
        form_breed = request.form["breed"]
        form_age = request.form["age"]

        # next, it assigns the attributes Age and Bio of the item we grabbed on line 70
        # to the variables we created above
        pet_item.Breed = form_breed
        pet_item.Age = form_age

        # finally, it saves these changes to the external database!
        db.session.commit()

    return render_template("details.html", pet_item=pet_item)

# here is our api endpoint
@app.route('/api/all')
def api_all():
    # we need to turn our objects into dictionaries

    # first create an empty list that will hold our dictionaries
    pet_json = []

    # then, create a for loop that will loop through our list of objects
    for pet in Pets().query.all():
        # and for each object, create a dictionary with the attributes of that object
        pet_dic = {
            "pet_id": pet.pet_id,
            "Image": pet.Image,
            "Name": pet.Name,
            "Breed": pet.Breed,
            "Age": pet.Age
        }

        # then append the dicionary to the empty list
        pet_json.append(pet_dic)

    return jsonify(pet_json)

# this is where we run our app
if __name__ == "__main__":
    app.run(
        debug = True,
        port = 3000
    )