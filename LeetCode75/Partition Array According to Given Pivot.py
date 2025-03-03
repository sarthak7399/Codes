# https://leetcode.com/problems/partition-array-according-to-given-pivot/

# Example 1:
# Input: nums = [9,12,5,10,14,3,10], pivot = 10
# Output: [9,5,3,10,10,12,14]
# Explanation: 
# The elements 9, 5, and 3 are less than the pivot so they are on the left side of the array.
# The elements 12 and 14 are greater than the pivot so they are on the right side of the array.
# The relative ordering of the elements less than and greater than pivot is also maintained. [9, 5, 3] and [12, 14] are the respective orderings.

from typing import List

class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        less, high, count = [], [], 0  # Lists for smaller and larger numbers, count for pivot occurrences

        for num in nums:
            if num < pivot:
                less.append(num)  # Store numbers smaller than pivot
            elif num == pivot:
                count += 1  # Count occurrences of pivot
            else:
                high.append(num)  # Store numbers greater than pivot

        return less + [pivot] * count + high  # Concatenate lists with pivot occurrences in the middle
