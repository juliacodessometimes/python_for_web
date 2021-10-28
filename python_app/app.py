## import our libraries
from flask import Flask, render_template

## instantiating the app object
app = Flask(__name__)

# underneath our app object is where we will do a lot of coding

# this is a simple variable called test_var
test_var = "test"

# this is a dictionary called betty_dict
betty_dict = {
    "Name": "Betty",
    "Location": "NYC",
    "Age": 30
}

# this is a list called users
users = ["Betty", "Max", "Tom"]

# this is a list of dictionaries called lang_list
# there are 2 dictionaries items in the list
lang_list = [
    {
    "Image": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Python-logo-notext.svg/220px-Python-logo-notext.svg.png",
    "Name": "Python",
    "Age": 30,
    "Bio": "Python is an interpreted high-level general-purpose programming language."
    },
    {
    "Image": "https://upload.wikimedia.org/wikipedia/commons/archive/6/6a/20120221235432%21JavaScript-logo.png",
    "Name": "JavaScript",
    "Age": 29,
    "Bio": "JavaScript, often abbreviated as JS, is a programming language that conforms to the ECMAScript specification."
    }
]

# here create our first route which is our "default" or homepage
# this is where we render our index.html template
@app.route("/")
def index():
    return render_template("index.html", 
    lang_list=lang_list)

# here is another webpage with the name "practice"
# we are bringing 3 variables called test, betty, and users with us
@app.route("/practice")
def about():
    return render_template("practice.html",
    test=test_var,
    betty=betty_dict,
    users=users)


## this is where we run our app
# it goes at the bottom and we don't need to touch it!
if __name__ == "__main__":
    app.run(
        debug = True,
        port = 3000
    )