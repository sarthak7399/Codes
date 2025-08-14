# https://leetcode.com/problems/largest-3-same-digit-number-in-string/

# Example 1:
# Input: num = "6777133339"
# Output: "777"
# Explanation: There are two distinct good integers: "777" and "333".
# "777" is the largest, so we return "777".

class Solution:
    def largestGoodInteger(self, num: str) -> str:
        nums = 999
        while nums != 0:
            if str(nums) in num:
                return str(nums)
            nums -= 111
        return "" if "000" not in num else "000"