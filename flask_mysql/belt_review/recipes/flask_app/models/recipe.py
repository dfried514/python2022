# import the function that will return an instance of a connection
from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re

# model the class after the table from our database
class Recipe:
    def __init__( self , data ):
        self.id = data['id']
        self.name = data['name']
        self.description = data['description']
        self.instructions = data['instructions']
        self.date_made = data['date_made']
        self.under_30_minutes = data['under_30_minutes']
        self.user_id = data['user_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    # Now we use class methods to query our database
    # class method to save our class instance to the database
    @classmethod
    def get_recipe_with_id(cls, id):
        query = "SELECT * FROM recipes WHERE id='%s';" % (id)
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL('recipes_schema').query_db(query)
        # return instance of class
        if not results:
            return None
        return cls(results[0])
    @classmethod
    def get_all_recipes(cls):
        query = "SELECT * FROM recipes;"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL('recipes_schema').query_db(query)
        # Create an empty list to append our instances of rows
        rows = []
        # Iterate over the db results and create class instances with cls.
        for row in results:
            rows.append( cls(row) )
        return rows
    # class method to save our class instance to the database
    @classmethod
    def insert_new_recipe(cls, data ):
        query = "INSERT INTO recipes ( name, description, instructions, date_made, under_30_minutes, user_id, created_at, updated_at ) VALUES ( %(name)s , %(description)s, %(instructions)s , %(date_made)s , %(under_30_minutes)s , %(user_id)s, NOW() , NOW() );"
        # data is a dictionary that will be passed into the save method from server.py
        return connectToMySQL('recipes_schema').query_db( query, data )
    # class method to update our class instance to the database
    @classmethod
    def update_recipe(cls, data):
        query = "UPDATE recipes SET name = %(name)s, description = %(description)s, instructions = %(instructions)s, date_made = %(date_made)s, under_30_minutes = %(under_30_minutes)s, user_id = %(user_id)s, updated_at = NOW() WHERE id = %(id)s;"
        connectToMySQL('recipes_schema').query_db( query, data )
        # data is a dictionary that will be passed into the save method from server.py
    @classmethod
    def delete_recipe(cls, id ):
        query = "DELETE FROM recipes WHERE id = %s;" % id
        connectToMySQL('recipes_schema').query_db( query )
    # class method to return a class instance with no values, a dummy instance
    @classmethod
    def get_dummy_recipe(cls):
        dummy_data = {
            'id': '',
            'name': '',
            'description': '',
            'instructions': '',
            'date_made': '',
            'under_30_minutes': '',
            'user_id': '',
            'created_at': '',
            'updated_at': ''
        }
        return cls(dummy_data)
    @staticmethod
    # validate the data
    def validate_recipe(data):
        print('data', data)
            
        is_valid = True
        if len(data['name']) < 3:
            flash("Recipe name is not valid")
            is_valid = False
        if len(data['description']) < 3:
            flash("Recipe description is not valid")
            is_valid = False
        if len(data['instructions']) < 3:
            flash("Recipe instructions are not valid")
            is_valid = False
        if len(data['date_made']) == 0:
            flash("Must enter date made")
            is_valid = False
        if not 'under_30_minutes' in data:
            flash("Must choose selection for Under 30 Minutes?")
            is_valid = False 
        if len(data['user_id']) == 0:
            flash("Must enter user_id")
            is_valid = False           
        return is_valid
