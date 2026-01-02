# https://leetcode.com/problems/n-repeated-element-in-size-2n-array/

# Example 1:
# Input: nums = [1,2,3,3]
# Output: 3

class Solution:
    def repeatedNTimes(self, A: list[int]) -> int:
        # Iterate till the third last element
        for i in range(len(A) - 2):
            # Check if current element repeats immediately
            # or with one element gap
            if A[i] == A[i + 1] or A[i] == A[i + 2]:
                return A[i]
        # If not found earlier, the last element is the repeated one
        return A[-1]
