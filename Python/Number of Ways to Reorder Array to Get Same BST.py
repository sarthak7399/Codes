# https://leetcode.com/problems/number-of-ways-to-reorder-array-to-get-same-bst/

# Example 1:
# Input: nums = [2,1,3]
# Output: 1
# Explanation: We can reorder nums to be [2,3,1] which will yield the same BST. There are no other ways to reorder nums which will yield the same BST.

from math import factorial
from typing import List

class Solution:
    def numOfWays(self, nums: List[int]) -> int:
        n = len(nums)
        born = [-1] * (n + 2)  # insertion time of each value; the walls 0 and n + 1 come before everything
        for t, x in enumerate(nums):
            born[x] = t

        sizes, stack = 1, [0]  # product of subtree sizes; values with increasing insertion times
        for v in range(1, n + 2):
            while born[stack[-1]] > born[v]:  # v is the right wall of the value on top
                stack.pop()
                sizes *= v - stack[-1] - 1  # and the value below it is the left wall
            stack.append(v)

        return (factorial(n) // sizes - 1) % (10**9 + 7)