# https://leetcode.com/problems/take-gifts-from-the-richest-pile/

# Example 1:
# Input: gifts = [25,64,9,4,100], k = 4
# Output: 29
# Explanation: 
# The gifts are taken in the following way:
# - In the first second, the last pile is chosen and 10 gifts are left behind.
# - Then the second pile is chosen and 8 gifts are left behind.
# - After that the first pile is chosen and 5 gifts are left behind.
# - Finally, the last pile is chosen again and 3 gifts are left behind.
# The final remaining gifts are [5,8,9,4,3], so the total number of gifts remaining is 29.

import math
from typing import List
class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        for _ in range(k):
            # Find the index of the pile with the maximum number of gifts
            max_index = gifts.index(max(gifts))
            
            # Replace the pile with the floor of the square root of its current value
            gifts[max_index] = math.floor(math.sqrt(gifts[max_index]))

        # Return the sum of all remaining gifts
        return sum(gifts)