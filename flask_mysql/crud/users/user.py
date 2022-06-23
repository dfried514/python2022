# import the function that will return an instance of a connection
from mysqlconnection import connectToMySQL
# model the class after the user table from our database
class User:
    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    # Now we use class methods to query our database
    @classmethod
    def get_all_users(cls):
        query = "SELECT * FROM users;"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL('users_schema').query_db(query)
        # Create an empty list to append our instances of users
        users = []
        # Iterate over the db results and create instances of users with cls.
        for user in results:
            users.append( cls(user) )
        return users
    @classmethod
    def get_user(cls, id):
        query = "SELECT * FROM users WHERE id=%d;" % (id)
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL('users_schema').query_db(query)
        # return instance of User 
        return cls(results[0])
    # class method to save our user to the database
    @classmethod
    def insert_new_user(cls, data ):
        query = "INSERT INTO users ( first_name , last_name , email , created_at, updated_at ) VALUES ( %(fname)s , %(lname)s , %(email)s , NOW() , NOW() );"
        # data is a dictionary that will be passed into the save method from server.py
        return connectToMySQL('users_schema').query_db( query, data )
    # class method to update our user in the database
    @classmethod
    def update_user(cls, data ):
        query = "UPDATE users SET first_name=%(fname)s, last_name=%(lname)s, email=%(email)s, updated_at=NOW() WHERE id=%(id)s;"
        # data is a dictionary that will be passed into the update method from server.py
        connectToMySQL('users_schema').query_db( query, data )
    # class method to delete our user in the database
    @classmethod
    def delete_user(cls, data ):
        query = "DELETE FROM users WHERE id=%(id)s;"
        # data is a dictionary that will be passed into the delete method from server.py
        connectToMySQL('users_schema').query_db( query, data )
