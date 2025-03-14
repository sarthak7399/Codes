# https://leetcode.com/problems/maximum-candies-allocated-to-k-children/

# Example 1:
# Input: candies = [5,8,6], k = 3
# Output: 5
# Explanation: We can divide candies[1] into 2 piles of size 5 and 3, and candies[2] into 2 piles of size 5 and 1. We now have five piles of candies of sizes 5, 5, 3, 5, and 1. We can allocate the 3 piles of size 5 to 3 children. It can be proven that each child cannot receive more than 5 candies.

from typing import List
class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        # Function to check if we can distribute at least 'k' piles of 'x' candies
        def check(x):
            if x == 0:  # Edge case: Avoid division by zero
                return True
            return sum(candy // x for candy in candies) >= k  # Count how many piles of 'x' we can make
        
        left, right = 0, sum(candies) // k  # Max possible candy per pile is sum(candies) // k

        # Binary search for the maximum 'x' such that we can form at least 'k' piles
        while left <= right:
            mid = (left + right) // 2  # Middle value to check
            if check(mid):  # If 'mid' candies per pile is possible
                left = mid + 1  # Try to increase 'mid' (maximize candies per pile)
            else:
                right = mid - 1  # Decrease 'mid' (not enough piles possible)
        
        return right  # Maximum possible candies per pile
