from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models.user import User

@app.route('/')
def index():
    users = User.get_all_users()
    return render_template("index.html", all_users=users)

@app.route('/new_user')
def new_user():
    return render_template("new_user.html")

@app.route('/create_user', methods=["POST"])
def create_user():
    # First we make a data dictionary from our request.form coming from our template.
    # The keys in data need to line up exactly with the variables in our query string.
    data = {
        "fname": request.form["fname"],
        "lname" : request.form["lname"],
        "email" : request.form["email"]
    }
    # We pass the data dictionary into the save method from the Friend class.
    id = User.insert_new_user(data)
    # Don't forget to redirect after saving to the database.
    return redirect('/show_user/' + str(id))

@app.route('/update_user', methods=["POST"])
def update_user():
    # First we make a data dictionary from our request.form coming from our template.
    # The keys in data need to line up exactly with the variables in our query string.
    # id value is included as a hidden input tag
    data = {
        "id": request.form["id"],
        "fname": request.form["fname"],
        "lname" : request.form["lname"],
        "email" : request.form["email"]
    }
    # We pass the data dictionary into the save method from the User class.
    User.update_user(data)
    # Don't forget to redirect after saving to the database.
    return redirect('/show_user/' + data['id'])

@app.route('/show_user/<int:id>')
def show_user(id):
    user = User.get_user(id)
    return render_template("show_user.html", user=user)

@app.route('/edit_user/<int:id>')
def edit_user(id):
    user = User.get_user(id)
    return render_template("edit_user.html", user=user)

@app.route('/delete_user/<int:id>')
def delete_user(id):
    User.delete_user({"id": id})
    return redirect('/')

