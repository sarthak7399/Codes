# https://leetcode.com/problems/find-all-possible-recipes-from-given-supplies/

# Example 1:
# Input: recipes = ["bread"], ingredients = [["yeast","flour"]], supplies = ["yeast","flour","corn"]
# Output: ["bread"]
# Explanation:
# We can create "bread" since we have the ingredients "yeast" and "flour".

from typing import List
class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        available_supplies = set(supplies)  # Convert initial supplies to a set for quick lookup
        
        # Map each recipe to its required ingredients
        recipe_to_ingredients = {recipes[i]: ingredients[i] for i in range(len(recipes))}
        
        visited = {}  # Memoization for checking if a recipe can be made
        result = []  # Stores the list of recipes that can be made
        
        # Helper function to check if a recipe can be made
        def can_make(recipe):
            # If the recipe is already visited and determined to be unmakeable, return False
            if recipe in visited and visited[recipe] == 0:
                return False
            
            # If the recipe is already marked as makeable, return True
            if recipe in visited and visited[recipe] == 1:
                return True
            
            # If the recipe is directly available in supplies, it can be made
            if recipe in available_supplies:
                return True
            
            # If the recipe does not exist in the ingredients list, it cannot be made
            if recipe not in recipe_to_ingredients:
                return False
            
            visited[recipe] = 0  # Mark as being processed (to detect cycles)
            
            # Recursively check if all ingredients can be made
            for ingredient in recipe_to_ingredients[recipe]:
                if not can_make(ingredient):
                    visited[recipe] = -1  # Mark as unmakeable
                    return False
            
            visited[recipe] = 1  # Mark as makeable
            result.append(recipe)  # Add to result list
            return True
        
        # Check all recipes
        for recipe in recipes:
            can_make(recipe)
        
        # Return only the recipes that are marked as makeable
        return [recipe for recipe in recipes if recipe in visited and visited[recipe] == 1]
