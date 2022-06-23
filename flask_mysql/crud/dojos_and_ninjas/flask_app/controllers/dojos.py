from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models.dojo import Dojo
from flask_app.models.ninja import Ninja

@app.route('/')
@app.route('/dojos')
def index():
    dojos = Dojo.get_all_dojos()
    return render_template("dojos.html", all_dojos=dojos)

@app.route('/dojos/<int:id>')
def dojo_show(id):
    dojo = Dojo.get_dojo_with_id(id)
    ninjas = Ninja.get_all_ninjas_with_dojo_id(id)
    return render_template("dojo_show.html", dojo=dojo, all_ninjas=ninjas)

@app.route('/create_dojo', methods=['POST'])
def create_dojo():
    # First we make a data dictionary from our request.form coming from our template.
    # The keys in data need to line up exactly with the variables in our query string.
    data = {
        "name": request.form["name"]
    }
    # We pass the data dictionary into the save method from the Dojo class.
    id = Dojo.insert_new_dojo(data)
    # Don't forget to redirect after saving to the database.
    return redirect('/dojos')
