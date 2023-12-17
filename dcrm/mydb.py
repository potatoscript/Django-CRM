import mysql.connector

database = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='root'
)

# prepare a cursor object
currorObject = database.cursor()

# Create a database
currorObject.execute("CREATE DATABASE office")

print("All Done!")
