# https://leetcode.com/problems/minimum-operations-to-make-array-values-equal-to-k/

# Example 1:
# Input: nums = [5,2,5,4,5], k = 2
# Output: 2
# Explanation:
# The operations can be performed in order using valid integers 4 and then 2.

from typing import List
class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        nums.sort()  # Sort the array for easier comparison
        count_k = 0          # Count of elements equal to k
        greater = 0          # Count of unique elements greater than k
        last_greater = None  # Track last greater element to count unique only
        smaller_exist = False  # Flag to check if any element < k exists

        for num in nums:
            if num == k:
                count_k += 1  # Count occurrences of k
            elif num > k:
                if num != last_greater:
                    last_greater = num
                    greater += 1  # Count unique elements > k
            else:
                smaller_exist = True  # If any element < k exists

        if count_k == len(nums):
            return 0  # All elements are equal to k, no operation needed
        if smaller_exist:
            return -1  # Cannot make all elements ≥ k if some are < k
        return greater  # Return number of unique elements > k that need to be removed
