# https://leetcode.com/problems/find-the-count-of-good-integers/

# Example 1:
# Input: n = 3, k = 5
# Output: 27
# Explanation:
# Some of the good integers are:
# 551 because it can be rearranged to form 515.
# 525 because it is already k-palindromic.

from collections import Counter
from math import factorial, prod

class Solution:
    def countGoodIntegers(self, n: int, k: int) -> int:
        # Special case for 1-digit numbers
        if n == 1:
            # Count how many 1-digit numbers are divisible by k
            return sum(num % k == 0 for num in range(1, 10))

        # Generate half-length parts of palindromes
        # Example: for n=4, generate "10" to "99" which gives palindromes like "1001", "1221", etc.
        part_pals = [str(num) for num in range(10**((n // 2) - 1), 10**(n // 2))]

        k_pals = []

        # Generate all valid palindromes of length n
        if n % 2 == 0:
            # Even-length palindrome: just mirror the first half
            k_pals = [num + num[::-1] for num in part_pals]
        else:
            # Odd-length palindrome: insert a middle digit from 0-9
            for mid in range(10):
                k_pals.extend([num + str(mid) + num[::-1] for num in part_pals])

        # Filter palindromes divisible by k
        k_pals = [p for p in k_pals if int(p) % k == 0]

        # Create a set of unique sorted digit patterns for valid palindromes
        perms = set(''.join(sorted(pal)) for pal in k_pals)

        cnt = 0  # To store the total valid permutations

        for p in perms:
            freqs = Counter(p)  # Count digit frequency

            # Compute the number of permutations of this digit pattern
            # (n - freqs['0']) gives the number of digits excluding leading 0
            # factorial(n - 1) is used to ensure the first digit is not 0
            # Divide by factorials of each digit count to avoid overcounting duplicates
            cnt += ((n - freqs.get('0', 0)) * factorial(n - 1)) // prod(map(factorial, freqs.values()))

        return cnt
