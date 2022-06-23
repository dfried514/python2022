# import the function that will return an instance of a connection
from flask_app.config.mysqlconnection import connectToMySQL
# model the class after the table from our database
class Favorite:
    def __init__( self , data ):
        self.authors_id = data['authors_id']
        self.books_id = data['books_id']
    # class method to save our class instance to the database
    @classmethod
    def insert_new_favorite(cls, data ):
        query = "INSERT INTO favorites ( authors_id, books_id ) VALUES ( %(authors_id)s , %(books_id)s );"
        # data is a dictionary that will be passed into the save method from server.py
        return connectToMySQL('books_schema').query_db( query, data )
    