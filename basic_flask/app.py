# this is an extremely basic flask app!

# importing our libraries
# we only need the class Flask for this example
from flask import Flask

# here we instantiate the app object
# we can name our app object whatever we like, but it's customary to name it "app"
app = Flask(__name__)

# here we are adding our first route to our app object using @app.route()
# this is the default route where you load your homepage
# you can tell it's the default because the URL is just "/"
@app.route("/")
def homepage():
    # directly underneath our route, we always need to define a function
    # this function tells our browser what to do at this route
    # here, we are just asking it to return some text!
    return "Hello! This is your app's homepage!"

# here is another route!
# this one has a name: "/about"
@app.route("/about")
def about():
    # instead of just rendering text, 
    # the function about() is rendering html (note the heading <h1> tags!)
    return "<h1>This is another route called /about!</h1>"


## this is where we run our app
# it always goes at the bottom of our app.py file and we don't need to touch it!
if __name__ == "__main__":
    app.run(
        debug = True,
        port = 3000
    )

# when we set "debug = True", we get a printout of what our app is doing in the terminal
# "port" specifies where on our computer we want to run our app
# (you can think of it as the final part of our server's ip address)

# to see our app in our browser, find the line:
# * Running on ... http:/...
# and copy paste the URL into your browser!
# try adding /about to the end of that URL to see your about page