# a cursor is the object we use to interact with the database
import pymysql.cursors

host = 'localhost'
user = 'root'
password = 'root'

filename = './erd/players_schema.sql'

connection = pymysql.connect(host = host, user = user, password = password, autocommit = True)
cursor = connection.cursor()

def executeScriptsFromFile(filename):
    # Open and read the file as a single buffer
    fd = open(filename, 'r')
    sqlFile = fd.read()
    fd.close()

    # all SQL commands (split on ';')
    sqlCommands = sqlFile.strip().split(';')

    # Execute every command from the input file
    for command in sqlCommands:
        # This will skip and report errors
        # For example, if the tables do not yet exist, this will skip over
        # the DROP TABLE commands
        try:
            if (len(command) > 0):
                cursor.execute(command)
        except:
            print('Error executing: ', command)

executeScriptsFromFile(filename)

cursor.close()
connection.close()
