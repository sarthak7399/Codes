# https://leetcode.com/problems/guess-number-higher-or-lower/description/?envType=study-plan-v2&envId=leetcode-75&__cf_chl_tk=HyYodGpGHXln3lCBwgSgMz5Mt5F17V1WwKfbVKqTu9I-1706898763-0-gaNycGzNElA

# Example 1:
# Input: n = 10, pick = 6
# Output: 6

# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        low, high = 1, n
        while low <= high:
            mid = (low + high) // 2
            G = guess(mid)
            if G == 0:
                return mid
            elif G == -1:
                high = mid - 1
            else:
                low = mid + 1
        return mid