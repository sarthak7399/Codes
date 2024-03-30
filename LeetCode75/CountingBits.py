# https://leetcode.com/problems/counting-bits/description/?envType=study-plan-v2&envId=leetcode-75&__cf_chl_tk=HyYodGpGHXln3lCBwgSgMz5Mt5F17V1WwKfbVKqTu9I-1706898763-0-gaNycGzNElA

# Example 1:
# Input: n = 2
# Output: [0,1,1]
# Explanation:
# 0 --> 0
# 1 --> 1
# 2 --> 10

from typing import List
class Solution:
    def countBits(self, n: int) -> List[int]:
        return [bin(x).count('1') for x in range(0, n + 1)]