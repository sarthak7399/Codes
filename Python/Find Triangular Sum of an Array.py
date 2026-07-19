# https://leetcode.com/problems/find-triangular-sum-of-an-array/

# Example 1:
# Input: nums = [1,2,3,4,5]
# Output: 8
# Explanation:
# The above diagram depicts the process from which we obtain the triangular sum of the array.

class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        n = len(nums) - 1  
        ans, A = nums[0], 1  # ans accumulates result, A = binomial coefficient (nCk)
        
        for k in range(1, n+1):
            A = A * (n-k+1) // k   # update binomial coefficient using formula
            ans = (ans + nums[k] * A) % 10  # add contribution of nums[k]*nCk modulo 10
        
        return ans  # final triangular sum



# This problem reduces to binomial expansion.
# The final number is a weighted sum of input numbers with binomial coefficients:

# Triangular Sum = (nums[0]*C(n,0) + nums[1]*C(n,1) + ... + nums[n]*C(n,n)) % 10

# Where C(n,k) = binomial coefficient.

# Diagram for flow (Pascal triangle style):
# nums = [a, b, c, d]
# Row 0:   a   b   c   d
# Row 1:    a+b   b+c   c+d
# Row 2:      (a+2b+c)   (b+2c+d)
# Row 3:          a+3b+3c+d  → triangular sum