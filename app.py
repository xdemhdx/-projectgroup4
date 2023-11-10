from http import HTTPStatus
from flask import flash, request
import sys
from extensions import db
from flask import Flask, jsonify, redirect, render_template, url_for
from flask_migrate import Migrate
from flask_restful import Api
from models.Recipe import Recipe
from config import Config


def create_app():
    print("Hello", file=sys.stderr)
    app = Flask(__name__)
    app.config.from_object(Config)
    register_extensions(app)
    # register_resources(app)
    routes(app)

    return app


def register_extensions(app):
    db.init_app(app)
    migrate = Migrate(app, db)


# def register_resources(app):
#     api = Api(app)
def routes(app):
    @app.route('/')
    def home():
        # the below code is to insert the data uncomeent it then refresh the page as many times as you want so
        # the data is inserted then comment it back 
        # new_recipe_data = {
        # 'recipe_name': 'Chocolate Cake',
        # 'instructions': 'Mix ingredients and bake at 350 degrees for 35 minutes.',
        # 'preparation_time_minutes': 20,
        # 'cooking_time_minutes': 35,
        # 'servings': 8,
        # 'calories': 300,
        # 'category': 'Dessert',
        # 'ingredients': [
        #     {'name': 'Flour', 'amount': '2 cups'},
        #     {'name': 'Sugar', 'amount': '1 cup'},
        #     {'name': 'Cocoa Powder', 'amount': '1/2 cup'}]
        # }
        # new_recipe = Recipe(
        #     recipe_name=new_recipe_data['recipe_name'],
        #     instructions=new_recipe_data['instructions'],
        #     preparation_time_minutes=new_recipe_data['preparation_time_minutes'],
        #     cooking_time_minutes=new_recipe_data['cooking_time_minutes'],
        #     servings=new_recipe_data['servings'],
        #     calories=new_recipe_data['calories'],
        #     category=new_recipe_data['category'],
        #     ingredients=new_recipe_data['ingredients']  # Assuming ingredients is a JSON-compatible list
        #     )
        # new_recipe.save()
        return render_template('index.html')
    # guys this route will redirect the user to a page where it will show all the recipes in the database
    @app.route('/recipes')
    def all():
        all_recipes = Recipe.get_all()
        return render_template('allrecipes.html', recipes=all_recipes)
    # guys this route will return a recipe by id 
    @app.route('/search')
    def get_by_id():
        rid = request.args.get('search')
        if rid.isdigit():
            rid = int(rid)
            data = Recipe.get_by_id(rid)
            if data is None:
                return  {"Message":" recipe not found"}
            return render_template('search-recipe.html',recipes=data)
        return {"Message":"Entry type shoulb be integer or number"}
        # if type(rid) != int:
        #     return {"Message":"Error Id should be type of integer"}
        # return rid
    @app.route('/update-recipe',methods=["POST"])
    def update_recipe():
        recipe_id = request.form.get('id')
        recipe_name = request.form.get('recipe_name')
        instructions = request.form.get('instructions')
        data = {
        'recipe_name': recipe_name,
        'instructions': instructions
        }
        response, status = Recipe.update(recipe_id, data)
        if status == HTTPStatus.OK:
        # If update is successful
            return jsonify(response), status
        else:
        # If recipe is not found or any other error
            return jsonify({'message': 'Update failed'}), status

    @app.route("/<int:recipe_id>/delete")
    def delete_recipe(recipe_id):
        respones , status = Recipe.delete(recipe_id)
        return respones




if __name__ == '__main__':
    app = create_app()
    app.run('127.0.0.1', 5000)
