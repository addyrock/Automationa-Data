import mysql.connector
from mysql.connector import Error

def create_connection():
    try:
        print("Inside the create_connection function")
        connection = mysql.connector.connect(
            host='localhost',           # Change host to 'localhost'
            database='arslan',           # Use your actual database name
            user='root',                 # XAMPP default user
            password=''                  # Leave empty for no password
        )

        if connection.is_connected():
            print("Connected to MySQL database")
            return connection
    except Error as e:
        print(f"Error: {e}")
        return None

connection = create_connection()
if connection:
    print("Connection successful")
else:
    print("Connection failed")
