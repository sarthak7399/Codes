# https://leetcode.com/problems/sum-of-all-subset-xor-totals/

# Example 1:
# Input: nums = [1,3]
# Output: 6
# Explanation: The 4 subsets of [1,3] are:
# - The empty subset has an XOR total of 0.
# - [1] has an XOR total of 1.
# - [3] has an XOR total of 3.
# - [1,3] has an XOR total of 1 XOR 3 = 2.
# 0 + 1 + 3 + 2 = 6

class Solution:
    # Recursive helper function to calculate sum of XORs of all subsets
    def rec(self, i, xor, n, nums):
        # Base case: if we've considered all elements, return the current XOR value
        if i == n:
            return xor
        # Edge case: shouldn't really occur due to previous condition, but safe guard
        if i > n:
            return 0

        # Option 1: Include nums[i] in the current subset (apply XOR)
        pick = self.rec(i + 1, xor ^ nums[i], n, nums)
        # Option 2: Exclude nums[i] from the current subset
        dont = self.rec(i + 1, xor, n, nums)

        # Return the sum of both choices
        return pick + dont

    def subsetXORSum(self, nums):
        n = len(nums)
        # Start recursion from index 0 with initial XOR value 0
        return self.rec(0, 0, n, nums)
