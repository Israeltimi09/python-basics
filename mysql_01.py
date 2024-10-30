import mysql.connector

connection = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "classicmodels"
)
if(connection.is_connected()):
    print("Connected to MYSQL database")
else:
    print("DB is not connected")