from flask_app import application
from flask import render_template,redirect,request,session,flash, url_for
from flask_app.models.like import Like
app = application

@app.route('/likes/like/<int:user_id>/<int:show_id>')
def insert_like(user_id, show_id):
    data = {
        'user_id': user_id,
        'show_id': show_id
    }
    Like.insert_like(data)
    return redirect(url_for('dashboard'))

@app.route('/likes/unlike/<int:user_id>/<int:show_id>')
def delete_like(user_id, show_id):
    data = {
        'user_id': user_id,
        'show_id': show_id
    }
    Like.delete_like(data)
    return redirect(url_for('dashboard'))
