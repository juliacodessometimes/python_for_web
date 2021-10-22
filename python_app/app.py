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
    {"Image": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Python-logo-notext.svg/220px-Python-logo-notext.svg.png",
    "Name": "Python",
    "Age": 30,
    "Bio": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Pellentesque euismod porttitor cursus. Vivamus aliquet leo ligula, quis interdum ante lobortis et. Donec volutpat orci quis ligula mollis, quis tempus augue hendrerit. Nulla augue ligula, fermentum eu nibh ut, porta varius arcu. Proin malesuada pulvinar blandit. Vestibulum elementum egestas nisl. Nulla feugiat nulla ut massa feugiat, sed efficitur mauris viverra. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Morbi ornare arcu mattis quam aliquet sollicitudin. Mauris dictum feugiat ante."},
    {"Image": "https://upload.wikimedia.org/wikipedia/commons/archive/6/6a/20120221235432%21JavaScript-logo.png",
    "Name": "JavaScript",
    "Age": 40,
    "Bio": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Pellentesque euismod porttitor cursus. Vivamus aliquet leo ligula, quis interdum ante lobortis et. Donec volutpat orci quis ligula mollis, quis tempus augue hendrerit. Nulla augue ligula, fermentum eu nibh ut, porta varius arcu. Proin malesuada pulvinar blandit. Vestibulum elementum egestas nisl. Nulla feugiat nulla ut massa feugiat, sed efficitur mauris viverra. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Morbi ornare arcu mattis quam aliquet sollicitudin. Mauris dictum feugiat ante."}
]

# here create our first route which is our "default" or homepage
# this is where we render our index.html template and add our lang_list variable that we want to render
@app.route("/")
def hello():
    return render_template("index.html", 
    lang_list=lang_list)

# here is a second webpage with the name "about"
# we are bringing 3 variables called test, betty, and users with us
@app.route("/about")
def about():
    return render_template("about.html",
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