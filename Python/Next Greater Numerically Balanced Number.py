# https://leetcode.com/problems/next-greater-numerically-balanced-number/

# Example 2:
# Input: n = 1000
# Output: 1333
# Explanation: 
# 1333 is numerically balanced since:
# - The digit 1 occurs 1 time.
# - The digit 3 occurs 3 times. 
# It is also the smallest numerically balanced number strictly greater than 1000.
# Note that 1022 cannot be the answer because 0 appeared more than 0 times.

class Solution:
    def solve(self, x: int) -> bool:
        s = str(x)                  # Convert number to string to access digits easily
        vec = [0] * 10              # Frequency array for digits 0–9

        # Count occurrences of each digit
        for ch in s:
            vec[ord(ch) - 48] += 1  # ord('0') = 48, so this maps '0'–'9' to 0–9

        # Check if the number is "beautiful"
        for ch in s:
            c = ord(ch) - 48
            # A digit is invalid if it is 0 or its frequency doesn’t equal its value
            if c == 0 or vec[c] != c:
                return False
        return True

    def nextBeautifulNumber(self, n: int) -> int:
        i = n + 1                   # Start checking from the next number
        while True:
            # If current number is beautiful, return it
            if self.solve(i):
                return i
            i += 1                  # Otherwise, move to next number
