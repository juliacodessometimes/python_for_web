## this is a database practice app

# importing our libaries
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

## instantiating the app object
app = Flask(__name__)

# this is where i want the app to look for my database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///people.db'

# here we instantiate the database object
db = SQLAlchemy(app)

# class which is our data model
class Users(db.Model):
    name = db.Column(db.String, primary_key=True)
    age = db.Column(db.Integer)
    location = db.Column(db.String, nullable=False)

# creates the model
db.create_all()

user_1 = Users(name="Betty", age=30, location="New York")
user_2 = Users(name="Tom", age=62, location="Miami")

# this adds a row to our database
db.session.add(user_2)

# this saves our changes to our database
try:
    db.session.commit()
except Exception as e:
    db.session.rollback()
finally:
    db.session.close()

# here we are querying the database
# row_list is a list of all objects with the class Users
row_list = Users.query.all()
print(row_list)
print(type(row_list))

# we can access attributes of the first object in the list using . notation!
print(row_list[1].location)


# here create our first route which is our "default" or homepage
# since we don't have a template, let's just render some text
@app.route("/")
def index():
    return "hello world"

## this is where we run our app
# this goes at the bottom and we don't need to touch it!
if __name__ == "__main__":
    app.run(
        debug = True,
        port = 3000
    )