import sqlite3
import csv

# Define the column names and their corresponding data types
columns = [
    ("Category", "TEXT"),
    ("Description", "TEXT"),
    ("Nutrient_Data_Bank_Number", "INTEGER"),
    ("Alpha_Carotene", "REAL"),
    ("Ash", "REAL"),
    ("Beta_Carotene", "REAL"),
    ("Beta_Cryptoxanthin", "REAL"),
    ("Carbohydrate", "REAL"),
    ("Cholesterol", "REAL"),
    ("Choline", "REAL"),
    ("Fiber", "REAL"),
    ("Kilocalories", "REAL"),
    ("Lutein_and_Zeaxanthin", "REAL"),
    ("Lycopene", "REAL"),
    ("Manganese", "REAL"),
    ("Niacin", "REAL"),
    ("Pantothenic_Acid", "REAL"),
    ("Protein", "REAL"),
    ("Refuse_Percentage", "REAL"),
    ("Retinol", "REAL"),
    ("Riboflavin", "REAL"),
    ("Selenium", "REAL"),
    ("Sugar_Total", "REAL"),
    ("Thiamin", "REAL"),
    ("Water", "REAL"),
    ("Fat_Monosaturated_Fat", "REAL"),
    ("Fat_Polysaturated_Fat", "REAL"),
    ("Fat_Saturated_Fat", "REAL"),
    ("Fat_Total_Lipid", "REAL"),
    ("Household_Weights_1st_Household_Weight", "REAL"),
    ("Household_Weights_1st_Household_Weight_Description", "TEXT"),
    ("Household_Weights_2nd_Household_Weight", "REAL"),
    ("Household_Weights_2nd_Household_Weight_Description", "TEXT"),
    ("Major_Minerals_Calcium", "REAL"),
    ("Major_Minerals_Copper", "REAL"),
    ("Major_Minerals_Iron", "REAL"),
    ("Major_Minerals_Magnesium", "REAL"),
    ("Major_Minerals_Phosphorus", "REAL"),
    ("Major_Minerals_Potassium", "REAL"),
    ("Major_Minerals_Sodium", "REAL"),
    ("Major_Minerals_Zinc", "REAL"),
    ("Vitamins_Vitamin_A_IU", "REAL"),
    ("Vitamins_Vitamin_A_RAE", "REAL"),
    ("Vitamins_Vitamin_B12", "REAL"),
    ("Vitamins_Vitamin_B6", "REAL"),
    ("Vitamins_Vitamin_C", "REAL"),
    ("Vitamins_Vitamin_E", "REAL"),
    ("Vitamins_Vitamin_K", "REAL")
]

# Function to create the SQLite database and table
def create_database_table():
    conn = sqlite3.connect("NutrientNoob_Flask/Databases/nutrition.db")
    c = conn.cursor()

    # Create table
    c.execute("DROP TABLE IF EXISTS nutrition")  # Drop the table if it already exists
    c.execute("CREATE TABLE nutrition ({})".format(", ".join(["{} {}".format(col[0], col[1]) for col in columns])))

    conn.commit()
    conn.close()

# Function to insert data from the CSV file into the SQLite table
def insert_data_from_csv():
    conn = sqlite3.connect("NutrientNoob_Flask/Databases/nutrition.db")
    c = conn.cursor()

    with open("NutrientNoob_Flask/RAW_nutrition.csv", "r") as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader)  # Skip the header row
        for row in csv_reader:
            c.execute("INSERT INTO nutrition VALUES ({})".format(", ".join(["?" for _ in range(len(columns))])), row)

    conn.commit()
    conn.close()

# Debug function to output nutrition data for the first 5 rows
def debug_output():
    conn = sqlite3.connect("NutrientNoob_Flask/Databases/nutrition.db")
    c = conn.cursor()

    # Get user input for ingredient search
    ingredient = input("Enter the ingredient you want to search for: ").strip().lower()

    # Search for the ingredient in the database
    c.execute("SELECT * FROM nutrition WHERE LOWER(Description) LIKE ?", ('%' + ingredient + '%',))
    rows = c.fetchall()

    if rows:
        print("Nutrition data for '{}' found in the database:".format(ingredient))
        for row in rows:
            print(row)
    else:
        print("No nutrition data found for '{}' in the database.".format(ingredient))

    conn.close()

# Create the database and table
create_database_table()

# Insert data from the CSV file
insert_data_from_csv()

# Verify that the database was created properly
conn = sqlite3.connect("NutrientNoob_Flask/Databases/nutrition.db")
c = conn.cursor()
c.execute("SELECT COUNT(*) FROM nutrition")
print("Total rows in the 'nutrition' table:", c.fetchone()[0])
conn.close()

# Debug output
debug_output()
