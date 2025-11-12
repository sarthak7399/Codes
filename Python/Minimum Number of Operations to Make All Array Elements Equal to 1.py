# https://leetcode.com/problems/minimum-number-of-operations-to-make-all-array-elements-equal-to-1/

# Example 1:
# Input: nums = [2,6,3,4]
# Output: 4
# Explanation: We can do the following operations:
# - Choose index i = 2 and replace nums[2] with gcd(3,4) = 1. Now we have nums = [2,6,1,4].
# - Choose index i = 1 and replace nums[1] with gcd(6,1) = 1. Now we have nums = [2,1,1,4].
# - Choose index i = 0 and replace nums[0] with gcd(2,1) = 1. Now we have nums = [1,1,1,4].
# - Choose index i = 2 and replace nums[3] with gcd(1,4) = 1. Now we have nums = [1,1,1,1].

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n, num1, g = len(nums), 0, 0

        # Count 1s and find overall GCD
        for x in nums:
            if x == 1:
                num1 += 1
            g = gcd(g, x)

        # If array has any 1s, each non-1 can become 1 in one operation
        if num1 > 0:
            return n - num1

        # If overall GCD > 1, impossible to make all 1
        if g > 1:
            return -1

        # Find smallest subarray with GCD = 1
        min_len = n
        for i in range(n):
            g = 0
            for j in range(i, n):
                g = gcd(g, nums[j])
                if g == 1:
                    min_len = min(min_len, j - i + 1)
                    break

        # Minimum operations = subarray ops + rest conversions
        return min_len + n - 2
