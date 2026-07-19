# https://leetcode.com/problems/power-of-three/

# Example 1:
# Input: n = 27
# Output: true
# Explanation: 27 = 3^3


class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        # Step 1: Any non-positive number cannot be a power of three
        if n <= 0:
            return False

        count1 = 0  # Counts how many '1's appear in base-3 representation of n

        # Step 2: Convert n to base-3 representation while checking digits
        while n > 0:
            digit = n % 3  # Get the least significant digit in base-3

            if digit == 1:
                count1 += 1
                # More than one '1' means it cannot be a pure power of 3
                if count1 > 1:
                    return False

            if digit == 2:
                # If a digit is '2', it can't be a power of 3
                return False

            n //= 3  # Move to the next digit (divide by 3)

        # Step 3: A power of three in base-3 has exactly one '1' and rest '0's
        return count1 == 1
