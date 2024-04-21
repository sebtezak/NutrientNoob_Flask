from flask import Flask, render_template, request, redirect, url_for, jsonify
from searchingNutrient import *
from searchingRecipe import *


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


if __name__ == '__main__':
    app.run(debug=True)
