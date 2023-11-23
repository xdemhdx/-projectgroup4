import json


class Recipe():
    def __init__(self,id=None,name=None,steps=None,prep_time=None,cook_time=None,serving=None,calory=None,category=None):
        if  id and id.isdigit() and int(id)>0:
            self.id = id
        else:
            raise 'error loading the recipe(id)'
        if name :
            self.name = name
        else:
            raise 'error loading the recipe(name)'
        if steps :
            self.steps = steps
        else:
            raise 'error loading the recipe(steps)'
        if prep_time and prep_time.isdigit() and int(prep_time)>=0:
            self.prep_time=prep_time
        else:
            raise 'error loading the recipe(prep)'
        if cook_time and cook_time.isdigit() and int(cook_time)>=0:
            self.cook_time = cook_time
        else:
            raise 'error loading the recipe(cook)'
        if  serving and serving.isdigit() and int(serving)>=0:
            self.serving = serving
        else:
            raise 'error loading the recipe(serving)'
        if  calory and calory.isdigit() and int(calory)>0:
            self.calory = calory
        else:
            raise 'error loading the recipe(calory)'
        if  category :
            self.category= category
        else:
            raise 'error loading the recipe(category)'



class manage_recipe():
    def __init__(self,recipes=None):
        pass
    @classmethod
    def import_file(self,filepath="models/data.json"):
        try:
            with open(filepath,"r") as file_pointer:
                data =json.load(file_pointer)
            recipes=[]
            for i in data['recipes']:
                recipe_class= Recipe(i['id'],i['recipe name'],i['instructions'],i['preparation time (minutes)'],i['cooking time (minutes)'],i['servings'],i['calories'],i['category'])
                recipes.append(recipe_class)
            return [True,recipes]
        except FileNotFoundError:
            print(f"The file {filepath} not found")
            return [False]
        except json.JSONDecodeError:
            print(f"The file {filepath} contains not valid JSON Structure")
            return [False]
    @classmethod
    def get_all(self):
        status=manage_recipe.import_file()
        if status[0]:
            return [True,status[1]]
        else:
            return [False]
    @classmethod
    def save(self,r_data=None,filepath="models/data.json"):
        if r_data:
            file = manage_recipe.import_file()
            #dict_data= {'id':r_data.id,'recipe name':r_data.name,''}
            data = file[1]
            data['recipes'].append(r_data)
            data = json.dumps(data,indent=4)
            with open(filepath,"w") as file_pointer:
                file_pointer.write(data)
        else:
            return [False]
    @classmethod
    def get_by_id(self,id=0):
        status = manage_recipe.get_all()
        if status:
            for i in status:
                if (i['id']==id):
                    return i
        return [False]
    @classmethod
    def delete(self,id=0):
        status = manage_recipe.get_all()
        



            