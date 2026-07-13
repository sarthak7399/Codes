# https://leetcode.com/problems/sequential-digits/

# Example 1:
# Input: low = 100, high = 300
# Output: [123,234]

from typing import List

class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        # Stores all valid sequential digit numbers
        ans = []

        # Base string containing consecutive digits
        s = "123456789"

        # Convert bounds to strings to determine the digit lengths
        l = str(low)
        h = str(high)

        # Generate sequential numbers of every possible length
        for length in range(len(l), len(h) + 1):

            # Starting position of the substring
            for start in range(0, 10 - length):

                # Form the sequential number
                num = int(s[start:start + length])

                # Keep only numbers within the required range
                if low <= num <= high:
                    ans.append(num)

        return ans