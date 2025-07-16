# https://leetcode.com/problems/max-difference-you-can-get-from-changing-an-integer/

# Example 1:
# Input: num = 555
# Output: 888
# Explanation: The first time pick x = 5 and y = 9 and store the new integer in a.
# The second time pick x = 5 and y = 1 and store the new integer in b.
# We have now a = 999 and b = 111 and max difference = 888

import math

class Solution:
    def create_high(self, num, place_value):
        """
        Creates the largest possible number by replacing a chosen digit (other than 9) 
        with 9 throughout the number.
        """
        result = 0
        replace_digit = -1  # First digit to replace, initialized to invalid
        while place_value > 0:
            current_digit = num // place_value

            # Select first non-9 digit to be replaced
            if replace_digit == -1 and current_digit != 9:
                replace_digit = current_digit

            # If this digit is the one selected, replace it with 9
            if current_digit == replace_digit:
                result = result * 10 + 9
            else:
                result = result * 10 + current_digit

            num %= place_value
            place_value //= 10

        return result

    def create_low(self, num, place_value):
        """
        Creates the smallest possible number by replacing a chosen digit (other than 1 or 0) 
        with 0 (or 1 if leading digit), aiming to minimize the value.
        """
        result = 0
        replace_digit = -1  # First digit to replace
        is_leading_one = 0  # 0 = undecided, 1 = leading 1 found, -1 = otherwise

        while place_value > 0:
            current_digit = num // place_value

            # Check the very first digit
            if is_leading_one == 0:
                if current_digit == 1:
                    is_leading_one = 1
                else:
                    is_leading_one = -1

            # Choose the first non-zero and non-one digit to replace
            if current_digit != 1 and replace_digit == -1 and current_digit != 0:
                replace_digit = current_digit

            # If it's the digit to be replaced, replace it with 0 (or 1 if leading digit)
            if current_digit == replace_digit:
                result = result * 10 + (0 if is_leading_one == 1 else 1)
            else:
                result = result * 10 + current_digit

            num %= place_value
            place_value //= 10

        return result

    def maxDiff(self, num: int) -> int:
        """
        Main function: returns the maximum difference between two numbers
        that can be formed by replacing digits in `num` with other digits.
        """
        num_digits = int(math.log10(num)) + 1
        highest_place = 10 ** (num_digits - 1)
        high = self.create_high(num, highest_place)
        low = self.create_low(num, highest_place)
        return high - low
