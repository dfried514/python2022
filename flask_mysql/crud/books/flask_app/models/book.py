# import the function that will return an instance of a connection
from flask_app.config.mysqlconnection import connectToMySQL
# model the class after the table from our database
class Book:
    def __init__( self , data ):
        self.id = data['id']
        self.title = data['title']
        self.num_of_pages = data['num_of_pages']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    # Now we use class methods to query our database
    @classmethod
    def get_all_books(cls):
        query = "SELECT * FROM books;"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL('books_schema').query_db(query)
        # Create an empty list to append our instances of rows
        rows = []
        # Iterate over the db results and create class instances with cls.
        for row in results:
            rows.append( cls(row) )
        return rows
    @classmethod
    def get_book_with_id(cls, id):
        query = "SELECT * FROM books WHERE id=%d;" % (id)
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL('books_schema').query_db(query)
        # return class instance
        return cls(results[0])
    @classmethod
    def get_favorite_books(cls, authors_id):
        query = "SELECT * FROM books JOIN favorites ON favorites.books_id = books.id WHERE favorites.authors_id=%d;" % (authors_id)
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL('books_schema').query_db(query)
        # Create an empty list to append our instances of rows
        rows = []
        # Iterate over the db results and create class instances with cls.
        for row in results:
            rows.append( cls(row) )
        return rows
    @classmethod
    def get_not_favorite_books(cls, authors_id):
        query = "SELECT * FROM books WHERE books.id NOT IN (SELECT books.id FROM books JOIN favorites ON favorites.books_id = books.id WHERE favorites.authors_id=%d);" % (authors_id)
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL('books_schema').query_db(query)
        # Create an empty list to append our instances of rows
        rows = []
        # Iterate over the db results and create instances of rows with cls.
        for row in results:
            rows.append( cls(row) )
        return rows
    # class method to save our class instance to the database
    @classmethod
    def insert_new_book(cls, data ):
        query = "INSERT INTO books ( title, num_of_pages, created_at, updated_at ) VALUES ( %(title)s , %(num_of_pages)s , NOW() , NOW() );"
        # data is a dictionary that will be passed into the save method from server.py
        return connectToMySQL('books_schema').query_db( query, data )
    