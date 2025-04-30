# Example 1:

# Input: nums = [12,345,2,6,7896]
# Output: 2
# Explanation: 
# 12 contains 2 digits (even number of digits). 
# 345 contains 3 digits (odd number of digits). 
# 2 contains 1 digit (odd number of digits). 
# 6 contains 1 digit (odd number of digits). 
# 7896 contains 4 digits (even number of digits). 
# Therefore only 12 and 7896 contain an even number of digits.

from math import log10, floor
from typing import List

class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        count = 0  # Initialize a counter to keep track of numbers with even digits
        
        for x in nums:
            # Compute the number of digits in x using floor(log10(x)) + 1
            # log10(x) gives the number of digits minus one (in base 10)
            # floor ensures we get the integer part, and adding 1 gives the total digits
            digit_count = int(floor(log10(x)) + 1)

            # Check if the number of digits is even
            if digit_count % 2 == 0:
                count += 1  # Increment count if digit count is even
        
        return count  # Return the total count of numbers with even number of digits
