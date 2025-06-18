# https://leetcode.com/problems/divide-array-into-arrays-with-max-difference/

# Example 1:
# Input: nums = [1,3,4,8,7,9,3,5,1], k = 2
# Output: [[1,1,3],[3,4,5],[7,8,9]]
# Explanation:
# The difference between any two elements in each array is less than or equal to 2.

from typing import List

class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        nums.sort()  # Sort the array to group close elements together
        result = []

        # Iterate over the sorted list in steps of 3 to form triplets
        for i in range(0, len(nums), 3):
            triplet = nums[i:i + 3]

            # Check if the difference between max and min in the triplet is more than k
            if triplet[-1] - triplet[0] > k:
                return []  # Cannot form a valid group, return empty list

            result.append(triplet)  # Add valid group to the result list

        return result
