from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models.author import Author
from flask_app.models.book import Book
from flask_app.models.favorite import Favorite

@app.route('/')
@app.route('/authors')
def authors():
    return render_template("authors.html", authors=Author.get_all_authors())

@app.route('/authors/<int:id>')
def author_show(id):
    author = Author.get_author_with_id(id)
    favorite_books = Book.get_favorite_books(id)
    not_favorite_books = Book.get_not_favorite_books(id)
    return render_template("author_show.html", author=author, favorite_books=favorite_books, not_favorite_books=not_favorite_books)

@app.route('/create_author', methods=['POST'])
def create_author():
    # First we make a data dictionary from our request.form coming from our template.
    # The keys in data need to line up exactly with the variables in our query string.
    data = {
        "name": request.form["name"]
    }
    # We pass the data dictionary into the save method from the Dojo class.
    id = Author.insert_new_author(data)
    # Don't forget to redirect after saving to the database.
    return redirect('/authors')

@app.route('/add_author_favorite', methods=['POST'])
def add_author_favorite():
    data = {
        "authors_id": request.form["authors_id"],
        "books_id": request.form["books_id"]
    }
    id = Favorite.insert_new_favorite(data)
    return redirect('/authors/' + data['authors_id'])   