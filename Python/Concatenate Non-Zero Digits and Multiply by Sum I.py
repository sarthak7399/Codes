# https://leetcode.com/problems/concatenate-non-zero-digits-and-multiply-by-sum-i/

# Example 1:
# Input: n = 10203004
# Output: 12340
# Explanation:
# The non-zero digits are 1, 2, 3, and 4. Thus, x = 1234.
# The sum of digits is sum = 1 + 2 + 3 + 4 = 10.
# Therefore, the answer is x * sum = 1234 * 10 = 12340.

class Solution:
    def sumAndMultiply(self, n: int) -> int:
        # Number formed after removing all zero digits
        x = 0

        # Sum of all non-zero digits
        digit_sum = 0

        # Find the highest power of 10 less than or equal to n
        divisor = 1
        while n // divisor >= 10:
            divisor *= 10

        # Process digits from left to right
        while divisor > 0:
            # Extract the current most significant digit
            digit = n // divisor

            # Remove the extracted digit from n
            n %= divisor

            # Ignore zero digits
            if digit != 0:
                # Build the number after removing zeros
                x = x * 10 + digit

                # Add the digit to the running sum
                digit_sum += digit

            # Move to the next digit
            divisor //= 10

        # Return:
        # (number after removing zeros) × (sum of non-zero digits)
        return x * digit_sum