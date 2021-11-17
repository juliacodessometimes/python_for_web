# this is dynamic templates practice app

# importing our libraries
# we need the class Flask for this example
# and the function render_template
from flask import Flask, render_template

# here we instantiate the app object
app = Flask(__name__)

# now that we have some data to show on our app, we need a way to store it
# dictionaries are good for storing multiple kinds of data usin keys:
python_dict = {
    "id": 1,
    "Image": "../static/1.png",
    "Name": "Python",
    "Age": 30,
    "Bio": "Python is an interpreted high-level general-purpose programming language."
}

# the above dictionary "python_dict" saves some information about the langage Python,
# including the name, age, bio, and the location of a picture of the Python logo in our files
# note how the image 1.png is saved in the static folder!

# but we want to save information about multiple programming languages!
# we can do this by putting dictionaries like the one above into a list:
lang_list = [
    {
    "id": 1,
    "Image": "../static/1.png",
    "Name": "Python",
    "Age": 30,
    "Bio": "Python is an interpreted high-level general-purpose programming language."
    },
    {
    "id":2,
    "Image": "../static/2.png",
    "Name": "JavaScript",
    "Age": 29,
    "Bio": "JavaScript, often abbreviated as JS, is a programming language that conforms to the ECMAScript specification."
    }
]

# the above "lang_list" is a list of dictionaries
# the first item in the list is the dictionary we defined on line 13
# the second item in the list is another dictionary with the same keys,
# except it contains information about the programming language javascript

# again, notice how both images (1.png and 2.png) are saved in our static folder!

# here we are adding our first route to our app object using @app.route()
@app.route("/")
def index():
    # function index() renders our index.html template, and passes the list lang_list as lang_list to that template
    return render_template("index.html", lang_list=lang_list)


# try adding more dictionaries to the list "lang_list" and see what happens!
# go to your homepage in your browser while your app is running to see how jinja fills the table
# now, try opening the index.html file in your browser without your app running. what changes?

# this is where we run our app
# it always goes at the bottom of our app.py file and we don't need to touch it!
if __name__ == "__main__":
    app.run(
        debug = True,
        port = 3000
    )