import unittest
#import model # you have to change this according to your folder/file name
from Recipe import Recipe , File

class UnitTestsMenuManagement(unittest.TestCase):
    def test_recipe_class(self):
        data = {
            'recipe_name': "",
            'instruction': "",
            'preparation_time_minutes': "-10",
            'cooking_time_minutes': "-20",
            'servings': "-4",
            'calories': "-600",
            'category': "Maybe?:)"
        }
        try:
            Recipe.add(data)
            flag = False  # Flag should remain False if no exception is raised
        except ValueError:
            flag = True  # Flag is set to True if a ValueError is raised
        self.assertTrue(flag)  
        
    def test_import_json(self):
        recipe_result = File.import_file()
        self.assertTrue(recipe_result[0])  # Assert that the import was successful
        self.assertEqual(len(recipe_result), 2)  # Assert that there are two elements in the tuple
        recipes = recipe_result[1]["recipes"]
        self.assertTrue(isinstance(recipes, list))  # Assert that recipes is a list
        self.assertTrue(len(recipes) > 0)  # Assert that there is at least one recipe
        # Test the first recipe in the list
        first_recipe = recipes[0]
        self.assertTrue(first_recipe["id"] > 0)
        self.assertTrue(str(first_recipe["preparation_time_minutes"]).isdigit())
        self.assertTrue(int(first_recipe["preparation_time_minutes"]) > 0)
        self.assertTrue(str(first_recipe["cooking_time_minutes"]).isdigit())
        self.assertTrue(int(first_recipe["cooking_time_minutes"]) > 0)
        self.assertTrue(str(first_recipe["servings"]).isdigit())
        self.assertTrue(int(first_recipe["servings"]) > 0)
        self.assertTrue(str(first_recipe["calories"]).isdigit())
        self.assertTrue(int(first_recipe["calories"]) > 0)
    

    # Remove this because saving a file should be integration remember whenn we had get all then append to last then send it to file_save() 
    # def test_save_file(self):
    #     #just add validation here or do it through the recipe class
    #     recipe1={"id":"1","recipe_name":"food","instruction":"burn it","preparation_time_minutes":"-600","cooking_time_minutes":"-200","servings":20,"calories":"0","category":"burnt food"}
    #     self.assertFalse(File.save_file(recipe1))        