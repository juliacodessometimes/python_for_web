## importing our libraries
# since we are using forms, we need "request"
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

## instantiating the app object
app = Flask(__name__)

# connecting to our database
# our database file is called languages.db
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

# adding data to our database
# this is one "row" or object in our database
lang_1 = Languages(
    lang_id = "1",
    Image = "../static/1.png",
    Name = "Python",
    Age = 30,
    Bio = "Python is an interpreted high-level general-purpose programming language."
)
# and this is another object or row in our database
lang_2 = Languages(
    lang_id = "2",
    Image = "../static/2.png",
    Name = "JavaScript",
    Age = 29,
    Bio = "JavaScript, often abbreviated as JS, is a programming language that conforms to the ECMAScript specification."
)

# these lines add our objects to the session
db.session.add(lang_1)
db.session.add(lang_2)

# this code is commiting our changes to the sesssion to the external database
try:
    db.session.commit()
except Exception as e:
    db.session.rollback()
finally:
    db.session.close()

# here is our default route
@app.route("/")
def index():
    # this line grabs all the rows in our database and saves it as a list called lang_data
    lang_data = Languages.query.all()
    # don't forget to pass the list lang_data to the template!
    return render_template("index.html", lang_list=lang_data)

# here is our dynamic route!
# in this route, <slug> is a variable that gets passed to the function below
@app.route("/details/<slug>", methods=["GET", "POST"])
def details(slug):
    # python takes the variable slug, and asks the database for the object (aka row) with that as a primary key
    lang_item = Languages.query.get(slug)

    # the line below checks if the method being used is POST
    if request.method == "POST":
        # if it is, it creates 2 variables  called form_age and form_bio
        # using whatever the user entered in the inputs named "age" and "bio"
        form_age = request.form["age"]
        form_bio = request.form["bio"]

        # next, it assigns the attributes Age and Bio of the item we grabbed on line 70
        # to the variables we created above
        lang_item.Age = form_age
        lang_item.Bio = form_bio

        # finally, it saves these changes to the external database!
        db.session.commit()

    # then we pass the final lang_item to the template "details"
    return render_template("details.html", lang_item=lang_item)


## this is where we run our app
# it goes at the bottom and we don't need to touch it!
if __name__ == "__main__":
    app.run(
        debug = True,
        port = 3000
    )