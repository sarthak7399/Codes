# https://leetcode.com/problems/unique-3-digit-even-numbers/

# Example 1:
# Input: digits = [1,2,3,4]
# Output: 12
# Explanation: The 12 distinct 3-digit even numbers that can be formed are 124, 132, 134, 142, 214, 234, 312, 314, 324, 342, 412, and 432. Note that 222 cannot be formed because there is only 1 copy of the digit 2.

class Solution:
    def totalNumbers(self, digits):
        # Get the total number of available digits.
        n = len(digits)

        # Store unique three-digit even numbers.
        # A set avoids counting duplicate numbers when the input
        # contains repeated digits.
        seen = set()

        # Choose the digit for the hundreds place.
        for h in range(n):

            # A three-digit number cannot start with 0.
            if digits[h] == 0:
                continue

            # Choose the digit for the tens place.
            for t in range(n):

                # The same digit position cannot be used twice.
                if t == h:
                    continue

                # Choose the digit for the units place.
                for u in range(n):

                    # All three chosen positions must be different.
                    if u == h or u == t:
                        continue

                    # The units digit must be even for the complete
                    # three-digit number to be even.
                    if digits[u] % 2 != 0:
                        continue

                    # Form the three-digit number.
                    num = (
                        digits[h] * 100
                        + digits[t] * 10
                        + digits[u]
                    )

                    # Add the number to the set of unique valid numbers.
                    seen.add(num)

        # Return the number of distinct three-digit even numbers formed.
        return len(seen)