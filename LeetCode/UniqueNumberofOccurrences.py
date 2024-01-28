# s://leetcode.com/problems/unique-number-of-occurrences/?envType=study-plan-v2&envId=leetcode-75

# Example 1:
# Input: arr = [1,2,2,1,1,3]
# Output: true
# Explanation: The value 1 has 3 occurrences, 2 has 2 and 3 has 1. No two values have the same number of occurrences.

# Example 2:
# Input: arr = [1,2]
# Output: false

from typing import List

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        freq = {}
        for x in arr:
            freq[x] = freq.get(x, 0) + 1    #If x is not already a key in freq, freq.get(x, 0) returns 0 (the default value) and then adds 1 to it. If x is already a key, it retrieves its current frequency and increments it by 1.

        return len(freq) == len(set(freq.values()))