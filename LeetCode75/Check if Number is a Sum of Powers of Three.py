# https://leetcode.com/problems/check-if-number-is-a-sum-of-powers-of-three/

# Example 1:
# Input: n = 12
# Output: true
# Explanation: 12 = 31 + 32

class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        while n > 0:
            if n % 3 == 2:  # If any digit in base-3 representation is 2, return False
                return False
            n //= 3  # Reduce n by dividing it by 3
        
        return True  # If only 0s and 1s were found, return True
