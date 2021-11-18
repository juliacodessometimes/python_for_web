## import our libraries
from flask import Flask, render_template, jsonify, request
from flask_sqlalchemy import SQLAlchemy

## instantiating the app object
app = Flask(__name__)

# connecting to our database
# here Python is looking for a file called languages.db
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///languages.db'

# instantiating the database object
db = SQLAlchemy(app)

# creating the "model" or class called Languages
# you can think of these as the "columns" in your database
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


## Querying the database

# .query.all() gets us a list of all objects of the class "Languages"
lang_all = Languages.query.all()
# we can use print() to see the list in the terminal
print(lang_all)

# we can get the first object in the list using []
# and get the attribute Bio using dot notation
print(lang_all[0].Bio)

# here we are getting the attribute "Name" from first object in the list
print("The name of the first object in the list is:", lang_all[0].Name)

# .query.get() returns the row that matches the primary key in the ()
# in line 75 below, we get the object of the class Languages that has a primary key "1" and save it as a variable called "lang"
lang = Languages.query.get("1")
# we can use dot notation on the variable to get atrributes of the object
print(lang.lang_id)
print("The name of the object with the primary key '1' is:", lang.Name)


# Making changes to the database

# here we are getting the object with the primary key "2" and saving it as a variable called "javascript1"
javascript1 = Languages.query.get("2")
# here we are printing the attribute Name from that object
print(javascript1.Name)

# to change this attribute, we can use dot notation to get the attribute Name from the object and set it equal to "test"
javascript1.Name = "test"
# printing it in the terminal will show the change
print(javascript1.Name)

# and here we save our changes to the database again
db.session.commit()

# let's change it back so it makes sense on our site!
javascript1.Name = "JavaScript"
print(javascript1.Name)

# remember we need to save our changes:
db.session.commit()

# try changing the some attributes and refreshing your site!

# here create our first route which is our "default" or homepage
@app.route("/")
def index():
    lang_data = Languages.query.all()
    return render_template("index.html", lang_list=lang_data)

# in this route, <lang_id> is a variable that gets passed to the function below
@app.route("/details/<lang_id>")
def details(lang_id):
    # python takes the variable lang_id, and asks the database for the row with that as a primary key
    # we save this object as a variable called lang_item
    lang_item = Languages.query.get(lang_id)
    # then we pass lang_item to the template "details"
    return render_template("details.html", lang_item=lang_item)

# this is a route that has a converter "int:" and does math for us!
# we need to use the converter to do math because URLs are always strings
@app.route("/math/<int:number>")
def math(number):
    # this function takes whatever number we put in the URL after /math/
    # and multiplies it by itself
    return "The square of " + str(number) + " is " + str(number*number)
    # notice how we need to use the str() function, because we can only return strings


## this is where we run our app
# it goes at the bottom and we don't need to touch it!
if __name__ == "__main__":
    app.run(
        debug = True,
        port = 3000
    )