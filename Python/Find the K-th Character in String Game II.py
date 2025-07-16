# https://leetcode.com/problems/find-the-k-th-character-in-string-game-ii/

# Example 1:
# Input: k = 5, operations = [0,0,0]
# Output: "a"
# Explanation:
# Initially, word == "a". Alice performs the three operations as follows:
# Appends "a" to "a", word becomes "aa".
# Appends "aa" to "aa", word becomes "aaaa".
# Appends "aaaa" to "aaaa", word becomes "aaaaaaaa".

from typing import List

class Solution:
    def kthCharacter(self, k: int, operations: List[int]) -> str:
        # Solution 4: One-liner 
        return chr((sum(o for o, b in zip(operations, bin(k-1)[:1:-1])
                    if b=='1') % 26) + 97)
        # Time:  O(log k)
        # Space: O(log k)

        # Solution 3: Bit Strip (removes largest power of two ≤ k)
        shifts = 0
        while k != 1:
            i = k.bit_length() - 1
            if (1 << i) == k:
                i -= 1
            k -= 1 << i
            if operations[i]:   
                shifts += 1
        return chr((shifts % 26) + 97)
        # Time:  O(log k)
        # Space: O(1)


        # Solution 2: Single Pass w/ Bit-Shift (more efficient)
        shifts, n = 0, len(operations) + 1
        for i in range(n - 1, 0, -1):
            half = 1 << (i - 1)
            if k > half:
                k -= half
                if operations[i - 1] == 1:
                    shifts += 1
        return chr((shifts % 26) + 97)
        # Time:  O(n)
        # Space: O(1)

        # Solution 1: Precompute & Trasverse Reversed (first attempt)
        n = len(operations) + 1
        lens = [1] * n
        for i in range(1, n):
            lens[i] = lens[i - 1] * 2
        shifts = 0
        for i in range(n - 1, 0, -1):
            if k > lens[i - 1]:
                k -= lens[i - 1]
                if operations[i - 1] == 1:
                    shifts += 1
        return chr((shifts % 26) + 97)
        # Time:  O(n)
        # Space: O(n)