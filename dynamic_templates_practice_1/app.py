# this is dynamic templates practice app

# importing our libraries
# we need the class Flask for this example
# and the function render_template
from flask import Flask, render_template

# here we instantiate the app object
app = Flask(__name__)

# let's define a python variables:
test_var = "this is a variable called test_var"

# a list:
user_list = ["Betty", "Max", "Tom"]

# a dictionary:
betty_dict = {
    "Name":"Betty", 
    "Location":"NYC", 
    "Age": 30
    }

# a class called "People()"", and an object "person" made from that class:
class People():
    # this is the constuctor function
    def __init__(self, name, location, age):
        self.name = name
        self.location = location
        self.age = age

person = People("Max", "Miami", 36)

# here we are adding our first route to our app object using @app.route()
@app.route("/")
def index():
    # instead of returning plain text, we want our homepage to render a template
    # we have created a template called "index.html" in the templates folder
    # the function render_template() looks for a file of that name in the templates folder, and renders it in your browser
    return render_template("index.html")

# here is another route!
# this one has a name: "/jinja"
@app.route("/jinja")
def jinja_practice():
    # this function is rendering the template "jinja_practice.html"...
    # BUT it's also rendering some variables along with it!
    return render_template("jinja_practice.html", test=test_var, users=user_list, betty=betty_dict, person=person)
    # first, it's passing the python variable we created on line 12 "test_var" to the template as the jinja variable "test"
    # then it passes the list we created one line 15 as the jinja variable "users"
    # then it passes the dictionary "betty_dict" as the jinja variable "betty"
    # finally it passes the object "person" as the jinja variable "person"

    # now we can show these python objects on our template "jinja_practice.html"!
    # to use them, we have to call them by their jinja name: "test"/"users"/"betty"/"person"

    # check the code in the jinja_practice.html file to see it in action!

# try adding more variables or changing the above variables around
# go to /jinja in your browser while your app is running to see how jinja fills in our python variables
# now, try opening the jinja_practice.html in your browser without your app running. what is different?

## this is where we run our app
# it always goes at the bottom of our app.py file and we don't need to touch it!
if __name__ == "__main__":
    app.run(
        debug = True,
        port = 3000
    )