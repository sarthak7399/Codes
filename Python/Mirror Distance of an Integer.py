# https://leetcode.com/problems/mirror-distance-of-an-integer/

# Example 1:
# Input: n = 25
# Output: 27
# Explanation:
# reverse(25) = 52.
# Thus, the answer is abs(25 - 52) = 27.

class Solution:
    def rev(self, n: int) -> int:
        a = 0  # Variable to store the reversed number
        
        # Reverse the digits of n
        while n > 0:
            a = a * 10 + (n % 10)  # Append last digit of n to 'a'
            n //= 10               # Remove last digit from n
        
        return a  # Return reversed number

    def mirrorDistance(self, n: int) -> int:
        m = self.rev(n)  # Get the reversed (mirror) number
        
        # Return absolute difference between original and reversed number
        return abs(m - n)