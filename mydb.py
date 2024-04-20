import mysql.connector

dataBase = mysql.connector.connect(
    host='localhost',
    user='root',
    password='S7+9X*af#LCx*-j'
)

# preparing a cursor object
cursorObject = dataBase.cursor()

# create database
cursorObject.execute("CREATE DATABASE elderco")

print("All done!")

