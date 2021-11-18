## importing our libraries
from flask import Flask, render_template, jsonify
from flask_sqlalchemy import SQLAlchemy

## instantiating the app object
app = Flask(__name__)

# connecting to our database called languages.db
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///languages.db'

# instantiating the database object
db = SQLAlchemy(app)

# creating the database "model" or class called Languages
class Languages(db.Model):
    lang_id = db.Column(db.String, primary_key=True)
    Image = db.Column(db.String, nullable=False)
    Name = db.Column(db.String)
    Age = db.Column(db.Integer)
    Bio = db.Column(db.String)

# this creates the model (or "columns") for our db object
db.create_all()

# adding data to our database by creating objects from the above class
# in total, we are adding 3 objects or rows to our database
lang_1 = Languages(
    lang_id = "1",
    Image = "../static/1.png",
    Name = "Python",
    Age = 30,
    Bio = "Python is an interpreted high-level general-purpose programming language."
)
lang_2 = Languages(
    lang_id = "2",
    Image = "../static/2.png",
    Name = "JavaScript",
    Age = 29,
    Bio = "JavaScript, often abbreviated as JS, is a programming language that conforms to the ECMAScript specification."
)
lang_3 = Languages(
    lang_id = "3",
    Image = "../static/3.png",
    Name = "C++",
    Age = 36,
    Bio = "C++ was designed with an orientation toward system programming and embedded, resource-constrained software and large systems, with performance, efficiency, and flexibility of use as its design highlights."
)

# these lines add each of our objects to the session
db.session.add(lang_1)
db.session.add(lang_2)
db.session.add(lang_3)

# and then the db.session.commit() line commits the changes to the .db file
try:
    db.session.commit()
except Exception as e:
    db.session.rollback()
finally:
    db.session.close()

# here is the list of dictionaries we are using for our API
api_data = [
    {
        "lang_id": "1",
        "Image": "../static/1.png",
        "Name": "Python",
        "Age": 30,
        "Bio": "Python is an interpreted high-level general-purpose programming language."
    },
    {
        "lang_id": "2",
        "Image": "../static/2.png",
        "Name": "JavaScript",
        "Age": 29,
        "Bio": "JavaScript, often abbreviated as JS, is a programming language that conforms to the ECMAScript specification."
    },
    {
        "lang_id": "3",
        "Image": "../static/3.png",
        "Name": "C++",
        "Age": 36,
        "Bio": "C++ was designed with an orientation toward system programming and embedded, resource-constrained software and large systems, with performance, efficiency, and flexibility of use as its design highlights."
    }
]

# here is our default route
@app.route("/")
def index():
    # this line grabs all the rows in our database and saves it as a list called lang_data
    lang_data = Languages.query.all()
    # don't forget to pass the list lang_data to the template!
    return render_template("index.html", lang_list=lang_data)

# here is our about route
@app.route("/about")
def about():
    return render_template("about.html")

# here is our API endpoint
@app.route("/api")
def api():
    return jsonify(api_data)

# here is our dynamic route!
# in this route, <slug> is a variable that gets passed to the function below
@app.route("/details/<slug>")
def details(slug):
    # python takes the variable slug, and asks the database for the row with that as a primary key
    lang_item = Languages.query.get(slug)
    # then we pass that row to the template "details"
    return render_template("details.html", lang_item=lang_item)

## this is where we run our app
# it goes at the bottom and we don't need to touch it!
if __name__ == "__main__":
    app.run(
        debug = True,
        port = 3000
    )