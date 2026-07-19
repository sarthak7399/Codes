# https://leetcode.com/problems/minimum-operations-to-make-the-integer-zero/

# Example 1:
# Input: num1 = 3, num2 = -2
# Output: 3
# Explanation: We can make 3 equal to 0 with the following operations:
# - We choose i = 2 and subtract 22 + (-2) from 3, 3 - (4 + (-2)) = 1.
# - We choose i = 2 and subtract 22 + (-2) from 1, 1 - (4 + (-2)) = -1.
# - We choose i = 0 and subtract 20 + (-2) from -1, (-1) - (1 + (-2)) = 0.
# It can be proven, that 3 is the minimum number of operations that we need to perform.

class Solution:
    def makeTheIntegerZero(self, num1: int, num2: int) -> int:
        # If num1 is already 0, no operations needed
        if num1 == 0:
            return 0

        # Try all possible numbers of operations (t = number of steps taken)
        # Up to 60 is sufficient because 2^60 > 10^18 (covers typical constraints)
        for t in range(0, 61):  
            # After t operations, the value becomes s = num1 - t * num2
            s = num1 - t * num2

            # If result is negative, skip (not possible to reach 0 from here)
            if s < 0:
                continue

            # If s is smaller than t, impossible (need at least s >= t)
            if s < t:
                continue

            # Count number of 1s in the binary representation of s
            # This tells us the minimum number of powers of 2 needed to represent s
            ones = s.bit_count()

            # If we can distribute the sum into exactly t numbers (each >= 1),
            # then a valid solution is found
            if ones <= t:
                return t

        # If no valid t is found, return -1
        return -1
