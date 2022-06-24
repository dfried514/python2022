# import the function that will return an instance of a connection
from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re 

# model the class after the table from our database
class Email:
    def __init__( self , data ):
        self.id = data['id']
        self.address = data['address']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    # Now we use class methods to query our database
    # class method to save our class instance to the database
    @classmethod
    def get_all_emails(cls):
        query = "SELECT * FROM email;"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL('emails_schema').query_db(query)
        # Create an empty list to append our class instances
        rows = []
        # Iterate over the db results and create class instances with cls.
        for row in results:
            rows.append( cls(row) )
        return rows
    @classmethod
    def insert_new_email(cls, data ):
        query = "INSERT INTO email ( address, created_at, updated_at ) VALUES ( %(address)s , NOW() , NOW() );"
        # data is a dictionary that will be passed into the save method from server.py
        return connectToMySQL('emails_schema').query_db( query, data )
    @classmethod
    def delete_email_with_id(cls, id ):
        query = "DELETE FROM email WHERE id=%d;" % (id)
        # data is a dictionary that will be passed into the save method from server.py
        return connectToMySQL('emails_schema').query_db( query )
    # Static methods don't have self or cls passed into the parameters.
    # We do need to take in a parameter to represent our burger
    @staticmethod
    def validate_email(data):
        print('data', data)
        # create a regular expression object 
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 
        is_valid = True
        # test whether a field matches the pattern
        if not EMAIL_REGEX.match(data['address']):
            flash("Invalid email address!")
            is_valid = False
        return is_valid
    