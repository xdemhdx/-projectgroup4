from models.Recipe import Recipe


# file = Recipe.File.import_file()


data = {'recipe_name': 'Korn Flakes', 'instruction': '123', 'preparation_time_minutes': "1", 'cooking_time_minutes': "1", 'servings': "4", 'calories': "69", 'category': 'pasta'}
print(Recipe.add(data))
# print(Recipe.update(1,data))
# print(Recipe.delete(4))
# print(Recipe.delete(3))
# print(Recipe.delete(2))
# print(Recipe.delete(1))
# print(Recipe.delete(1))




