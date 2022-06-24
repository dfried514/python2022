from flask_app import app
from flask import render_template,redirect,request,session,flash, url_for
from flask_app.models.dojo import Dojo

@app.route('/')
def new_dojo():
    return render_template("index.html")

@app.route('/result/<int:id>')
def result(id):
    return render_template("result.html", dojo=Dojo.get_dojo_with_id(id))

@app.route('/create_dojo', methods=['POST'])
def create_dojo():
    # if there are errors:
    # We call the staticmethod on class model to validate
    if not Dojo.validate_dojo(request.form):
        # redirect to the route where the burger form is rendered.
        return redirect('/')
    # else no errors:
    # We pass the data dictionary into the save method from the Dojo class.
    # Don't forget to redirect after saving to the database.
    return redirect(url_for('result', id=Dojo.insert_new_dojo(request.form)))
