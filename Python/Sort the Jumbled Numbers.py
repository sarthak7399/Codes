# https://leetcode.com/problems/sort-the-jumbled-numbers/

# Example 1:
# Input: mapping = [8,9,4,0,2,1,3,5,7,6], nums = [991,338,38]
# Output: [338,38,991]
# Explanation: 
# Map the number 991 as follows:
# 1. mapping[9] = 6, so all occurrences of the digit 9 will become 6.
# 2. mapping[1] = 9, so all occurrences of the digit 1 will become 9.
# Therefore, the mapped value of 991 is 669.
# 338 maps to 007, or 7 after removing the leading zeros.
# 38 maps to 07, which is also 7 after removing leading zeros.
# Since 338 and 38 share the same mapped value, they should remain in the same relative order, so 338 comes before 38.
# Thus, the sorted array is [338,38,991].

from typing import List
class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        def compare(num):
            result = 0
            place = 1

            if num == 0:
                return mapping[0]

            while num > 0:
                digit = num % 10
                num //= 10
                new_digit = mapping[digit]
                result += new_digit * place
                place *= 10
            return result

        nums.sort(key=compare)
        return nums
        