# import the function that will return an instance of a connection
from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
# model the class after the table from our database
class Dojo:
    def __init__( self , data ):
        self.id = data['id']
        self.name = data['name']
        self.location = data['location']
        self.language = data['language']
        self.comment = data['comment']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    # Now we use class methods to query our database
    # class method to save our class instance to the database
    @classmethod
    def get_dojo_with_id(cls, id):
        query = "SELECT * FROM dojos WHERE id=%d;" % (id)
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL('dojo_survey_schema').query_db(query)
        # return instance of Dojo
        return cls(results[0])
    @classmethod
    def insert_new_dojo(cls, data ):
        query = "INSERT INTO dojos ( name, location, language, comment, created_at, updated_at ) VALUES ( %(name)s , %(location)s , %(language)s , %(comment)s , NOW() , NOW() );"
        # data is a dictionary that will be passed into the save method from server.py
        return connectToMySQL('dojo_survey_schema').query_db( query, data )
    # Static methods don't have self or cls passed into the parameters.
    # We do need to take in a parameter to represent our burger
    @staticmethod
    def validate_dojo(dojo):
        is_valid = True # we assume this is true
        if len(dojo['name']) < 3:
            flash("Name must be at least 3 characters")
            is_valid = False
        if len(dojo['location']) < 3:
            flash("Location must be at least 3 characters")
            is_valid = False
        if len(dojo['language']) < 2:
            flash("Language must be at least 2 characters")
            is_valid = False
        return is_valid
