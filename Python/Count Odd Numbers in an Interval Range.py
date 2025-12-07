# https://leetcode.com/problems/count-odd-numbers-in-an-interval-range/

# Example 1:
# Input: low = 3, high = 7
# Output: 3
# Explanation: The odd numbers between 3 and 7 are [3,5,7].

class Solution:
    def countOdds(self, low: int, high: int) -> int:
        # Count odds ≤ high minus odds < low
        return (high + 1) // 2 - (low // 2)
