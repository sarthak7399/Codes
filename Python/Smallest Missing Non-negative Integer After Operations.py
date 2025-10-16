# https://leetcode.com/problems/smallest-missing-non-negative-integer-after-operations/

# Example 1:
# Input: nums = [1,-10,7,13,6,8], value = 5
# Output: 4
# Explanation: One can achieve this result by applying the following operations:
# - Add value to nums[1] twice to make nums = [1,0,7,13,6,8]
# - Subtract value from nums[2] once to make nums = [1,0,2,13,6,8]
# - Subtract value from nums[3] twice to make nums = [1,0,2,3,6,8]
# The MEX of nums is 4. It can be shown that 4 is the maximum MEX we can achieve.

class Solution:
    def findSmallestInteger(self, nums: list[int], value: int) -> int:
        # Initialize a list to count occurrences of each remainder
        remainder_count = [0] * value

        # Step 1: Compute remainder frequency
        for num in nums:
            # Handle negative numbers correctly by using ((num % value) + value) % value
            rem = ((num % value) + value) % value
            remainder_count[rem] += 1

        # Step 2: Start finding the smallest non-negative integer result
        result = 0
        while remainder_count[result % value] > 0:
            # If remainder already used, reduce its count and move to next integer
            remainder_count[result % value] -= 1
            result += 1

        # Step 3: Return the smallest integer not "covered" by the given remainders
        return result
