# import the function that will return an instance of a connection
from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re

# model the class after the table from our database
class User:
    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.dob = data['dob']
        self.os = data['os']
        self.location = data['location']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    # Now we use class methods to query our database
    # class method to save our class instance to the database
    @classmethod
    def get_user_with_email(cls, email):
        query = "SELECT * FROM users WHERE email='%s';" % (email)
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL('users_schema').query_db(query)
        # return instance of class
        if not results:
            return None
        return cls(results[0])
    # class method to save our class instance to the database
    @classmethod
    def insert_new_user(cls, data ):
        query = "INSERT INTO users ( first_name, last_name, email, dob, os, location, password, created_at, updated_at ) VALUES ( %(first_name)s , %(last_name)s, %(email)s , %(dob)s , %(os)s , %(location)s , %(password)s , NOW() , NOW() );"
        # data is a dictionary that will be passed into the save method from server.py
        return connectToMySQL('users_schema').query_db( query, data )
    @staticmethod
    def validate_user(data):
        print('data', data)
        email_regex = '^\w+@\w+\.[a-zA-Z]{2,4}$'
        name_regex = '^[A-Z][a-z]{2,}$'
            
        is_valid = True
        if not re.match(name_regex, data['first_name']):
            flash("First name is not valid")
            is_valid = False
        if not re.match(name_regex, data['last_name']):
            flash("Last name is not valid")
            is_valid = False
        if not re.match(email_regex, data['email']):
            flash("Email is not valid")
            is_valid = False
        if len(data['dob']) == 0:
            flash("Must enter date of birth")
            is_valid = False
        if not 'os' in data:
            flash("Must choose an operating system")
            is_valid = False
        if data['location'] == 'No Choice':
            flash("Must choose a location")
            is_valid = False
        if not data['password'] == data['password2']:
            flash("Passwords don't match!")
            is_valid = False
        if re.search('[0-9]', data['password']) == None or re.search('[a-z]', data['password']) == None or re.search('[A-Z]', data['password']) == None or len(data['password']) < 6:
            flash("Password is not valid")
            is_valid = False             
        return is_valid
    