from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models.author import Author
from flask_app.models.book import Book
from flask_app.models.favorite import Favorite

@app.route('/books')
def books():
    return render_template("books.html", books=Book.get_all_books())

@app.route('/books/<int:id>')
def book_show(id):
    book = Book.get_book_with_id(id)
    favorite_authors = Author.get_favorite_authors(id)
    not_favorite_authors = Author.get_not_favorite_authors(id)
    return render_template("book_show.html", book=book, favorite_authors=favorite_authors, not_favorite_authors=not_favorite_authors)

@app.route('/create_book', methods=['POST'])
def create_book():
    # First we make a data dictionary from our request.form coming from our template.
    # The keys in data need to line up exactly with the variables in our query string.
    data = {
        "title": request.form["title"],
        "num_of_pages": request.form["num_of_pages"]
    }
    # We pass the data dictionary into the save method from the Dojo class.
    id = Book.insert_new_book(data)
    # Don't forget to redirect after saving to the database.
    return redirect('/books')

@app.route('/add_book_favorite', methods=['POST'])
def add_book_favorite():
    data = {
        "authors_id": request.form["authors_id"],
        "books_id": request.form["books_id"]
    }
    id = Favorite.insert_new_favorite(data)
    return redirect('/books/' + data['books_id'])   
