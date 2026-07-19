# https://leetcode.com/problems/replace-non-coprime-numbers-in-array/

# Example 1:
# Input: nums = [6,4,3,2,7,6,2]
# Output: [12,7,6]
# Explanation: 
# - (6, 4) are non-coprime with LCM(6, 4) = 12. Now, nums = [12,3,2,7,6,2].
# - (12, 3) are non-coprime with LCM(12, 3) = 12. Now, nums = [12,2,7,6,2].
# - (12, 2) are non-coprime with LCM(12, 2) = 12. Now, nums = [12,7,6,2].
# - (6, 2) are non-coprime with LCM(6, 2) = 6. Now, nums = [12,7,6].
# There are no more adjacent non-coprime numbers in nums.
# Thus, the final modified array is [12,7,6].
# Note that there are other ways to obtain the same resultant array.

from math import gcd
from typing import List

class Solution:
    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:
        stack = []  # acts like a processing stack to merge numbers

        for num in nums:
            # Keep merging with the last number in stack if gcd > 1 (not coprime)
            while stack:
                g = gcd(stack[-1], num)  # greatest common divisor of last element & current num
                if g == 1:
                    # If coprime, stop merging
                    break
                # Merge into LCM: (a*b)//gcd(a,b)
                num = (stack.pop() * num) // g
            # Push the merged (or original) number back
            stack.append(num)

        # Final stack contains only coprime-adjacent numbers
        return stack
