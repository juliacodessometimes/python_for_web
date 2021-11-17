# this is a forms practice app

# importing our libraries
from flask import Flask, render_template, request
# for this app we need Flask (to create our app object)
# render_template (to render templates or html files)
# and request (to use POST requests)

## instantiating the app object
app = Flask(__name__)

# here is our main database, which is really just a list of dictionaries
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

# here a dictionary of user emails and passwords
# notice how the emails are the keys of the dictionary, and the values are the passwords
users = {
    "jbloom@gmail.com": "apple",
    "suzieq@gmail.com": "orange1"
}

# here we create our first route which is our "default" or homepage
# we can specify what method we want this route to use using methods = []
# we don't need to specify GET since that is the default method, but here we are doing it just as an example!
@app.route("/", methods=['GET'])
def index():
    return render_template("index.html", 
    lang_list=lang_list)

# here is the route where we want to handle the login forms for our website
# since users need to send data (ie their email and passwords) to our server from the client,
# we need to specify that POST is allowed using methods=[]
@app.route('/login', methods=['GET', 'POST'])
def login():
    # the function login() checks method, and acts accordingly

    # if the request made is a POST request, then:
    if request.method == 'POST':
        # request.form[] looks for a form with that name in our template
        # the next 2 lines create 2 new variables called email and password from whatever the user entered in the form
        email = request.form["user_email"]
        password = request.form["user_password"]
        # if the variables email and password match what's in our dictionary called users
        if email in users and users[email] == password:
            # then, render the template login.html, with the added variable "message" set to: "Sucessfully logged in!"
            return render_template("login.html", message="Successfully logged in!")
        # otherwise, render login.html with the variable "message" set to: "Try again"
        return render_template("login.html", message="Try again")

    # if the method is not POST, then we render login.html by itself like normal!
    return render_template("login.html")

# try going to /login in your browser while your app is running
# what happens if you try to submit an incorrect email/password combination?
# what happens if you submit an email/password combination that exists in the dictinonary "users?"

# this is where we run our app
if __name__ == "__main__":
    app.run(
        debug = True,
        port = 3000
    )