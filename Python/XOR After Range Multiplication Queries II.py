# https://leetcode.com/problems/xor-after-range-multiplication-queries-ii/

# Example 1:
# Input: nums = [1,1,1], queries = [[0,2,1,4]]
# Output: 4
# Explanation:
# A single query [0, 2, 1, 4] multiplies every element from index 0 through index 2 by 4.
# The array changes from [1, 1, 1] to [4, 4, 4].
# The XOR of all elements is 4 ^ 4 ^ 4 = 4.

from collections import defaultdict
import math
from typing import List

class Solution:
    def xorAfterQueries(self, nums: List[int], queries: List[List[int]]) -> int:
        MOD = 10**9 + 7  # Modulo value for large numbers
        n = len(nums)

        # Edge case: if array is empty
        if n == 0:
            return 0

        # Square root decomposition threshold
        square = int(math.sqrt(n)) + 1

        # Dictionary to store queries with small step size (k < square)
        small = defaultdict(list) 

        # Process each query
        for l, r, k, v in queries:
            if k >= square:
                # For large k, directly update elements (brute force)
                idx = l
                while idx <= r:
                    nums[idx] = (nums[idx] * v) % MOD
                    idx += k
            else:
                # For small k, store queries for later batch processing
                small[k].append((l, r, v))

        # Array to store multiplication factors for each index
        factors = [1] * n

        # Process all small k queries using optimized approach
        for k, qlist in small.items():
            # Events array for each remainder class (mod k)
            events = [[] for _ in range(k)]
            
            # Build events (range updates using prefix technique)
            for l, r, v in qlist:
                res = l % k  # Residue class
                step = (r - l) // k
                last = l + step * k  # Last valid index in this progression
                
                # Start event: multiply by v
                events[res].append((l, v))  
                
                # End event: multiply by modular inverse of v
                end_idx = last + k
                if end_idx < n:              
                    inv_v = pow(v, MOD - 2, MOD)  # Modular inverse
                    events[res].append((end_idx, inv_v))
            
            # Apply events for each residue class
            for res in range(k):
                ev = events[res]
                if not ev:
                    continue

                ev.sort()  # Sort events by index
                cur = 1    # Current multiplication factor
                ptr = 0
                m = len(ev)

                # Traverse indices with step k
                i = res
                while i < n:
                    # Apply all events occurring at index i
                    while ptr < m and ev[ptr][0] == i:
                        cur = (cur * ev[ptr][1]) % MOD
                        ptr += 1

                    # Store cumulative factor
                    factors[i] = (factors[i] * cur) % MOD
                    i += k
        
        # Apply all accumulated factors to nums
        for i in range(n):
            nums[i] = (nums[i] * factors[i]) % MOD
        
        # Compute XOR of final array
        ans = 0
        for x in nums:
            ans ^= x

        return ans