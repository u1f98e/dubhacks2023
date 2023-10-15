from sqlalchemy import ForeignKey
from sqlalchemy.orm import mapped_column, Mapped, relationship 
from typing import List, Set

from config import db, ma

recipe_ingredients = db.Table(
	"recipe_ingredients",
	db.Column("recipe_id", db.Integer, db.ForeignKey("recipe.id"), primary_key=True),
	db.Column("ingredient_id", db.Integer, db.ForeignKey("ingredients.id"), primary_key=True),
	db.Column("amount", db.String(32))
)
# class RecipeIngredients(db.Model):
# 	__tablename__ = "recipe_ingredients"
# 	recipe_id = db.Column(db.Integer, ForeignKey("recipe.id"), primary_key=True)
# 	ingredient_id = db.Column(db.Integer, ForeignKey("ingredients.id"), primary_key=True)
# 	amount = db.Column(db.String(32))

class Ingredient(db.Model):
	__tablename__ = "ingredients"
	id: Mapped[int] = mapped_column(primary_key=True)
	name = db.Column(db.String(64), unique=True)

	recipes: Mapped[List["Recipe"]] = relationship(secondary=recipe_ingredients, back_populates="ingredients")

class Recipe(db.Model):
	__tablename__ = "recipe"
	id: Mapped[int] = mapped_column(primary_key=True)
	name = db.Column(db.String(32))
	description = db.Column(db.String)
	instructions = db.Column(db.String)
	image_url = db.Column(db.String(128))

	ingredients: Mapped[List["Ingredient"]] = relationship(secondary=recipe_ingredients, back_populates="recipes")

	user_id: Mapped[int] = mapped_column(ForeignKey("user.id"))
	user: Mapped["User"] = relationship(back_populates="recipes")

class User(db.Model):
	__tablename__ = "user"
	id: Mapped[int] = mapped_column(primary_key=True)
	name = db.Column(db.String(32))
	bio = db.Column(db.String)
	image_url = db.Column(db.String(128))

	recipes: Mapped[List["Recipe"]] = relationship(back_populates="user")

class RecipeSchema(ma.SQLAlchemyAutoSchema):
	class Meta:
		model = Recipe
		load_instance = True
		sqla_session = db.session

recipe_schema = RecipeSchema()

class UserSchema(ma.SQLAlchemyAutoSchema):
	class Meta:
		model = User
		load_instance = True
		sqla_session = db.session

user_schema = UserSchema()
