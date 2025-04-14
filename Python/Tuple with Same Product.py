# https://leetcode.com/problems/tuple-with-same-product/

# Example 2:
# Input: nums = [1,2,4,5,10]
# Output: 16
# Explanation: There are 16 valid tuples:
# (1,10,2,5) , (1,10,5,2) , (10,1,2,5) , (10,1,5,2)
# (2,5,1,10) , (2,5,10,1) , (5,2,1,10) , (5,2,10,1)
# (2,10,4,5) , (2,10,5,4) , (10,2,4,5) , (10,2,5,4)
# (4,5,2,10) , (4,5,10,2) , (5,4,2,10) , (5,4,10,2)

from collections import defaultdict
from typing import List
class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        n = len(nums)
        product_count = defaultdict(int)

        # Step 1: Compute products of all pairs and store their frequency
        for i in range(n):
            for j in range(i + 1, n):
                product = nums[i] * nums[j]
                product_count[product] += 1

        total = 0
        # Step 2: Count valid tuples based on frequency
        for count in product_count.values():
            if count >= 2:
                total += count * (count - 1) // 2  # Choose 2 pairs from count pairs
        
        return total * 8  # Each tuple (a, b, c, d) can be arranged in 8 ways