#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
  item_count = 0
  count = 0
  for key, value in recipe.items():
        if key in ingredients:
            if value > ingredients[key]:
              return count
            else:
              ingredients[key] = ingredients[key] - value
              item_count += 1
        else:
            return count
  if item_count == len(recipe):
        count += 1

  add_count = recipe_batches(recipe, ingredients)
  count = count + add_count
  return count


if __name__ == '__main__':
  # Change the entries of these dictionaries to test
  # your implementation with different inputs
  #recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  #ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  recipe = { 'milk': 2, 'sugar': 40, 'butter': 20 }
  ingredients = { 'milk': 5, 'sugar': 120, 'butter': 500 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))
