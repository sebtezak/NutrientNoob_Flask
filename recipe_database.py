#if this import statement is not working, go to terminal and use command "pip install pysqlite3"
import sqlite3
import csv


# Connect to SQLite database
conn = sqlite3.connect('Databases/recipes.db')
c = conn.cursor()

# Create table
c.execute('''CREATE TABLE IF NOT EXISTS recipes (
                name TEXT,
                id INTEGER,
                minutes INTEGER,
                contributor_id INTEGER,
                submitted TEXT,
                tags TEXT,
                nutrition TEXT,
                n_steps INTEGER,
                steps TEXT,
                description TEXT,
                ingredients TEXT,
                n_ingredients INTEGER
            )''')

# Read data from CSV file and insert into table
with open('RAW_recipes.csv', newline='', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)
    next(reader)  # Skip header row
    for row in reader:
        c.execute('''INSERT INTO recipes (
                        name, id, minutes, contributor_id, submitted, tags, nutrition, n_steps, steps, description, ingredients, n_ingredients
                    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''', row)

# Commit changes and close connection
conn.commit()
conn.close()

'''print("Data from CSV file successfully inserted into SQLite database.")'''


"""TEST STATEMENTS
# Connect to SQLite database
conn = sqlite3.connect('Databases/recipes.db')
c = conn.cursor()

# Execute a SELECT query to retrieve data (limit to first 5 recipes)
c.execute('''SELECT * FROM recipes LIMIT 2''')

# Fetch all rows from the result set
rows = c.fetchall()

# Print the retrieved data
for row in rows:
    print(row)

# Close connection
conn.close() 
"""
