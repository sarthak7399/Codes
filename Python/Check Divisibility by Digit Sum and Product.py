# https://leetcode.com/problems/check-divisibility-by-digit-sum-and-product/

# Example 1:
# Input: n = 99
# Output: true
# Explanation:
# Since 99 is divisible by the sum (9 + 9 = 18) plus product (9 * 9 = 81) of its digits (total 99), the output is true.

class Solution:
    def checkDivisibility(self, n: int) -> bool:
        # Store the original number since n will be modified
        # while extracting its digits.
        original = n

        # Initialise variables to store the sum and product of digits.
        digit_sum = 0
        digit_product = 1

        # Extract each digit from right to left.
        while n > 0:
            digit = n % 10

            # Add the current digit to the digit sum.
            digit_sum += digit

            # Multiply the current digit into the digit product.
            digit_product *= digit

            # Remove the last digit.
            n //= 10

        # Calculate the divisor as the sum of digit sum
        # and digit product.
        divisor = digit_sum + digit_product

        # Return True if the original number is divisible
        # by the calculated divisor.
        return original % divisor == 0