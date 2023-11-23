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
        data = json.dumps(r_data,indent=4)
        with open(filepath,"w") as file_pointer:
            file_pointer.write(data)
class Recipe():

    def __init__(self,recipe_name , instruction,preparation_time_minutes,cooking_time_minutes,servings,calories,category):
        all_data = Recipe.get_all()
        length = Recipe.get_all().get('recipes')
        if(len(length)==0):
            length =0
        else:
            length = length[-1]['id']
        self.id = length+1
        self.recipe_name = recipe_name
        self.instruction = instruction
        self.preparation_time_minutes = preparation_time_minutes
        self.cooking_time_minutes = cooking_time_minutes
        self.servings = servings
        self.calories = calories
        self.category = category
        all_data.get('recipes').append(self.data)
        File.save_file(all_data)
    @property
    def data(self):
        return {
            'id': self.id,
            'recipe_name': self.recipe_name,
            'instruction': self.instruction,
            'preparation_time_minutes': self.preparation_time_minutes,
            'cooking_time_minutes': self.cooking_time_minutes,
            'servings': self.servings,
            'calories': self.calories,
            'category': self.category
        }
    @classmethod 
    def add(self,r_data):
        Recipe(r_data['recipe_name'],r_data['instruction'],r_data['preparation_time_minutes'],r_data['cooking_time_minutes'],r_data['servings'],r_data['calories'],r_data['category'])
    @classmethod
    def get_all(self):
        file = File.import_file()
        data = file[1]
        return data
    @classmethod
    def get_by_id(self,r_id=0):
        
        file = File.import_file()
        result = {}
        if(file[0]):
            data= file[1].get('recipes')
            for i in data:
                if(i.get('id')==r_id):
                    result = i
        if(len(result)>0):
            return result
        return [False]
        #return cls.query.filter(cls.id==id).first() later will use it when implementing the controller to fetch the data
    @classmethod
    def update(cls, id, data):
        all = Recipe.get_by_id(id)
        print(all)
        
        # recipe = cls.query.filter_by(id=id).first()
        # if not recipe:
        #     return {'message': 'Recipe not found'}, HTTPStatus.NOT_FOUND
        # recipe.recipe_name = data.get('recipe_name', recipe.recipe_name)
        # recipe.instructions = data.get('instructions', recipe.instructions)
        # recipe.preparation_time_minutes = data.get('preparation_time_minutes',recipe.preparation_time_minutes)
        # recipe.cooking_time_minutes = data.get('cooking_time_minutes',recipe.cooking_time_minutes)
        # recipe.servings = data.get('servings',recipe.servings)
        # recipe.calories = data.get('calories',recipe.calories)
        # recipe.category = data.get('category',recipe.category)
        # db.session.commit()
        # return recipe.data, HTTPStatus.OK
    @classmethod
    def delete(cls,id):
        flag = False
        data = Recipe.get_all()
        for i in data.get('recipes'):
            if(i.get('id')==id):
                data.get('recipes').remove(i)
                flag = True
                break
        if(not flag):
            return False
        File.save_file(data)
        return True

    
        
