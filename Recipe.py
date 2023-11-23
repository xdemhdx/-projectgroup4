from extensions import db
from http import HTTPStatus
import json


# this class File has to methods one for read the file and one for write the file for a json format
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
            try:
                file_pointer.write(data)
                return True
            except:
                return False
#class Recipe 
class Recipe():
    def __init__(self, recipe_name, instruction, preparation_time_minutes, cooking_time_minutes, servings, calories, category):
        self.recipe_name = recipe_name
        self.instruction = instruction
        self.preparation_time_minutes = preparation_time_minutes
        self.cooking_time_minutes = cooking_time_minutes
        self.servings = servings
        self.calories = calories
        self.category = category
    # this method will fetch the object of Recipe class
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
    # this method all revice a data and check for any illegal values if no illegal values encounterd then it will create an object of Recipe and add it to a file by calling a File.save method
    @classmethod 
    def add(cls, r_data):
        # Validation checks for illegal values | it returns boolean good for testing
        if not r_data.get('recipe_name'):
            raise ValueError('Error loading the recipe (name)')

        if not r_data.get('instruction'):
            raise ValueError('Error loading the recipe (instruction)')

        if not r_data.get('preparation_time_minutes') or not r_data['preparation_time_minutes'].isdigit() or int(r_data['preparation_time_minutes']) < 0:
            raise ValueError('Error loading the recipe (prep time)')

        if not r_data.get('cooking_time_minutes') or not r_data['cooking_time_minutes'].isdigit() or int(r_data['cooking_time_minutes']) < 0:
            raise ValueError('Error loading the recipe (cook time)')

        if not r_data.get('servings') or not r_data['servings'].isdigit() or int(r_data['servings']) <= 0:
            raise ValueError('Error loading the recipe (servings)')

        if not r_data.get('calories') or not r_data['calories'].isdigit() or int(r_data['calories']) <= 0:
            raise ValueError('Error loading the recipe (calories)')

        if not r_data.get('category'):
            raise ValueError('Error loading the recipe (category)')
        new_recipe = cls(
        r_data['recipe_name'],
        r_data['instruction'],
        r_data['preparation_time_minutes'],
        r_data['cooking_time_minutes'],
        r_data['servings'],
        r_data['calories'],
        r_data['category'])
        # Save new recipe
        all_data = cls.get_all()[1]
        length = all_data.get('recipes', [])
        new_recipe.id = length[-1]['id'] + 1 if length else 1
        # Convert recipe object to dictionary and add to all_data
        recipe_dict = vars(new_recipe)
        all_data.get('recipes').append(recipe_dict)
        return File.save_file(all_data)
    # this method will retive all the recipes in the json file
    @classmethod
    def get_all(self):
        file = File.import_file()
        if file[0]:
            return [True,file[1]]
        else:
            return [False]
    # this method will retive all a specific recipe by id 
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
    # this method will update a recipe  including a validation checks
    @classmethod
    def update(self,id, data):
        all_data = Recipe.get_all()
        for recipe in all_data[1]['recipes']:
            if recipe.get('id') == id:

                if 'recipe_name' in data:
                    if data['recipe_name']:
                        recipe['recipe_name'] = data['recipe_name']
                    else:
                        raise ValueError('Error updating the recipe (name)')


                if 'instruction' in data:
                    if data['instruction']:
                        recipe['instruction'] = data['instruction']
                    else:
                        raise ValueError('Error updating the recipe (instruction)')


                if 'preparation_time_minutes' in data:
                    ptm = data['preparation_time_minutes']
                    if ptm.isdigit() and int(ptm) >= 0:
                        recipe['preparation_time_minutes'] = ptm
                    else:
                        raise ValueError('Error updating the recipe (preparation time)')


                if 'cooking_time_minutes' in data:
                    ctm = data['cooking_time_minutes']
                    if ctm.isdigit() and int(ctm) >= 0:
                        recipe['cooking_time_minutes'] = ctm
                    else:
                        raise ValueError('Error updating the recipe (cooking time)')


                if 'servings' in data:
                    srv = data['servings']
                    if srv.isdigit() and int(srv) > 0:
                        recipe['servings'] = srv
                    else:
                        raise ValueError('Error updating the recipe (servings)')


                if 'calories' in data:
                    cal = data['calories']
                    if cal.isdigit() and int(cal) > 0:
                        recipe['calories'] = cal
                    else:
                        raise ValueError('Error updating the recipe (calories)')


                if 'category' in data and data['category']:
                    recipe['category'] = data['category']
                else:
                    raise ValueError('Error updating the recipe (category)')

                File.save_file(all_data[1])
                return True

        # if no recipe with  given ID is found :)
        return False
    # this method will delete a specific recipe with a given id if it exist it will return true after deleting it 
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

    
        
