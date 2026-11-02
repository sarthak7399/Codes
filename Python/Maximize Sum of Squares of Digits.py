# https://leetcode.com/problems/maximize-sum-of-squares-of-digits/

# Example 1:
# Input: num = 2, sum = 3
# Output: "30"
# Explanation:
# There are 3 good integers: 12, 21, and 30.
# The score of 12 is 12 + 22 = 5.
# The score of 21 is 22 + 12 = 5.
# The score of 30 is 32 + 02 = 9.
# The maximum score is 9, which is achieved by the good integer 30. Therefore, the answer is "30".

class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:
        # Each digit can be at most 9, so the maximum possible sum is 9 * num.
        if sum > 9 * num:
            return ""

        # Divide the required sum by 9.
        # q = number of digits that can be 9.
        # r = remaining sum that cannot form another 9.
        q, r = divmod(sum, 9)

        # Place the largest digits first to maximize the number's square sum:
        # 1. Add q digits of 9.
        # 2. Add the remaining digit r if it is non-zero.
        # 3. Fill the remaining positions with zeros.
        return '9' * q + (str(r) if r else '') + '0' * (num - q - (1 if r else 0))