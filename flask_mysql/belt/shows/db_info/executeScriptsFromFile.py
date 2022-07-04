# a cursor is the object we use to interact with the database
import pymysql.cursors

# host = 'database-3.cv3bbotq8wvi.us-west-1.rds.amazonaws.com'
# host = 'aatygnn0kp0p44.c9hdwzzg0yse.us-west-2.rds.amazonaws.com'
host = 'localhost'
user = 'root'
password = 'root'
db = 'shows2_schema'
charset = 'utf8mb4'
cursorclass = pymysql.cursors.DictCursor
autocommit = True
filename = './erd/players_schema.sql'

 #db = db, charset = charset, cursorclass = cursorclass, autocommit = autocommit)

connection = pymysql.connect(host = host, user = user, password = password, autocommit = True)

#connection = pymysql.connect(host = host, user = user, password = password)
cursor = connection.cursor()

def executeScriptsFromFile(filename):
    # Open and read the file as a single buffer
    fd = open(filename, 'r')
    sqlFile = fd.read()
    fd.close()

    # all SQL commands (split on ';')
    sqlCommands = sqlFile.split(';')

    # Execute every command from the input file
    for command in sqlCommands:
        # This will skip and report errors
        # For example, if the tables do not yet exist, this will skip over
        # the DROP TABLE commands
        try:
            cursor.execute(command)
        except:
            print('Error executing: ', command)

executeScriptsFromFile(filename)

cursor.close()
connection.close()
