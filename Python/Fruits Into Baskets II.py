# https://leetcode.com/problems/fruits-into-baskets-ii/

# Example 1:
# Input: fruits = [4,2,5], baskets = [3,5,4]
# Output: 1
# Explanation:
# fruits[0] = 4 is placed in baskets[1] = 5.
# fruits[1] = 2 is placed in baskets[0] = 3.
# fruits[2] = 5 cannot be placed in baskets[2] = 4.
# Since one fruit type remains unplaced, we return 1.

from typing import List

class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        used = [False] * len(baskets)  # To keep track of which baskets have been used
        unplaced = 0                             # Counter to track fruits that couldn't be placed

        # Try placing each fruit in a suitable unused basket
        for fruit in fruits:
            placed = False                       # Flag to check if current fruit is placed
            for i in range(len(baskets)):
                # Place fruit in the first unused basket that can hold it
                if not used[i] and baskets[i] >= fruit:
                    used[i] = True               # Mark this basket as used
                    placed = True
                    break                        # Move to next fruit once placed

            # If fruit could not be placed in any basket, increment unplaced counter
            if not placed:
                unplaced += 1

        return unplaced  # Return the total number of fruits that couldn't be placed
