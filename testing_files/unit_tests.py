import unittest
import datalayer # you have to change this according to your folder/file name



class UnitTestsMenuManagement(unittest.TestCase):
    def test_recipe_class(self):
    # the class should follow this order id, name, ingredient[name,amount,unit], instruction, prep_time,cook_time, serving, calories, category
    # there won't be a need to do setters and getters for now
        recipe1=recipe_manager.recipe(-2,"chocolate cookie",["cookie stuff",-10,"Kg"],"Just mix and hope",-20,-20,-4,-600,"Cookie")
        self.assertIsInstance(recipe1.id,int)
        self.assertIsInstance(recipe1.prep_time,int)
        self.assertIsInstance(recipe1.cook_time,int)
        self.assertIsInstance(recipe1.serving,int)
        self.assertIsInstance(recipe1.calories,int)
        self.assertIsInstance(recipe1.ingredeints.amount,int)
        self.assertIsInstance(recipe1.name,str)
        self.assertIsInstance(recipe1.instruction,str)
        self.assertIsInstance(recipe1.ingredients,list)
        self.assertIsInstance(recipe1.category,str)
        self.assertTrue(recipe1.id>0)
        self.assertTrue(recipe1.prep_time>0)
        self.assertTrue(recipe1.cook_time>0)
        self.assertTrue(recipe1.serving>0)
        self.assertTrue(recipe1.calories>0)
        self.assertTrue(recipe1.ingredients.amount>0)
        
    def test_import_json(self):
        recipe_result=menu_management.Test.import_file()# you have to change this according to your import function
        self.assertTrue(recipe_result[0])
        self.assertTrue(len(recipe_result[1])==1)
        self.assertTrue(recipe_result[1]["recipes"][0]["ingredients"][0]["amount"]>0)
        self.assertTrue(recipe_result[1]["recipes"][0]["preparation time (minutes)"]>0)
        self.assertTrue(recipe_result[1]["recipes"][0]["cooking time (minutes)"]>0)
        self.assertTrue(recipe_result[1]["recipes"][0]["servings"]>0)
        self.assertTrue(recipe_result[1]["recipes"][0]["calories"]>0)
        self.assertTrue(recipe_result[1]["recipes"][0]["id"]>0)