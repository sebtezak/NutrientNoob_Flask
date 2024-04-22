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
    recipe_id = request.json.get('id', [])

    recipe_info = find_recipe_info(recipe_id)
    
    #print(recipe_info)

    return jsonify(recipe_info)

@app.route('/recipeinstructions')
def redirect_recipe_instructions():
    return render_template('recipeinstructions.html')

@app.route('/get_user_data', methods=['POST'])
def get_user_data():
    # Extract the ingredients from the request
    user_data = request.json.get('user_data', [])
    user_id = add_new_user(user_data)

    return jsonify(user_id)

@app.route('/usersetup')
def user_setup():
    return render_template('usersetup.html')

@app.route('/setup_user_profile', methods=['POST'])
def setup_user_profile():
    user_profile_data = request.json.get('userData', [])
    configure_user_profile(user_profile_data)

    return jsonify(user_profile_data)

@app.route('/get_login_data', methods=['POST'])
def get_login_data():
    login_data = request.json.get('login_data', [])
    valid_login = check_login(login_data)

    return jsonify(valid_login)

@app.route('/get_account_info', methods=['POST'])
def get_account_info():
    user_id = request.json.get('user_id', [])
    user_account_info = get_account_info_from_id(user_id)


    return jsonify(user_account_info)

@app.route('/favorite_recipe', methods=['POST'])
def favorite_recipe():
    favoriteRecipeInfo = request.json.get('favoriteRecipeInfo', [])
    print(favoriteRecipeInfo)
    recipe_favorite_success = favorite_recipe_from_name(favoriteRecipeInfo)

    return jsonify(recipe_favorite_success)

@app.route('/delete_user', methods=['POST'])
def delete_user():
    user_id = request.json.get('user_id', [])
    print(user_id)
    delete_user_successful = remove_user(user_id)

    return jsonify(delete_user_successful)

if __name__ == '__main__':
    app.run(debug=True)
