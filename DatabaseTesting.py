import mysql.connector
from mysql.connector import Error

def create_connection():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            database='arslan',  # Your database name
            user='root',  # XAMPP default user
            password=''  # No password for local environment
        )
        if connection.is_connected():
            print("Connected to MySQL database")
            return connection
    except Error as e:
        print(f"Error: '{e}'")
        return None

def insert_user(connection, name, email):
    try:
        cursor = connection.cursor()
        query = "INSERT INTO customers (name, email) VALUES (%s, %s)"
        cursor.execute(query, (name, email))
        connection.commit()
        print("User inserted successfully")
    except Error as e:
        print(f"Failed to insert into MySQL table: {e}")

def fetch_users(connection):
    try:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM customers")
        result = cursor.fetchall()
        for row in result:
            print(row)
    except Error as e:
        print(f"Failed to fetch records from MySQL table: {e}")

def update_user(connection, name, email, user_id):
    try:
        cursor = connection.cursor()
        query = "UPDATE customers SET name = %s, email = %s WHERE id = %s"
        cursor.execute(query, (name, email, user_id))
        connection.commit()
        print("User updated successfully")
    except Error as e:
        print(f"Failed to update record in MySQL table: {e}")

if __name__ == "__main__":
    # Create a database connection
    print("Before connection")
    connection = create_connection()
    if connection:
        print("Connection successful")

        # Insert a new user
        insert_user(connection, "John Doe", "john@example.com")
        print("Inserted a user")

        # Fetch and display all users
        print("Fetching all users:")
        fetch_users(connection)

        # Update a user
        print("Updating a user:")
        update_user(connection, "Jane D", "jane@example.com", 1)

        # Fetch and display all users after update
        fetch_users(connection)

        # Close the connection
        connection.close()
    else:
        print("Connection to DB failed")
