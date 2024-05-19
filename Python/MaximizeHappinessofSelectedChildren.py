# https://leetcode.com/problems/maximize-happiness-of-selected-children

# Example 1:
# Input: happiness = [1,2,3], k = 2
# Output: 4
# Explanation: We can pick 2 children in the following way:
# - Pick the child with the happiness value == 3. The happiness value of the remaining children becomes [0,1].
# - Pick the child with the happiness value == 1. The happiness value of the remaining child becomes [0]. Note that the happiness value cannot become less than 0.
# The sum of the happiness values of the selected children is 3 + 1 = 4.

from typing import List
class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        # Sort happiness values in non-increasing order
        sorted_happiness = sorted(happiness, reverse=True)
        
        # Initialize the total happiness sum
        total_happiness = 0
        
        # Iterate over the sorted happiness values
        for i, happy in enumerate(sorted_happiness):
            # Check if the happiness value is positive
            if happy > 0:
                # Calculate the modified happiness value considering the cost of modification
                modified_happy = happy - i
                
                # Check if modifying the happiness value doesn't make it negative
                if modified_happy > -1:
                    # Add the modified happiness value to the total happiness sum
                    total_happiness += modified_happy
                    
                    # Decrement the number of allowed modifications
                    k -= 1
                    
                    # Check if the number of allowed modifications is exhausted
                    if k == 0:
                        # Return the total happiness sum
                        return total_happiness
        
        # Return the total happiness sum
        return total_happiness
