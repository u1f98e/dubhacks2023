from src.model import Recipe, recipe_schema, Ingredient
from config import db

def get_recipe(recipe_id):
	recipe = Recipe.query.get(recipe_id)
	return recipe_schema.dump(recipe)

def get_recipes():
	recipes = Recipe.query.all()
	return recipe_schema.dump(recipes, many=True)

def create(recipe):
	new_recipe = Recipe(name=recipe["name"], description=recipe["description"], instructions=recipe["instructions"], image_url=recipe["image_url"], user_id=recipe["user_id"])
	for ingredient_name in recipe["ingredients"]:
		exists = Ingredient.query.filter_by(name=ingredient_name).first()
		if not exists:
			db.session.add(Ingredient(name=ingredient_name))

	new_recipe.ingredients = Ingredient.query.filter(Ingredient.name.in_(recipe["ingredients"])).all()
	db.session.add(new_recipe)
	db.session.commit()
	return recipe_schema.dump(new_recipe)

def get_recipe_with_ingredients(ingredients):
	recipes = Recipe.query.filter(Recipe.ingredients.any(ingredient_id=ingredients)).all()
	return recipe_schema.dump(recipes, many=True)