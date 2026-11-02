# https://leetcode.com/problems/kth-smallest-amount-with-single-denomination-combination/

# Example 1:
# Input: coins = [3,6,9], k = 3
# Output: 9
# Explanation: The given coins can make the following amounts:
# Coin 3 produces multiples of 3: 3, 6, 9, 12, 15, etc.
# Coin 6 produces multiples of 6: 6, 12, 18, 24, etc.
# Coin 9 produces multiples of 9: 9, 18, 27, 36, etc.
# All of the coins combined produce: 3, 6, 9, 12, 15, etc.

from typing import List
from math import gcd

class Solution:

    def findKthSmallest(self, coins: List[int], k: int) -> int:
        # Sort the coin values so smaller divisors are processed first.
        coins.sort()

        # Remove redundant coin values.
        # If a coin is divisible by an already selected smaller coin,
        # every multiple of this coin is already covered.
        useful = []

        for coin in coins:
            redundant = False

            for prev in useful:
                if coin % prev == 0:
                    redundant = True
                    break

            if not redundant:
                useful.append(coin)

        # The answer is at least 1.
        low = 1

        # In the worst case, the k-th number can be bounded by
        # the smallest useful coin multiplied by k.
        high = useful[0] * k

        m = len(useful)

        # Total non-empty subsets of useful coins.
        total_masks = 1 << m

        # Precompute the LCM for every subset of coins.
        lcms = [1] * total_masks

        # Precompute the inclusion-exclusion sign for every subset.
        signs = [1] * total_masks

        for mask in range(1, total_masks):
            current_lcm = 1
            bits = 0

            # Build the LCM of all coins included in this subset.
            for i in range(m):
                if mask & (1 << i):

                    # Calculate LCM safely using:
                    # lcm(a, b) = a / gcd(a, b) * b
                    current_lcm //= gcd(current_lcm, useful[i])

                    # Avoid unnecessary overflow and mark this LCM
                    # as larger than the maximum possible answer.
                    if current_lcm > high // useful[i]:
                        current_lcm = high + 1
                        break

                    current_lcm *= useful[i]
                    bits += 1

            lcms[mask] = current_lcm

            # Inclusion-exclusion:
            # odd-sized subsets are added, even-sized subsets subtracted.
            signs[mask] = 1 if bits % 2 == 1 else -1

        def count(x: int) -> int:
            # Count how many positive integers <= x are divisible
            # by at least one useful coin using inclusion-exclusion.
            result = 0

            for mask in range(1, total_masks):
                if lcms[mask] <= x:
                    result += signs[mask] * (x // lcms[mask])

            return result

        # Binary search for the smallest number x such that
        # at least k valid numbers are less than or equal to x.
        while low < high:
            mid = low + (high - low) // 2

            if count(mid) >= k:
                high = mid
            else:
                low = mid + 1

        # low is the k-th smallest valid number.
        return low