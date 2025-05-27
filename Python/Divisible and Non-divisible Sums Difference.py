# https://leetcode.com/problems/divisible-and-non-divisible-sums-difference/

# Example 1:
# Input: n = 10, m = 3
# Output: 19
# Explanation: In the given example:
# - Integers in the range [1, 10] that are not divisible by 3 are [1,2,4,5,7,8,10], num1 is the sum of those integers = 37.
# - Integers in the range [1, 10] that are divisible by 3 are [3,6,9], num2 is the sum of those integers = 18.
# We return 37 - 18 = 19 as the answer.

class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        # Calculate the sum of first n natural numbers using formula: n * (n + 1) / 2
        total_sum = n * (n + 1) // 2

        # Count how many numbers from 1 to n are divisible by m
        divisible_count = n // m

        # Sum of all numbers divisible by m from 1 to n:
        # It forms an arithmetic progression: m, 2m, 3m, ..., divisible_count * m
        # Sum = m * (1 + 2 + ... + divisible_count) = m * divisible_count * (divisible_count + 1) / 2
        divisible_sum = m * divisible_count * (divisible_count + 1) // 2

        # Return the difference between:
        # - the sum of numbers *not* divisible by m
        # - the sum of numbers divisible by m
        # Which is equivalent to: (total_sum - divisible_sum) - divisible_sum = total_sum - 2 * divisible_sum
        return total_sum - 2 * divisible_sum
