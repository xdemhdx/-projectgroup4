import unittest
#import model # you have to change this according to your folder/file name
from models.Recipe import Recipe

class UnitTestsMenuManagement(unittest.TestCase):
    def test_recipe_class(self):
         try:
            recipe1=Recipe.File.recipe(-2,"chocolate cookie",["cookie stuff",-10,"Kg"],"Just mix and hope",-20,-20,-4,-600,"Cookie")
            flag=False
         except:
             flag=True
         self.assertTrue(flag)
        
    def test_import_json(self):
        recipe_result=Recipe.File.import_file()
        self.assertTrue(recipe_result[0])
        self.assertTrue(len(recipe_result)==2)
        self.assertTrue(recipe_result[1]["recipes"][0]["id"]>0)
        self.assertTrue(recipe_result[1]["recipes"][0]["preparation_time_minutes"].isdigit())
        self.assertTrue(int(recipe_result[1]["recipes"][0]["preparation_time_minutes"])>0)
        self.assertTrue(recipe_result[1]["recipes"][0]['cooking_time_minutes'].isdigit())
        self.assertTrue(int(recipe_result[1]["recipes"][0]['cooking_time_minutes'])>0)
        self.assertTrue(recipe_result[1]["recipes"][0]["servings"].isdigit())
        self.assertTrue(int(recipe_result[1]["recipes"][0]["servings"])>0)
        self.assertTrue(recipe_result[1]["recipes"][0]["calories"].isdigit())
        self.assertTrue(int(recipe_result[1]["recipes"][0]["calories"])>0)
        
    def test_save_file(self):
        #just add validation here or do it through the recipe class
        recipe1={"id":"1","recipe_name":"food","instruction":"burn it","preparation_time_minutes":"-600","cooking_time_minutes":"-200","servings":20,"calories":"0","category":"burnt food"}
        self.assertFalse(Recipe.File.save_file(recipe1))        