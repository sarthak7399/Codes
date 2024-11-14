# https://leetcode.com/problems/minimized-maximum-of-products-distributed-to-any-store/

# Example 1:
# Input: n = 6, quantities = [11,6]
# Output: 3
# Explanation: One optimal way is:
# - The 11 products of type 0 are distributed to the first four stores in these amounts: 2, 3, 3, 3
# - The 6 products of type 1 are distributed to the other two stores in these amounts: 3, 3
# The maximum number of products given to any store is max(2, 3, 3, 3, 3, 3) = 3.

from math import ceil
from typing import List
class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        
        # Condition function to check if a given maximum (k) per store can distribute 
        # all items within n stores.
        def condition(k):
            count = 0  # count of required stores with current maximum limit per store
            for q in quantities:
                # Calculate required stores for each quantity if each store gets at most k items
                count += ceil(q / k)
            # Return True if we can distribute within the n stores limit
            return count <= n
        
        # Initialize binary search boundaries: min quantity (1) to max quantity in the list
        start, end = 1, max(quantities)
        
        # Perform binary search to find the minimized maximum
        while start < end:
            mid = start + (end - start) // 2  # Midpoint to check as the potential minimized max
            # If the current mid value satisfies the distribution within n stores
            if condition(mid):
                end = mid  # Try a smaller maximum by moving the end pointer
            else:
                start = mid + 1  # Increase the minimum possible max by moving the start pointer

        # Start will hold the minimized maximum value at the end of the binary search
        return start
