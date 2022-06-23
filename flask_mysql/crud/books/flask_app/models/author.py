# import the function that will return an instance of a connection
from flask_app.config.mysqlconnection import connectToMySQL
# model the class after the table from our database
class Author:
    def __init__( self , data ):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    # Now we use class methods to query our database
    @classmethod
    def get_all_authors(cls):
        query = "SELECT * FROM authors;"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL('books_schema').query_db(query)
        # Create an empty list to append our instances of rows
        rows = []
        # Iterate over the db results and create class instances with cls.
        for row in results:
            rows.append( cls(row) )
        return rows
    @classmethod
    def get_author_with_id(cls, id):
        query = "SELECT * FROM authors WHERE id=%d;" % (id)
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL('books_schema').query_db(query)
        # return class instance
        return cls(results[0])
    @classmethod
    def get_favorite_authors(cls, books_id):
        query = "SELECT * FROM authors JOIN favorites ON favorites.authors_id = authors.id WHERE favorites.books_id=%d;" % (books_id)
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL('books_schema').query_db(query)
        # Create an empty list to append our instances of rows
        rows = []
        # Iterate over the db results and create class instances with cls.
        for row in results:
            rows.append( cls(row) )
        return rows
    @classmethod
    def get_not_favorite_authors(cls, books_id):
        query = "SELECT * FROM authors WHERE authors.id NOT IN (SELECT authors.id FROM authors JOIN favorites ON favorites.authors_id = authors.id WHERE favorites.books_id=%d);" % (books_id)
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
    def insert_new_author(cls, data ):
        query = "INSERT INTO authors ( name, created_at, updated_at ) VALUES ( %(name)s , NOW() , NOW() );"
        # data is a dictionary that will be passed into the save method from server.py
        return connectToMySQL('books_schema').query_db( query, data )
    