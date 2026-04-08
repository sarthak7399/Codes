# https://leetcode.com/problems/xor-after-range-multiplication-queries-i/

# Example 1:
# Input: nums = [1,1,1], queries = [[0,2,1,4]]
# Output: 4
# Explanation:
# A single query [0, 2, 1, 4] multiplies every element from index 0 through index 2 by 4.
# The array changes from [1, 1, 1] to [4, 4, 4].
# The XOR of all elements is 4 ^ 4 ^ 4 = 4.

import math
from typing import List

class Solution:
    MOD = 10**9 + 7

    # -------- Fast modular exponentiation --------
    def modpow(self, a: int, e: int) -> int:
        r = 1
        a %= self.MOD

        # Binary exponentiation
        while e:
            if e & 1:
                r = (r * a) % self.MOD
            a = (a * a) % self.MOD
            e >>= 1

        return r

    def xorAfterQueries(self, nums: List[int], queries: List[List[int]]) -> int:
        n = len(nums)

        # Block size for sqrt decomposition
        B = int(math.sqrt(n)) + 1

        # events[k][rem] → list of (position, multiplier)
        # Used to handle small k efficiently
        events = [[] for _ in range(B + 1)]
        for k in range(1, B + 1):
            events[k] = [[] for _ in range(k)]

        # -------- Step 1: Process queries --------
        for l, r, k, v in queries:

            if k > B:
                # -------- Case 1: Large k --------
                # Directly update elements (few elements affected)
                i = l
                while i <= r:
                    nums[i] = (nums[i] * v) % self.MOD
                    i += k

            else:
                # -------- Case 2: Small k --------
                # Use event-based lazy updates

                rem = l % k  # group index

                # Convert to compressed index space
                start = (l - rem) // k
                end = (r - rem) // k

                # Add multiplication event at start
                events[k][rem].append((start, v))

                # Add inverse at end+1 to cancel effect (range update trick)
                maxT = (n - 1 - rem) // k
                if end + 1 <= maxT:
                    inv = self.modpow(v, self.MOD - 2)  # modular inverse
                    events[k][rem].append((end + 1, inv))

        # -------- Step 2: Apply events for small k --------
        for k in range(1, B + 1):
            for rem in range(k):

                ev = events[k][rem]
                if not ev:
                    continue

                # Sort events by position
                ev.sort()

                # -------- Compress events --------
                # Combine multiple updates at same position
                comp = []
                for t, val in ev:
                    if comp and comp[-1][0] == t:
                        comp[-1] = (t, comp[-1][1] * val % self.MOD)
                    else:
                        comp.append((t, val))

                # -------- Apply prefix multiplication --------
                cur = 1   # current multiplier
                ptr = 0   # pointer in compressed events
                t = 0     # compressed index
                idx = rem # actual index in nums

                while idx < n:

                    # Apply all events at this compressed index
                    while ptr < len(comp) and comp[ptr][0] == t:
                        cur = (cur * comp[ptr][1]) % self.MOD
                        ptr += 1

                    # Apply accumulated multiplier
                    nums[idx] = nums[idx] * cur % self.MOD

                    # Move to next index in this sequence
                    t += 1
                    idx += k

        # -------- Step 3: Compute final XOR --------
        ans = 0
        for x in nums:
            ans ^= x

        return ans