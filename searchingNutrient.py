import csv
import os
import random

# Load all of the data into a valid list (More Efficient)
def load_and_filter_data(nutrient):
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
    print(f"No ingredients found containing {nutrient}.")