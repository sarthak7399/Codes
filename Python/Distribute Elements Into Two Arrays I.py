# https://leetcode.com/problems/distribute-elements-into-two-arrays-i/

# Example 2:
# Input: nums = [5,4,3,8]
# Output: [5,3,4,8]
# Explanation: After the first 2 operations, arr1 = [5] and arr2 = [4].
# In the 3rd operation, as the last element of arr1 is greater than the last element of arr2 (5 > 4), append nums[3] to arr1, hence arr1 becomes [5,3].
# In the 4th operation, as the last element of arr2 is greater than the last element of arr1 (4 > 3), append nums[4] to arr2, hence arr2 becomes [4,8].
# After 4 operations, arr1 = [5,3] and arr2 = [4,8].
# Hence, the array result formed by concatenation is [5,3,4,8].

from typing import List

class Solution:
    def resultArray(self, nums: List[int]) -> List[int]:
        # Initialise the two arrays with the first two elements.
        arr1 = [nums[0]]
        arr2 = [nums[1]]

        # Process the remaining elements.
        for i in range(2, len(nums)):
            # Append the current number to the array whose
            # last element is greater.
            if arr1[-1] > arr2[-1]:
                arr1.append(nums[i])
            else:
                arr2.append(nums[i])

        # Concatenate both arrays to form the final result.
        return arr1 + arr2