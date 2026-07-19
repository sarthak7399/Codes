# https://leetcode.com/problems/divide-an-array-into-subarrays-with-minimum-cost-i/

# Example 1:
# Input: nums = [1,2,3,12]
# Output: 6
# Explanation: The best possible way to form 3 subarrays is: [1], [2], and [3,12] at a total cost of 1 + 2 + 3 = 6.
# The other possible ways to form 3 subarrays are:
# - [1], [2,3], and [12] at a total cost of 1 + 2 + 12 = 15.
# - [1,2], [3], and [12] at a total cost of 1 + 3 + 12 = 16.

class Solution:
    def minimumCost(self, v):
        n = len(v)                 # Total number of elements

        s = v[0]                   # Take the first element as base cost

        v[1:n] = sorted(v[1:n])    # Sort all elements except the first one

        # Add the two smallest elements from the remaining list
        s = s + v[1] + v[2]

        return s                   # Return the minimum total cost
