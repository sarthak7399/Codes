# https://leetcode.com/problems/fraction-to-recurring-decimal/

# Example 1:
# Input: numerator = 1, denominator = 2
# Output: "0.5"

class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        # Edge case: if numerator is 0 → result is "0"
        if numerator == 0:
            return "0"

        fraction = []

        # Handle negative result: add '-' if signs differ
        if (numerator < 0) ^ (denominator < 0):
            fraction.append("-")

        # Work with absolute values
        dividend = abs(numerator)
        divisor = abs(denominator)

        # Append the integer part of the division
        fraction.append(str(dividend // divisor))

        # Find remainder after integer division
        remainder = dividend % divisor

        # If no remainder, return integer result directly
        if remainder == 0:
            return "".join(fraction)

        # Otherwise, process fractional part
        fraction.append(".")

        # Dictionary to store remainder positions (for detecting repeating cycles)
        map_dict = {}

        while remainder != 0:
            # If remainder already seen → repeating cycle detected
            if remainder in map_dict:
                # Insert "(" at the index where the remainder first appeared
                fraction.insert(map_dict[remainder], "(")
                # Append ")" at the end
                fraction.append(")")
                break

            # Store current remainder position in result string
            map_dict[remainder] = len(fraction)

            # Multiply remainder by 10 (simulate long division)
            remainder *= 10

            # Append quotient digit
            fraction.append(str(remainder // divisor))

            # Update remainder
            remainder %= divisor

        return "".join(fraction)
