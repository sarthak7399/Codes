# https://leetcode.com/problems/construct-the-minimum-bitwise-array-i/

# Example 1:
# Input: nums = [2,3,5,7]
# Output: [-1,1,4,3]
# Explanation:
# For i = 0, as there is no value for ans[0] that satisfies ans[0] OR (ans[0] + 1) = 2, so ans[0] = -1.
# For i = 1, the smallest ans[1] that satisfies ans[1] OR (ans[1] + 1) = 3 is 1, because 1 OR (1 + 1) = 3.
# For i = 2, the smallest ans[2] that satisfies ans[2] OR (ans[2] + 1) = 5 is 4, because 4 OR (4 + 1) = 5.
# For i = 3, the smallest ans[3] that satisfies ans[3] OR (ans[3] + 1) = 7 is 3, because 3 OR (3 + 1) = 7.

class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        for i, j in enumerate(nums):
            # Special case: no valid answer for 2
            if j == 2:
                nums[i] = -1
            else:
                # Bit trick to compute smallest x such that x | (x+1) = j
                nums[i] = ((((j + 1) ^ j) + 1) >> 2) ^ j

        return nums
