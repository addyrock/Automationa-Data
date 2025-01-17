import pymysql

# Database connection details
DB_HOST = 'localhost'
DB_USER = 'root'  # Default username for phpMyAdmin
DB_PASSWORD = ''  # Leave blank if no password is set
DB_NAME = 'blood donor'  # Your database name

try:
    # Connect to the database
    connection = pymysql.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_NAME
    )

    print("Connected to the database successfully!")

    # Create a cursor object
    cursor = connection.cursor()
    select_query= ("SELECT * FROM users;")
    cursor.execute(select_query)
    # Write and execute your SELECT query
    update_query = ("UPDATE users SET age = 12 WHERE id = 1;")
    cursor.execute(update_query)

    query_insert = "INSERT INTO users (id, age) VALUES (2, 12);"
    cursor.execute(query_insert)
    connection.commit()


    # Fetch and print the results
    results = cursor.fetchall()
    for row in results:
        print(row)

except pymysql.MySQLError as e:
    print(f"Error connecting to database: {e}")

finally:
    # Close the connection
    if 'connection' in locals() and connection.open:
        connection.close()
        print("Database connection closed.")
