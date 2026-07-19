# https://leetcode.com/problems/four-divisors/

# Example 1:
# Input: nums = [21,4,7]
# Output: 32
# Explanation: 
# 21 has 4 divisors: 1, 3, 7, 21
# 4 has 3 divisors: 1, 2, 4
# 7 has 2 divisors: 1, 7
# The answer is the sum of divisors of 21 only.

import math

class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        div_sum = 0  # Final sum of divisors for valid numbers

        for i in nums:
            div_count = 0  # Count of divisors of i
            in_sum = 0     # Sum of divisors of i

            # Check divisors only up to sqrt(i)
            for divisor in range(1, int(math.sqrt(i)) + 1):
                if i % divisor == 0:
                    other = i // divisor  # Paired divisor

                    if divisor == other:
                        # Perfect square contributes only one divisor
                        div_count += 1
                        in_sum += divisor
                    else:
                        # Pair of distinct divisors
                        div_count += 2
                        in_sum += divisor + other

                    # Early exit if more than 4 divisors found
                    if div_count > 4:
                        break

            # If exactly 4 divisors, add their sum
            if div_count == 4:
                div_sum += in_sum

        return div_sum
