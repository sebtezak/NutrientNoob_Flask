import sqlite3
import os
import random

# Load all of the data into a valid list (More Efficient)
'''def load_and_filter_data(nutrient):
    csv_file_path='NutrientNoob/RAW_nutrition.csv'
    nutrient_key = nutrient.strip().lower()
    valid_ingredients = []

    with open(csv_file_path, 'r') as file:
        csv_reader = csv.DictReader(file)

        for row in csv_reader:
            row = {k.strip().lower(): v for k, v in row.items()}
            if nutrient_key in row and float(row[nutrient_key]) > 0:
                valid_ingredients.append(row["description"])

    return valid_ingredients

# Randomize from the possible list
def search_ingredients_by_nutrient(preloaded_data):
    return random.sample(preloaded_data, min(20, len(preloaded_data)))


# REPLACE WITH THE DROP DOWN VALUES!!! :)
nutrient = input("Enter a nutrient to search for: ")

# Gets list from function
matching_ingredients = search_ingredients_by_nutrient(load_and_filter_data(nutrient))

# REPLACE!!! Prints on terminal the list of 20 ingredients
if matching_ingredients:
    print(f"20 ingredients containing {nutrient}:")
    for ingredient in matching_ingredients:
        print(ingredient)
else:
    # This will be removed because of the drop down feature
    print(f"No ingredients found containing {nutrient}.")'''

def get_top_ingredients_by_nutrient(names, mins, maxs):
    # Connect to the SQLite database
    conn = sqlite3.connect('Databases/nutrition.db')
    cursor = conn.cursor()

    try:
        # Construct the WHERE clause for the SQL query based on the provided nutrient information
        conditions = []
        for name, min_value, max_value in zip(names, mins, maxs):
            condition = f"{name} >= {min_value}"
            conditions.append(condition)

        where_clause = " AND ".join(conditions)

        # Execute SQL query to retrieve top 20 ingredients with the specified nutrient conditions
        cursor.execute(f"SELECT Description FROM Nutrition WHERE {where_clause} ORDER BY {names[0]}")
        
        # Fetch the results
        top_ingredients = cursor.fetchall()

        return top_ingredients

    except sqlite3.Error as e:
        print("Error executing SQL query:", e)
        return None

    finally:
        # Close the database connection
        conn.close()

def format_ingredient_name(ingredient_name):
    # Split the ingredient name by commas
    split_names = []
    for item in ingredient_name:
        split_items = item.split(',')
        
        # Capitalize each word and strip extra whitespace
        capitalized_items = []
        for word in split_items:
            capitalized_word = word.strip().capitalize()
            capitalized_items.append(capitalized_word)
        
        # Join the capitalized words with commas and add to the list
        formatted_item = ', '.join(capitalized_items)
        split_names.append(formatted_item)
    
    # Join the formatted items with commas
    formatted_name = ', '.join(split_names)
    
    return formatted_name

def format_nutrient_search(array):
    names = []
    mins = []
    maxs = []
    if (len(array) == 0):
        return 0

    major_minerals = {"Calcium", "Copper", "Iron", "Magnesium", "Phosphorus", "Potassium", "Sodium", "Zinc"}
    vitamins = {"Vitamin"}

    for nutrient in array:
        name = nutrient['name'].replace(' ', '_')  # Replace spaces with underscores
        min_value = float(nutrient.get('min', 0) or 0)  # Convert min to float, default to 0 if empty
        max_value = float(nutrient.get('max', '99999') or '99999')  # Convert max to float, default to 99999 if empty

        # Adjust name based on nutrient type
        if name.split('_')[0] in major_minerals:
            name = "Major_Minerals_" + name
        elif any(vitamin in name for vitamin in vitamins):
            if name == "Vitamin_A":
                name = "Vitamins_Vitamin_A_RAE"  # Adjust column name for Vitamin A
            else:
                name = "Vitamins_" + name

        names.append(name)
        mins.append(min_value)
        maxs.append(max_value)
        

    search_result = get_top_ingredients_by_nutrient(names, mins, maxs)
    random.shuffle(search_result)
    formatted_search_result = [format_ingredient_name(item) for item in search_result]

    return formatted_search_result


