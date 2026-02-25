# https://leetcode.com/problems/sort-integers-by-the-number-of-1-bits/

# Example 1:
# Input: arr = [0,1,2,3,4,5,6,7,8]
# Output: [0,1,2,4,8,3,5,6,7]
# Explantion: [0] is the only integer with 0 bits.
# [1,2,4,8] all have 1 bit.
# [3,5,6] have 2 bits.
# [7] has 3 bits.
# The sorted array by bits is [0,1,2,4,8,3,5,6,7]

import collections
from typing import List

class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        # Dictionary:
        # key   -> number of set bits (1s in binary)
        # value -> list of numbers having that many set bits
        bitmap = collections.defaultdict(list)
        
        # Group numbers based on count of set bits
        for val in arr:
            bits = val.bit_count()   # built-in method to count 1s in binary
            bitmap[bits].append(val)
            
        ans = []
        
        # Process groups in increasing order of bit count
        for key in sorted(bitmap.keys()):
            # For same bit count, numbers must be sorted numerically
            for val in sorted(bitmap[key]):
                ans.append(val)
                
        return ans