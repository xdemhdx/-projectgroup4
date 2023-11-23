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

    def __init__(self,recipe_name=None,instruction=None,preparation_time_minutes=None,cooking_time_minutes=None,servings=None,calories=None,category=None):
        all_data = Recipe.get_all()[1]
        length = Recipe.get_all()[1].get('recipes')
        if(len(length)==0):
            length =0
        else:
            length = length[-1]['id']
        self.id = length+1
        if recipe_name :
            self.recipe_name = recipe_name
        else:
            raise 'error loading the recipe(name)'
        if instruction :
            self.instruction = instruction
        else:
            raise 'error loading the recipe(instruction)'
        if preparation_time_minutes and preparation_time_minutes.isdigit() and int(preparation_time_minutes)>=0:
            self.preparation_time_minutes=preparation_time_minutes
        else:
            raise 'error loading the recipe(prep)'
        if cooking_time_minutes and cooking_time_minutes.isdigit() and int(cooking_time_minutes)>=0:
            self.cooking_time_minutes = cooking_time_minutes
        else:
            raise 'error loading the recipe(cook)'
        if  servings and servings.isdigit() and int(servings)>=0:
            self.servings = servings
        else:
            raise 'error loading the recipe(servings)'
        if  calories and calories.isdigit() and int(calories)>0:
            self.calories = calories
        else:
            raise 'error loading the recipe(calories)'
        if  category :
            self.category= category
        else:
            raise 'error loading the recipe(category)'
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
        if file[0]:
            return [True,file[1]]
        else:
            return [False]
    @classmethod
    def get_by_id(self,r_id=0):
        file = Recipe.get_all()
        result = {}
        if(file[0]):
            data= file[1].get('recipes')
            for i in data:
                if(i.get('id')==r_id):
                    result = i
            if(len(result)>0):
                return [True,result]
        return [False]
        
    @classmethod
    def update(self, id, data):
        all_data = Recipe.get_all()
        for i in all_data[1].get('recipes'):
            if(i.get('id')==id):
                i['recipe_name']= data['recipe_name']
                i['instruction']= data['instruction']
                i['preparation_time_minutes']= data['preparation_time_minutes']
                i['cooking_time_minutes']= data['cooking_time_minutes']
                i['servings']= data['servings']
                i['calories']= data['calories']
                i['category']= data['category']
        File.save_file(all_data[1])
    @classmethod
    def delete(self,id):
        flag = False
        data = Recipe.get_all()
        if data[0]:
            for i in data[1].get('recipes'):
                if(i.get('id')==id):
                    data[1].get('recipes').remove(i)
                    flag = True
                    break
            if(not flag):
                return False
            File.save_file(data[1])
            return True
        else:
            return False

    
        
