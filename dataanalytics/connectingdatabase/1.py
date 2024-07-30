import mysql.connector

# Connect to MySQL database
conn = mysql.connector.connect(
    host="localhost",
    user="username",
    password="password",
    database="database_name"
)

# Create a cursor object
cursor = conn.cursor()

# Execute SQL query
cursor.execute("SELECT * FROM table_name")

# Fetch all rows
rows = cursor.fetchall()

# Display the data
for row in rows:
    print(row)

# Close the cursor and connection
cursor.close()
conn.close()
