import mysql.connector

# connecting database server.
database = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd=''
)

# cursor object.
cursor_obj = database.cursor()

# creating database
cursor_obj.execute('CREATE DATABASE crm_db;')
print("Database creation completed.")



