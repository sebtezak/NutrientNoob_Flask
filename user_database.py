import sqlite3


#IMPORTANT: ***This file should only be run ONE time to initialize user database***


# Connect to SQLite database
conn = sqlite3.connect('Databases/user.db')
c = conn.cursor()

# Create table if not exists
c.execute('''CREATE TABLE IF NOT EXISTS user (
                username TEXT,
                user_id INTEGER PRIMARY KEY,
                email TEXT,
                password TEXT,
                favorite_recipes TEXT,
                favorite_ingredients TEXT,
                dietary_restrictions TEXT,
                date_joined TEXT,
                profile_picture TEXT,
                favorite_food TEXT
            )''')

# Sample user data
user_data = {
    'username': 'john_doe',
    'user_id': 1,
    'email': 'john@example.com',
    'password': 'hashed_password',  # Make sure to hash the password before storing
    'favorite_recipes': '',
    'favorite_ingredients': '',
    'dietary_restrictions': '',
    'date_joined': '2024-04-20 15:30:00',  # Example date
    'profile_picture': 'path_to_image',
    'favorite_food': 'pizza'
}

# Insert user data into the table
"""c.execute('''INSERT INTO user (username, user_id, email, password, favorite_recipes, favorite_ingredients,
             dietary_restrictions, date_joined, profile_picture, favorite_food)
             VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''', tuple(user_data.values()))"""

# Commit changes to the database
conn.commit()
conn.close()