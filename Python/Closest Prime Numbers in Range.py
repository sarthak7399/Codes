# https://leetcode.com/problems/closest-prime-numbers-in-range/

# Example 1:
# Input: left = 10, right = 19
# Output: [11,13]
# Explanation: The prime numbers between 10 and 19 are 11, 13, 17, and 19.
# The closest gap between any pair is 2, which can be achieved by [11,13] or [17,19].
# Since 11 is smaller than 17, we return the first pair.

from ast import List
class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        if left > right:
            return [-1, -1]

        # Step 1: Sieve of Eratosthenes
        is_prime = [True] * (right + 1)
        is_prime[0] = is_prime[1] = False

        for i in range(2, int(right ** 0.5) + 1):
            if is_prime[i]:
                for j in range(i * i, right + 1, i):
                    is_prime[j] = False

        # Step 2: Collect primes in range
        primes = [i for i in range(left, right + 1) if is_prime[i]]

        # Step 3: If fewer than 2 primes exist, return [-1, -1]
        if len(primes) < 2:
            return [-1, -1]

        # Step 4: Find the closest prime pair
        min_diff, num1, num2 = float('inf'), -1, -1
        for i in range(1, len(primes)):
            diff = primes[i] - primes[i - 1]
            if diff < min_diff:
                min_diff = diff
                num1, num2 = primes[i - 1], primes[i]

        return [num1, num2]