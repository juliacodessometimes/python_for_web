## importing all of the libraries we used in this class
from flask import Flask, render_template, jsonify, request, abort
from flask_sqlalchemy import SQLAlchemy

## instantiating the app object
app = Flask(__name__)

# connecting to our database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///languages.db'

# instantiating the database object
db = SQLAlchemy(app)

# creating the database "model" or class called Languages
class Languages(db.Model):
    # each attribute acts as a column in our database
    lang_id = db.Column(db.String, primary_key=True)
    Image = db.Column(db.String, nullable=False)
    Name = db.Column(db.String)
    Age = db.Column(db.Integer)
    Bio = db.Column(db.String)


# this creates the model (or "columns") for our db object
db.create_all()

# since we have already created our database, we don't need to create objects or rows for our database!
# we can move right on to adding our routes

# here is our default route
@app.route("/")
def index():
    # this line grabs all the rows in our database and saves it as a list called lang_data
    lang_data = Languages.query.all()
    # don't forget to pass the list lang_data to the template!
    return render_template("index.html", lang_list=lang_data)

# here is our about page
@app.route("/about")
def about():
    return render_template("about.html")

# here is our dynamic route!
@app.route("/details/<slug>")
def details(slug):
    # python takes the variable slug in the URL, and asks the database for the object (aka row) with that as a primary key
    lang_item = Languages.query.get(slug)

    # here we add an if statement that checks if the integer of the slug is greater than the number of items in our list
    if int(slug) > len(Languages.query.all()):
        # and if it is, adds a message
        abort(404, description="No language with that id was found")

    # then we pass the lang_item to the template "details"
    return render_template("details.html", lang_item=lang_item)

# here is our api endpoint
@app.route("/api")
def api():
    # creating an empty list to hold all the dictionaries
    lang_json = []
    
    # here we loop through the list of objects returned by .query.all()
    for i in Languages.query.all():
        # creating a new dictionary called d and assigning the keys/values
        d = {
            "lang_id": i.lang_id,
            "Image": i.Image,
            "Name": i.Name,
            "Age": i.Age,
            "Bio": i.Bio
        }

        # and appending that dictionary to the empty list
        lang_json.append(d)

    return jsonify(lang_json)

## this is where we run our app
# it goes at the bottom and we don't need to touch it!
if __name__ == "__main__":
    app.run(
        debug = True,
        port = 3000
    )