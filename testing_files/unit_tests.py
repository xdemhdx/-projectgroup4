import unittest
#import datalayer.menu_management # you have to change this according to your folder/file name

class UnitTestsMenuManagement(unittest.TestCase):
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