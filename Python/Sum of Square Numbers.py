# https://leetcode.com/problems/sum-of-square-numbers/

# Example 1:
# Input: c = 5
# Output: true
# Explanation: 1 * 1 + 2 * 2 = 5

from cmath import sqrt
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        left,right = 0,int(sqrt(c))

        while left<=right:
            sumsquare = left*left + right*right
            if sumsquare==c:
                return True
            if sumsquare>c:
                right-=1
            else:
                left+=1
        return False