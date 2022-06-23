from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models.ninja import Ninja
from flask_app.models.dojo import Dojo

@app.route('/new_ninja')
def new_ninja():
    dojos = Dojo.get_all_dojos()
    return render_template("new_ninja.html", all_dojos=dojos)

@app.route('/create_ninja', methods=["POST"])
def create_ninja():
    # First we make a data dictionary from our request.form coming from our template.
    # The keys in data need to line up exactly with the variables in our query string.
    data = {
        "fname": request.form["fname"],
        "lname" : request.form["lname"],
        "age" : request.form["age"],
        "dojo_id" : request.form["dojo_id"]
    }
    # We pass the data dictionary into the save method from the Ninja class.
    id = Ninja.insert_new_ninja(data)
    # Don't forget to redirect after saving to the database.
    return redirect('/dojos/' + data['dojo_id'])
