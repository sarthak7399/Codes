# https://leetcode.com/problems/find-missing-elements/

# Example 1:
# Input: nums = [1,4,2,5]
# Output: [3]
# Explanation:
# The smallest integer is 1 and the largest is 5, so the full range should be [1,2,3,4,5]. Among these, only 3 is missing.

from typing import List

class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        # Store all array elements in a set
        # for O(1) average lookup time.
        seen = set(nums)

        # Find the minimum and maximum values in the array.
        mn = min(nums)
        mx = max(nums)

        # Store all missing elements.
        ans = []

        # Check every value between the minimum
        # and maximum values, inclusive.
        for x in range(mn, mx + 1):

            # Add the value if it is not present in the array.
            if x not in seen:
                ans.append(x)

        return ans