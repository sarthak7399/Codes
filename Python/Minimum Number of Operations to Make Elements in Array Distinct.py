# https://leetcode.com/problems/minimum-number-of-operations-to-make-elements-in-array-distinct/

# Example 1:
# Input: nums = [1,2,3,4,2,3,3,5,7]
# Output: 2
# Explanation:
# In the first operation, the first 3 elements are removed, resulting in the array [4, 2, 3, 3, 5, 7].
# In the second operation, the next 3 elements are removed, resulting in the array [3, 5, 7], which has distinct elements.
# Therefore, the answer is 2.

from typing import List
class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        from collections import Counter
        
        # Count the frequency of each number in the list
        freq = Counter(nums)

        # Helper function to check if all elements are distinct or not repeated
        def is_distinct():
            return all(v <= 1 for v in freq.values())

        # If all numbers are already distinct, no operations are needed
        if is_distinct():
            return 0

        operations = 0

        while nums:
            # If less than 3 numbers remain, we need only one more operation to make them distinct
            if len(nums) < 3:
                return operations + 1

            # Remove the first 3 elements from `nums`, and update their frequencies
            for i in range(3):
                freq[nums[i]] -= 1
                if freq[nums[i]] == 0:
                    del freq[nums[i]]  # Remove from counter if frequency becomes zero

            nums = nums[3:]  # Process the remaining elements
            operations += 1

            # Check if the remaining elements are all distinct
            if is_distinct():
                return operations

        return operations
