# https://leetcode.com/problems/design-a-food-rating-system/

# Example 1:
# Input
# ["FoodRatings", "highestRated", "highestRated", "changeRating", "highestRated", "changeRating", "highestRated"]
# [[["kimchi", "miso", "sushi", "moussaka", "ramen", "bulgogi"], ["korean", "japanese", "japanese", "greek", "japanese", "korean"], [9, 12, 8, 15, 14, 7]], ["korean"], ["japanese"], ["sushi", 16], ["japanese"], ["ramen", 16], ["japanese"]]
# Output
# [null, "kimchi", "ramen", null, "sushi", null, "ramen"]

# Explanation
# FoodRatings foodRatings = new FoodRatings(["kimchi", "miso", "sushi", "moussaka", "ramen", "bulgogi"], ["korean", "japanese", "japanese", "greek", "japanese", "korean"], [9, 12, 8, 15, 14, 7]);
# foodRatings.highestRated("korean"); // return "kimchi"
#                                     // "kimchi" is the highest rated korean food with a rating of 9.
# foodRatings.highestRated("japanese"); // return "ramen"
#                                       // "ramen" is the highest rated japanese food with a rating of 14.
# foodRatings.changeRating("sushi", 16); // "sushi" now has a rating of 16.
# foodRatings.highestRated("japanese"); // return "sushi"
#                                       // "sushi" is the highest rated japanese food with a rating of 16.
# foodRatings.changeRating("ramen", 16); // "ramen" now has a rating of 16.
# foodRatings.highestRated("japanese"); // return "ramen"
#                                       // Both "sushi" and "ramen" have a rating of 16.
#                                       // However, "ramen" is lexicographically smaller than "sushi".

import heapq
from collections import defaultdict

class FoodRatings(object):

    def __init__(self, foods, cuisines, ratings):
        """
        :type foods: List[str]
        :type cuisines: List[str]
        :type ratings: List[int]
        """
        self.cuisine_to_heap = defaultdict(list)   # cuisine -> max-heap of (-rating, food)
        self.food_to_cuisine = {}                  # food -> cuisine
        self.food_to_rating = defaultdict(int)     # food -> current rating (stored as negative for heapq)

        for i in range(len(foods)):
            self.food_to_cuisine[foods[i]] = cuisines[i]
            # Push (-rating, food) so max rating is at heap top, ties resolved by lexicographic order
            heapq.heappush(self.cuisine_to_heap[cuisines[i]], (-ratings[i], foods[i]))
            self.food_to_rating[foods[i]] = -ratings[i]

    def changeRating(self, food, newRating):
        """
        Update the rating of a given food
        """
        cuisine = self.food_to_cuisine[food]
        # Push the new rating into heap (lazy deletion, old entries remain until popped later)
        heapq.heappush(self.cuisine_to_heap[cuisine], (-newRating, food))
        self.food_to_rating[food] = -newRating

    def highestRated(self, cuisine):
        """
        Return the highest rated food for a given cuisine
        (ties broken by lexicographic order of food name)
        """
        while self.cuisine_to_heap[cuisine]:
            curr = self.cuisine_to_heap[cuisine][0]   # peek top of heap
            # If top is outdated (rating mismatch), pop and continue
            if curr[0] != self.food_to_rating[curr[1]]:
                heapq.heappop(self.cuisine_to_heap[cuisine])
                continue
            # Otherwise, this is the valid highest-rated food
            return curr[1]
        return None
