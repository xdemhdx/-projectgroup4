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
    routes(app)
    return app

def register_extensions(app):
    db.init_app(app)
    migrate = Migrate(app, db)

def routes(app):
    @app.route('/')
    def home():
        return render_template('index.html')
    # guys this route will redirect the user to a page where it will show all the recipes in the database
    @app.route('/add')
    def add():
        return render_template("addmenu.html")
    @app.route("/add-recipe",methods=["POST"])
    def addrecipe():
        recipe_name = request.form.get('recipe_name')
        instruction = request.form.get('instruction')
        preparation_time = request.form.get('preparation_time')
        cooking_time = request.form.get('cooking_time')
        servings = request.form.get('servings')
        calories = request.form.get('calories')
        category = request.form.get('category')
        data = {
            "recipe_name":recipe_name,
            "instruction": instruction,
            "preparation_time_minutes":preparation_time,
            "cooking_time_minutes": cooking_time,
            "servings": servings,
            "calories":calories,
            "category":category
        }
        result = Recipe.add(data)
        if(result):
            return {"Suceeess":"Imported"}
        return {"Error":"Unable to import"}


    @app.route('/recipes')
    def all():
        all_recipes = Recipe.get_all()[1].get('recipes')
        return render_template('allrecipes.html', recipes=all_recipes)
    # guys this route will return a recipe by id 
    @app.route('/search',methods=["GET"])
    def get_by_id():
        rid = request.args.get('id')
        if rid.isdigit():
            rid = int(rid)
            data = Recipe.get_by_id(rid)
            if not data[0]:
                return  {"Message":" recipe not found"}
            return render_template('search-recipe.html',recipes=data[1])
        return {"Message":"Entry type shoulb be integer or number"}
    @app.route('/update-recipe',methods=["POST"])
    def update_recipe():
        recipe_id = int(request.form.get('id'))
        recipe_name = request.form.get('recipe_name')
        instruction = request.form.get('instruction')
        preparation_time_minutes = request.form.get('preparation_time_minutes')
        cooking_time_minutes = request.form.get('cooking_time_minutes')
        servings = request.form.get('servings')
        calories = request.form.get('calories')
        category = request.form.get('category')
        data = {
        'recipe_name': recipe_name,
        'instruction': instruction,
        'preparation_time_minutes':preparation_time_minutes,
        'cooking_time_minutes':cooking_time_minutes,
        'servings': servings,
        'calories': calories,
        'category': category
        }
        Recipe.update(recipe_id,data)
        data = Recipe.get_by_id(recipe_id)[1]
        return render_template('search-recipe.html',recipes=data)

    @app.route("/<int:recipe_id>/delete")
    def delete_recipe(recipe_id):
        result = Recipe.delete(recipe_id)
        if(result):
            return {"Message":"Delete Successful"}
        return {"Message":"Delete UnSuccessful Or ID does not exist!"}
        
        




if __name__ == '__main__':
    app = create_app()
    app.run('127.0.0.1', 5000)
