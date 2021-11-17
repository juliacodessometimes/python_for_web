# this is an api practice app

# import our libraries
from flask import Flask, render_template, jsonify
# for this app we need Flask (to create our app object)
# render_template (to render templates or html files)
# and jsonify (to render JSON data for our API)

## instantiating the app object
app = Flask(__name__)

# our API database
# which is really just a list of dictionaries!
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

# here is our main route
# it's where we render our index.html template or homepage
@app.route("/")
def index():
    return render_template("index.html", 
    lang_list=lang_list)


# this is our API "endpoint" 
# (when we render an API using jsonify() instead of a template, we call it an endpoint not a route!)
# it shows all of our data when we go to the URL "/api"
@app.route('/api')
def api_function():
    # this function renders our JSON data in the browser using jsonify
    return jsonify(lang_list)

# this is another endpoint for our API
# we added logic to it so it filters out data we don't want to show
@app.route('/api/filter')
def apifilter_function():
    # an empty list called results
    results = []

    # here we are looping through the list of dictionaries, lang_list
    for i in lang_list:
        # if the value for Age for that item is less than 30
        if i["Age"] < 30:
            # append or add that item (dictionary) to the list results!
            results.append(i)
    
    # finally, the browser renders our list using JSON
    return jsonify(results)

# try going to /api and /api/filter in your browser while your app is running!

# this is where we run our app
if __name__ == "__main__":
    app.run(
        debug = True,
        port = 3000
    )