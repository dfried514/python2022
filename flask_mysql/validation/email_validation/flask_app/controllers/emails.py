from flask_app import app
from flask import render_template,redirect,request,session,flash, url_for
from flask_app.models.email import Email

@app.route('/')
def new_email():
    return render_template("index.html")

@app.route('/create_email', methods=['POST'])
def create_email():
    # if there are errors:
    # We call the staticmethod on class model to validate
    if not Email.validate_email(request.form):
        # redirect to the route where the class form is rendered.
        return redirect('/')
    # else no errors:
    # We pass the data dictionary into the save method from the class.
    # Don't forget to redirect after saving to the database.
    # With success message flashed
    id = Email.insert_new_email(request.form)
    print('id', id)
    flash("Submitted email is valid, and has been entered into the database!")
    return redirect(url_for('success'))

@app.route('/success')
def success():
    emails=Email.get_all_emails()
    print('emails', emails)
    return render_template("success.html", emails=Email.get_all_emails())

@app.route('/delete_email/<int:id>')
def delete_email(id):
    Email.delete_email_with_id(id)
    return redirect(url_for('success'))