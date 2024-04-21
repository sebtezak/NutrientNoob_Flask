from flask import Flask, render_template, request, redirect, url_for, jsonify
from searchingNutrient import *
from searchingRecipe import *
from user_database_functions import *


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/account')
def account():
    return render_template('account.html')

@app.route('/recipes')
def recipes():
    return render_template('recipes.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/nutrition')
def nutrition():
    return render_template('nutrition.html')


@app.route('/backend/endpoint', methods=['POST'])
def nutrient_search():
    # Get the nutrients array from the request
    nutrients = request.json.get('nutrients', [])

    # Perform search operations using the received nutrients array
    # Here you can write the logic to search for ingredients based on the provided nutrients
    result_ingredients = format_nutrient_search(nutrients)

    # Return the search results as JSON
    return jsonify(result_ingredients)

@app.route('/nutrientsearch')
def redirect_nutrient_search():
    return render_template('nutrientsearch.html')

@app.route('/get_recipes', methods=['POST'])
def get_recipes():
    # Extract the ingredients from the request
    ingredients = request.json.get('ingredients', [])

    result_recipes = format_recipe_search(ingredients)

    return jsonify(result_recipes)

@app.route('/recipesearch')
def redirect_recipe_search():
    return render_template('recipesearch.html')

@app.route('/get_instructions', methods=['POST'])
def get_instructions():
    # Extract the ingredients from the request
    recipes = request.json.get('id', [])

    result_recipe_instructions = format_recipe_search(recipes)

    return jsonify(result_recipe_instructions)

@app.route('/recipeinstructions')
def redirect_recipe_instructions():
    return render_template('recipeinstructions.html')

<<<<<<< HEAD
@app.route('/get_user_data', methods=['POST'])
def get_user_data():
    # Extract the ingredients from the request
    user_data = request.json.get('user_data', [])
    user_id = add_new_user(user_data)
    print(user_id)

    return jsonify(user_id)

@app.route('/usersetup')
def user_setup():
    return render_template('usersetup.html')

@app.route('/setup_user_profile', methods=['POST'])
def setup_user_profile():
    user_profile_data = request.json.get('userData', [])
    configure_user_profile(user_profile_data)

    return jsonify(user_profile_data)


=======
>>>>>>> fa098ec9b5c4d234b5368a045d5754a350e9bf6a

if __name__ == '__main__':
    app.run(debug=True)
