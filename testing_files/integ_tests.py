import unittest
#import datalayer
class IntegrationTestsMenuManagement(unittest.TestCase):
    def test_add_method(self):
        manager=recipe_manager.recipes()
        recipe1=recipe_manager.recipe(-2,"chocolate cookie",["cookie stuff",-10,"Kg"],"Just mix and hope",-20,-20,-4,-600,"Cookie")
        self.assertFalse(manager.add(recipe1))
    
    def test_delete_method(self):
        manager=recipe_manager.recipes()
        recipe1=recipe_manager.recipe(2,"chocolate cookie",["cookie stuff",10,"Kg"],"Just mix and hope",20,20,4,600,"Cookie")
        recipe2=[recipe1]
        self.assertTrue(all(x in manager.recipeList for x in recipe2))#subject to change
        manager.add(recipe1)
        manager.delete(2)
        self.assertTrue(all(x in manager.recipeList for x in recipe2))#subject to change
    
    def test_find_one_method(self):
        manager=recipe_manager.recipes()
        recipe1=recipe_manager.recipe(2,"chocolate cookie",["cookie stuff",10,"Kg"],"Just mix and hope",20,20,4,600,"Cookie")
        result=manager.find(2)
        self.assertTrue(result.name==recipe1.name)
        self.assertTrue(result.instruction==recipe1.instruction)
        self.assertTrue(result.ingredients.amount==recipe1.ingredients.amount)
        self.assertTrue(result.ingredients.name==recipe1.ingredients.name)
        self.assertTrue(result.ingredients.unit==recipe1.ingredients.amount)
        self.assertTrue(result.prep_time==recipe1.prep_time)
        self.assertTrue(result.cook_time==recipe1.cook_time)
        self.assertTrue(result.serving==recipe1.serving)
        self.assertTrue(result.category==recipe1.category)
    
    def test_find_all_method(self):
        #to be filled
        return None
    
    def test_edit_method(self):
        # To be dicussed
        return None



   
