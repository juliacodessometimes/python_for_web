## import our libraries
from flask import Flask, render_template, jsonify, request

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

# our new API database
# which is really just a list of dictionaries!
lang_list = [
    {
    "id": 1,
    "Image": "static/1.png",
    "Name": "Python",
    "Age": 30,
    "Bio": "Python is an interpreted high-level general-purpose programming language."
    },
    {
    "id":2,
    "Image": "static/2.png",
    "Name": "JavaScript",
    "Age": 29,
    "Bio": "JavaScript, often abbreviated as JS, is a programming language that conforms to the ECMAScript specification."
    }
]

# here is another dictionary of user emails and passwords
users = {
    "jbloom@gmail.com": "apple",
    "suzieq@gmail.com": "orange1"
}

# here create our first route which is our "default" or homepage
# this is where we render our index.html template
@app.route("/", methods=['GET'])
def index():
    return render_template("index.html", 
    lang_list=lang_list)

# here is where we handle the login forms for our website
# since we are using POST methods, we need to specify what is allowed using methods=[]
@app.route('/login', methods=['GET', 'POST'])
def login():
    # if the request made is a POST request, then
    if request.method == 'POST':
        # create new variables called email and password from the forms in our template
        email = request.form["email"]
        password = request.form["password"]
        # if the variables email and password match what's in our dictionary called users
        if email in users and users[email] == password:
            # then, render the template, with an added variable
            return render_template("login.html", variable="Successfully logged in!")
        # otherwise, render login.html with a different message
        return render_template("login.html", variable="Try again")

    # if the method is not POST, then we render login.html by itself
    return render_template("login.html")

# this is our API endpoint (or route)
# it shows all of our data
@app.route('/api')
def api_function():
    return jsonify(lang_list)

# this is another endpoint for our API
# we added logic to it so it filters out data we don't want to show
@app.route('/api/filter')
def apifilter_function():
    results = []

    for i in lang_list:
        if i["Age"] < 30:
            results.append(i)
    
    return jsonify(results)

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