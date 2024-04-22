import sqlite3
import random


def get_top_recipes(array):
    # Connect to the SQLite database
    conn = sqlite3.connect('Databases/recipes.db')
    cursor = conn.cursor()

    try:
        # Construct the WHERE clause for the SQL query based on the provided ingredients
        conditions = []
        for ingredient in array:
            condition = f"Ingredients LIKE '%{ingredient}%'"
            conditions.append(condition)

        where_clause = " AND ".join(conditions)

        # Execute SQL query to retrieve top 20 recipes matching the ingredients
        cursor.execute(f"SELECT name, id FROM Recipes WHERE {where_clause} ORDER BY Description LIMIT 2000")
        
        # Fetch the results
        top_recipes = cursor.fetchall()

        return top_recipes

    except sqlite3.Error as e:
        print("Error executing SQL query:", e)
        return None

    finally:
        # Close the database connection
        conn.close()

def format_recipe_search(array):
    
    result = []

    for key, value in array.items():
        if value:  
            result.append(value)

    result_recipes = get_top_recipes(result)
    
    random.shuffle(result_recipes)
    return result_recipes


def find_recipe_info(recipe_id):
    # Connect to the SQLite database
    conn = sqlite3.connect('Databases/recipes.db')
    cursor = conn.cursor()

    # Fetch recipe information from the database
    cursor.execute("SELECT name, minutes, tags, nutrition, steps, description, ingredients FROM recipes WHERE id=?", (recipe_id,))
    recipe_data = cursor.fetchone()

    # Close the connection
    conn.close()

    if recipe_data:

        # Create a dictionary to store recipe information
        recipe_info = {
            'name': recipe_data[0],
            'minutes': recipe_data[1],
            'tags': recipe_data[2],
            'nutrition': recipe_data[3],
            'steps': recipe_data[4],
            'description': recipe_data[5],
            'ingredients': recipe_data[6]
        }
        return recipe_info
    else:
        return None



    