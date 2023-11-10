from extensions import db
from http import HTTPStatus
class Recipe(db.Model):
    __tablename__ = 'recipe'

    id = db.Column(db.Integer, primary_key=True)
    recipe_name = db.Column(db.String(100), nullable=False)
    ingredients = db.relationship('Ingredient', backref='recipe', lazy=True)
    instructions = db.Column(db.String(1000))  # Adjust size as needed
    preparation_time_minutes = db.Column(db.Integer)
    cooking_time_minutes = db.Column(db.Integer)
    servings = db.Column(db.Integer)
    calories = db.Column(db.Integer)
    category = db.Column(db.String(50))

    @property
    def data(self):
        return {
            'id': self.id,
            'recipe_name': self.recipe_name,
            'ingredients': [ingredient.to_dict() for ingredient in self.ingredients],
            'instructions': self.instructions,
            'preparation_time_minutes': self.preparation_time_minutes,
            'cooking_time_minutes': self.cooking_time_minutes,
            'servings': self.servings,
            'calories': self.calories,
            'category': self.category
        }
    def save(self):
        db.session.add(self)
        db.session.commit()
    @classmethod
    def get_all(cls):
        result = cls.query.all()
        return [recipe.data for recipe in result]
    @classmethod
    def get_by_id(cls,id):
        return cls.query.filter(cls.id==id).first()
    @classmethod
    def update(cls, id, data):
        recipe = cls.query.filter_by(id=id).first()
        if not recipe:
            return {'message': 'Recipe not found'}, HTTPStatus.NOT_FOUND
        recipe.recipe_name = data.get('recipe_name', recipe.recipe_name)
        recipe.instructions = data.get('instructions', recipe.instructions)
        recipe.preparation_time_minutes = data.get('preparation_time_minutes', recipe.preparation_time_minutes)
        recipe.cooking_time_minutes = data.get('cooking_time_minutes', recipe.cooking_time_minutes)
        recipe.servings = data.get('servings', recipe.servings)
        recipe.calories = data.get('calories', recipe.calories)
        recipe.category = data.get('category', recipe.category)
        db.session.commit()
        return recipe.data, HTTPStatus.OK
    @classmethod
    def delete(cls,id):
        recipe = cls.query.filter(cls.id == id).first()
        if recipe is None:
            return {'message': 'recipe not found'}, HTTPStatus.NOT_FOUND
        db.session.delete(recipe)
        db.session.commit()
        return {}, HTTPStatus.NO_CONTENT

    
        


class Ingredient(db.Model):
    __tablename__ = 'ingredient'

    id = db.Column(db.Integer, primary_key=True)
    recipe_id = db.Column(db.Integer, db.ForeignKey('recipe.id'), nullable=False)
    ingredient = db.Column(db.String(50), nullable=False)
    amount = db.Column(db.Integer, nullable=False)
    @classmethod
    def to_dict(self):
        return {
            'ingredient': self.ingredient,
            'amount': self.amount
        } 
# @classmethod
# def post(cls, recipe_id, ingredient_data):
#         new_ingredient = cls(
#             recipe_id=recipe_id,
#             ingredient=ingredient_data['ingredient'],
#             amount=ingredient_data['amount']
#         )
#         db.session.add(new_ingredient)
#         db.session.commit()

#         return new_ingredient.to_dict(), HTTPStatus.CREATED