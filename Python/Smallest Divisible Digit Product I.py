# https://leetcode.com/problems/smallest-divisible-digit-product-i/

# Example 1:
# Input: n = 10, t = 2
# Output: 10
# Explanation:
# The digit product of 10 is 0, which is divisible by 2, making it the smallest number greater than or equal to 10 that satisfies the condition.

class Solution:
    def smallestNumber(self, n: int, t: int) -> int:

        # Keep checking numbers starting from n
        while True:

            # Compute the product of the digits
            product = 1
            x = n

            while x > 0:
                product *= x % 10
                x //= 10

            # If the digit product is divisible by t,
            # this is the required smallest number.
            if product % t == 0:
                return n

            # Otherwise, check the next number.
            n += 1