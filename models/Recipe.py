from extensions import db
from http import HTTPStatus
import json

class File():
    @classmethod
    def import_file(cls,filepath="models/data.json"):
        try:
            with open(filepath,"r") as file_pointer:
                data = json.load(file_pointer)
                return [True,data]
        except FileNotFoundError:
            print(f"The file {filepath} not found")
            return [False]
        except json.JSONDecodeError:
            print(f"The file {filepath} contains not valid JSON Structure")
            return False 
    def save_file(r_data,filepath="models/data.json"):
        file = File.import_file()
        data = file[1]
        data['recipes'].append(r_data)
        data = json.dumps(data,indent=4)
        with open(filepath,"w") as file_pointer:
            file_pointer.write(data)
class Recipe(db.Model):
    __tablename__ = 'recipe'
    id = db.Column(db.Integer, primary_key=True)
    recipe_name = db.Column(db.String(100), nullable=False)
    instructions = db.Column(db.String(1000))  # Adjust size as needed
    preparation_time_minutes = db.Column(db.Integer)
    cooking_time_minutes = db.Column(db.Integer)
    servings = db.Column(db.Integer)
    calories = db.Column(db.Integer)
    category = db.Column(db.String(50))
    ingredients = db.Column(db.JSON)  # Storing ingredients as a JSON field
    @property
    def data(self):
        return {
            'id': self.id,
            'recipe_name': self.recipe_name,
            'ingredients': self.ingredients,  # Directly return the JSON field
            'instructions': self.instructions,
            'preparation_time_minutes': self.preparation_time_minutes,
            'cooking_time_minutes': self.cooking_time_minutes,
            'servings': self.servings,
            'calories': self.calories,
            'category': self.category
        }
    def save(self):
        db.session.add(self)
        db.session.commit()
    @classmethod
    def get_all(cls):
        result = cls.query.all()
        return [recipe.data for recipe in result]
    @classmethod
    def get_by_id(cls,id):
        result = cls.query.filter(cls.id == id).first()
        return result.data if result else None
            

        #return cls.query.filter(cls.id==id).first() later will use it when implementing the controller to fetch the data
    @classmethod
    def update(cls, id, data):
        recipe = cls.query.filter_by(id=id).first()
        if not recipe:
            return {'message': 'Recipe not found'}, HTTPStatus.NOT_FOUND
        recipe.recipe_name = data.get('recipe_name', recipe.recipe_name)
        recipe.instructions = data.get('instructions', recipe.instructions)
        recipe.preparation_time_minutes = data.get('preparation_time_minutes',recipe.preparation_time_minutes)
        recipe.cooking_time_minutes = data.get('cooking_time_minutes',recipe.cooking_time_minutes)
        recipe.servings = data.get('servings',recipe.servings)
        recipe.calories = data.get('calories',recipe.calories)
        recipe.category = data.get('category',recipe.category)
        db.session.commit()
        return recipe.data, HTTPStatus.OK
    @classmethod
    def delete(cls,id):
        recipe = cls.query.filter(cls.id == id).first()
        if recipe is None:
            return {'message': 'recipe not found'}, HTTPStatus.NOT_FOUND
        db.session.delete(recipe)
        db.session.commit()
        return {}, HTTPStatus.NO_CONTENT

    
        
