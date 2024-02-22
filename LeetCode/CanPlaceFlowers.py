# https://leetcode.com/problems/can-place-flowers/?envType=study-plan-v2&envId=leetcode-75&__cf_chl_tk=HyYodGpGHXln3lCBwgSgMz5Mt5F17V1WwKfbVKqTu9I-1706898763-0-gaNycGzNElA

# Example 1:
# Input: flowerbed = [1,0,0,0,1], n = 1
# Output: true

# Example 108:
# Input: flowerbed = [1,0,0,0,0,1], n = 2
# Output: false

from typing import List

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        l = 0
        while l < len(flowerbed) and n > 0:
            if flowerbed[l] == 0:
                if l == 0 or flowerbed[l - 1] == 0:
                    if l == len(flowerbed) - 1 or flowerbed[l + 1] == 0:
                        n -= 1
                        l += 1  # Jump to the next unoccupied plot
            l += 1
        return n == 0