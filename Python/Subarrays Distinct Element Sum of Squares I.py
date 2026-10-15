# https://leetcode.com/problems/subarrays-distinct-element-sum-of-squares-i/

# Example 1:
# Input: nums = [1,2,1]
# Output: 15
# Explanation: Six possible subarrays are:
# [1]: 1 distinct value
# [2]: 1 distinct value
# [1]: 1 distinct value
# [1,2]: 2 distinct values
# [2,1]: 2 distinct values
# [1,2,1]: 2 distinct values
# The sum of the squares of the distinct counts in all subarrays is equal to 12 + 12 + 12 + 22 + 22 + 22 = 15.

from typing import List

class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        # Get the length of the array.
        n = len(nums)

        # Store the sum of squared distinct counts for all subarrays.
        res = 0

        # Choose each index as the starting point of a subarray.
        for i in range(n):
            # Track distinct elements in the current subarray.
            s = set()

            # Extend the subarray from index i to every possible ending index.
            for j in range(i, n):
                # Add the current element to the set.
                # Duplicate elements are automatically ignored.
                s.add(nums[j])

                # Count the distinct elements in the current subarray.
                d = len(s)

                # Add the square of the distinct element count.
                res += d * d

        # Return the total sum across all subarrays.
        return res