import mysql.connector

username = input("Enter DB username:")
passwd = input("Enter DB password:")
# connecting database server.
database = mysql.connector.connect(
    host='localhost',
    user=username,
    passwd=passwd
)

# cursor object.
cursor_obj = database.cursor()

# creating database
cursor_obj.execute('CREATE DATABASE crm_db;')
print("Database creation completed.")



