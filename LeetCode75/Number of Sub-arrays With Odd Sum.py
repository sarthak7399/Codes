# https://leetcode.com/problems/number-of-sub-arrays-with-odd-sum/

# Example 1:
# Input: arr = [1,3,5]
# Output: 4
# Explanation: All subarrays are [[1],[1,3],[1,3,5],[3],[3,5],[5]]
# All sub-arrays sum are [1,4,9,3,8,5].
# Odd sums are [1,9,3,5] so the answer is 4.

from typing import List
class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        oddCount, prefixSum, mod = 0, 0, 1_000_000_007  # Initialize variables
        
        for a in arr:
            prefixSum += a  # Update prefix sum
            oddCount += prefixSum % 2  # Count odd prefix sums
        
        # Compute total odd subarrays using the formula
        oddCount += (len(arr) - oddCount) * oddCount 
        
        return oddCount % mod  # Return result modulo 1e9+7
