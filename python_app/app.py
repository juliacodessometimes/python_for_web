## import our libraries
from flask import Flask, render_template

## instantiating the app object
app = Flask(__name__)

# This is where we will code
# this is a variable
test_var = "test"

# this is a dictionary
betty_dict = {
    "Name": "Betty",
    "Location": "NYC",
    "Age": 30
}

# this is a list
users = ["Betty", "Max", "Tom"]

print(betty_dict["Name"])


# create a new list
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

# create our first route
@app.route("/")
def hello():
    return render_template("index.html", 
    lang_list=lang_list)

# here is a second webpage
@app.route("/about")
def about():
    return render_template("about.html",
    test=test_var,
    betty=betty_dict,
    users=users)


## This is where we run our app
if __name__ == "__main__":
    app.run(
        debug = True,
        port = 3000
    )