import unittest
import Recipe
#import datalayer
#IMPORTANT MAKE SURE TO RESET THE JSON TO HAVE ONLY 2 RECIPES FOR THIS TEST
class IntegrationTestsMenuManagement(unittest.TestCase):
    def test_add_method(self):
        recipe1={"id":"1","recipe_name":"food","instruction":"burn it","preparation_time_minutes":"-600","cooking_time_minutes":"-200","servings":20,"calories":"0","category":"burnt food"}
        try:
            Recipe.Recipe.add(recipe1)
            flag=False
        except:
            flag=True
        self.assertTrue(flag)
    
    def test_delete_method(self):
        recipe1={"recipe_name":"Frozen pizza","instruction":"microwave it","preparation_time_minutes":"20","cooking_time_minutes":"60","servings":"4","calories":"3","category":"frozen food"}
        Recipe.Recipe.add(recipe1)
        self.assertTrue(Recipe.Recipe.delete(3))# PLEASE KEEP ONLY 2 ELEMENTS A AT TIME INSIDE THE JSON BECAUSE THE ID IS GENERATED BASED ON THE PREVIOUS
        self.assertFalse(Recipe.Recipe.delete(100))
    def test_find_one_method(self):
        recipe1={"recipe_name":"NEW Frozen pizza","instruction":"microwave it","preparation_time_minutes":"20","cooking_time_minutes":"60","servings":"4","calories":"3","category":"frozen food"}
        Recipe.Recipe.add(recipe1)
        result_correct=Recipe.Recipe.get_by_id(3)# PLEASE KEEP ONLY 2 ELEMENTS A AT TIME INSIDE THE JSON BECAUSE THE ID IS GENERATED BASED ON THE PREVIOUS
        result_false=Recipe.Recipe.get_by_id(100)
        self.assertFalse(result_false[0])
        self.assertTrue(result_correct[0])
        flag=True
        for i in result_correct[1]:
            if result_correct[1]['recipe_name']!=recipe1['recipe_name']:
                flag=False
            elif result_correct[1]['instruction']!=recipe1['instruction']:
                flag=False
            elif result_correct[1]['preparation_time_minutes']!=recipe1['preparation_time_minutes']:
                flag=False
            elif result_correct[1]['cooking_time_minutes']!=recipe1['cooking_time_minutes']:
                flag=False
            elif result_correct[1]['servings']!=recipe1['servings']:
                flag=False
            elif result_correct[1]['calories']!=recipe1['calories']:
                flag=False
            elif result_correct[1]['category']!=recipe1['category']:
                flag=False
        self.assertTrue(flag)
        Recipe.Recipe.delete(3)
    def test_find_all_method(self):
        #this method is very close in functionality to import so we won't test it
        pass
            
    
    def test_edit_method(self):
        recipe1={"recipe_name":"NEW Frozen pizza","instruction":"microwave it","preparation_time_minutes":"20","cooking_time_minutes":"60","servings":"4","calories":"3","category":"frozen food"}
        self.assertFalse(Recipe.Recipe.update(4,recipe1))
        Recipe.Recipe.update(2,recipe1)
        result_correct=Recipe.Recipe.get_by_id(2)
        flag=True
        for i in result_correct[1]:
            if result_correct[1]['recipe_name']!=recipe1['recipe_name']:
                flag=False
            elif result_correct[1]['instruction']!=recipe1['instruction']:
                flag=False
            elif result_correct[1]['preparation_time_minutes']!=recipe1['preparation_time_minutes']:
                flag=False
            elif result_correct[1]['cooking_time_minutes']!=recipe1['cooking_time_minutes']:
                flag=False
            elif result_correct[1]['servings']!=recipe1['servings']:
                flag=False
            elif result_correct[1]['calories']!=recipe1['calories']:
                flag=False
            elif result_correct[1]['category']!=recipe1['category']:
                flag=False
        self.assertTrue(flag)
       



   
