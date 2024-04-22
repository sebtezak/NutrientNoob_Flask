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

def get_account_info_from_id(user_id):
    # Connect to the SQLite database
    conn = sqlite3.connect('Databases/user.db')
    cursor = conn.cursor()

    try:
        # Retrieve user information from the database based on user_id
        cursor.execute("SELECT username, email, favorite_recipes, favorite_ingredients, dietary_restrictions, date_joined, profile_picture, favorite_food FROM user WHERE user_id=?", (user_id,))
        user_info = cursor.fetchone()

        if user_info:
            # Create a dictionary to store user account information
            account_info = {
                'username': user_info[0],
                'email': user_info[1],
                'favorite_recipes': user_info[2],
                'favorite_ingredients': user_info[3],
                'dietary_restrictions': user_info[4],
                'date_joined': user_info[5],
                'profile_picture': user_info[6],
                'favorite_food': user_info[7]
            }
            return account_info
        else:
            print("User not found.")
            return None

    except sqlite3.Error as e:
        print("Error retrieving user account information:", e)
        return None

    finally:
        # Close the database connection
        conn.close()


def favorite_recipe_from_name(recipe_info):
    user_id = recipe_info.get('userID')
    recipe_name = recipe_info.get('recipeName')

    if not user_id or not recipe_name:
        #print("Invalid input format. Please provide 'userID' and 'recipeName'.")
        return False

    try:
        # Connect to the SQLite database
        conn = sqlite3.connect('Databases/user.db')
        cursor = conn.cursor()

        # Retrieve user information from the database based on user_id
        cursor.execute("SELECT favorite_recipes FROM user WHERE user_id=?", (user_id,))
        user_info = cursor.fetchone()

        if user_info:
            favorite_recipes_str = user_info[0]
            # Split the favorite recipes string into a list
            favorite_recipes = favorite_recipes_str.split(',') if favorite_recipes_str else []

            # Check if the recipe is already in the favorites or if the favorites list is full
            if recipe_name in favorite_recipes or len(favorite_recipes) >= 10:
                return False  # Recipe already in favorites or favorites list full
            
            # Append the new recipe name to the existing list of favorite recipes
            favorite_recipes.append(recipe_name)
            # Join the list back into a string
            favorite_recipes_str = ','.join(favorite_recipes)
            
            # Update user's data in the database
            cursor.execute("UPDATE user SET favorite_recipes = ? WHERE user_id = ?", (favorite_recipes_str, user_id))
            conn.commit()
            
            return True  # Recipe successfully added to favorites
        else:
            print("User not found.")
            return False

    except sqlite3.Error as e:
        print("Error retrieving user account information:", e)
        return False

    finally:
        # Close the cursor and connection
        cursor.close()
        conn.close()
