# https://leetcode.com/problems/minimum-operations-to-make-binary-array-elements-equal-to-one-i/

# Example 1:
# Input: nums = [0,1,1,1,0,0]
# Output: 3

# Explanation:
# We can do the following operations:
# Choose the elements at indices 0, 1 and 2. The resulting array is nums = [1,0,0,1,0,0].
# Choose the elements at indices 1, 2 and 3. The resulting array is nums = [1,1,1,0,0,0].
# Choose the elements at indices 3, 4 and 5. The resulting array is nums = [1,1,1,1,1,1].

from typing import List

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        count = 0  # Tracks the number of operations
        total_sum = 0  # Keeps track of the sum of processed elements

        # Iterate through the array, flipping bits when encountering a 0
        for i in range(n - 2):
            if nums[i] == 0:  # If the current element is 0, perform an operation
                count += 1  # Increment operation count
                nums[i] ^= 1  # Flip current element
                nums[i + 1] ^= 1  # Flip next element
                nums[i + 2] ^= 1  # Flip the element after next

            total_sum += nums[i]  # Update the sum of processed elements

        # Check if the entire array is converted to all 1s
        if (total_sum + nums[n - 1] + nums[n - 2]) == n:
            return count  # Return the total number of operations

        return -1  # Return -1 if conversion to all 1s is not possible
