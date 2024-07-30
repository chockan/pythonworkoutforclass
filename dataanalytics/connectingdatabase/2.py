import sqlite3

# Connect to SQLite database
conn = sqlite3.connect('database.db')

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
