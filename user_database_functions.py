import sqlite3
from datetime import datetime

def remove_user(user_id):
    # Connect to the SQLite database
    conn = sqlite3.connect('Databases/user.db')
    c = conn.cursor()

    try:
        # Execute the DELETE SQL statement
        c.execute("DELETE FROM user WHERE user_id = ?", (user_id,))
        print("User removed successfully.")

        # Commit the transaction
        conn.commit()

    except sqlite3.Error as e:
        print("Error removing user:", e)

    finally:
        # Close the database connection
        conn.close()

def add_new_user(user_data):
    # Connect to SQLite database
    conn = sqlite3.connect('Databases/user.db')
    c = conn.cursor()

    try:
        # Check if username or email already exists
        c.execute("SELECT COUNT(*) FROM user WHERE username=? OR email=?", (user_data['username'], user_data['email']))
        count = c.fetchone()[0]
        if count > 0:
            print("Username or email already exists")
            return 0

        # Insert user data into the table
        user_data['date_joined'] = datetime.now().strftime('%Y-%m-%d')
        c.execute('''INSERT INTO user (username, email, password, favorite_recipes,
                     favorite_ingredients, dietary_restrictions, date_joined,
                     profile_picture, favorite_food)
                     VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)''',
                  (user_data['username'], user_data['email'], user_data['password'],
                   '', '', '', user_data['date_joined'], '', ''))

        # Retrieve the user_id of the inserted user
        c.execute("SELECT user_id FROM user WHERE username=?", (user_data['username'],))
        user_id = c.fetchone()[0]
        print("User added successfully with user_id:", user_id)
        return user_id

    except sqlite3.Error as e:
        print("Error:", e)
        return 0

    finally:
        # Commit changes and close the connection
        conn.commit()
        conn.close()


def configure_user_profile(user_data):
    # Extract user data from the dictionary
    dietary_restrictions = user_data.get('dietary_restrictions', '')
    favorite_food = user_data.get('favorite_food', '')
    user_id = user_data.get('user_id')

    # Connect to the SQLite database
    conn = sqlite3.connect('Databases/user.db')
    cursor = conn.cursor()

    try:
        # Update the user's profile in the database
        cursor.execute('''UPDATE user SET dietary_restrictions = ?, favorite_food = ? WHERE user_id = ?''',
                       (dietary_restrictions, favorite_food, user_id))
        
        # Commit the changes
        conn.commit()
        print("User profile updated successfully.")

    except sqlite3.Error as e:
        print("Error updating user profile:", e)

    finally:
        # Close the database connection
        conn.close()


def check_login(login_data):
    # Connect to the user database
    conn = sqlite3.connect('Databases/user.db')
    c = conn.cursor()

    # Extract username and password from login_data
    username = login_data.get('username')
    password = login_data.get('password')

    # Query the database to check if the credentials are valid
    c.execute("SELECT user_id FROM user WHERE username = ? AND password = ?", (username, password))
    user_id = c.fetchone()

    # Close the database connection
    conn.close()

    # Return the user_id if credentials are valid, otherwise return 0
    return user_id[0] if user_id else 0