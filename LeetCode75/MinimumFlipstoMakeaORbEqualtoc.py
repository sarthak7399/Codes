# https://leetcode.com/problems/minimum-flips-to-make-a-or-b-equal-to-c/description/?envType=study-plan-v2&envId=leetcode-75&__cf_chl_tk=HyYodGpGHXln3lCBwgSgMz5Mt5F17V1WwKfbVKqTu9I-1706898763-0-gaNycGzNElA

# Example 1:
# Input: a = 2, b = 6, c = 5
# Output: 3
# Explanation: After flips a = 1 , b = 4 , c = 5 such that (a OR b == c)

# Example 2:
# Input: a = 4, b = 2, c = 7
# Output: 1

class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        flips = 0  # Initialize the count of flips needed
        for i in range(31):     # Iterate through the bits of c (up to the 31st bit)
            if (c >> i) & 1:                # i'th bit of c is 1    
                flips += ((a >> i) & 1) == 0 and ((b >> i) & 1) == 0        # If i'th bit of a and b are both 0, it needs to be flipped
            else:       # i'th bit of c is 0
                flips += (a >> i) & 1       # If i'th bit of a is 1, it needs to be flipped
                flips += (b >> i) & 1       # If i'th bit of b is 1, it needs to be flipped
        return flips 
