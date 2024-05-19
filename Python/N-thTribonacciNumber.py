# https://leetcode.com/problems/n-th-tribonacci-number/


# Example 1:
# Input: n = 4
# Output: 4
# Explanation:
# T_3 = 0 + 1 + 1 = 2
# T_4 = 1 + 1 + 2 = 4

class Solution:
    def tribonacci(self, n: int) -> int:
        if n < 2:
            return n  # Return n if n is 0 or 1
        trib = [0, 1, 1]  # Initialize tribonacci sequence        
        # Generate tribonacci sequence up to n
        for i in range(3, n + 1):
            next_val = trib[0] + trib[1] + trib[2]  # Calculate next value
            trib[0], trib[1], trib[2] = trib[1], trib[2], next_val  # Update tribonacci sequence        
        return trib[2]  # Return the nth tribonacci number
