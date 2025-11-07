# https://leetcode.com/problems/maximize-the-minimum-powered-city/

# Example 1:
# Input: stations = [1,2,4,5,0], r = 1, k = 2
# Output: 5
# Explanation: 
# One of the optimal ways is to install both the power stations at city 1. 
# So stations will become [1,4,4,5,0].
# - City 0 is provided by 1 + 4 = 5 power stations.
# - City 1 is provided by 1 + 4 + 4 = 9 power stations.
# - City 2 is provided by 4 + 4 + 5 = 13 power stations.
# - City 3 is provided by 5 + 4 = 9 power stations.
# - City 4 is provided by 5 + 0 = 5 power stations.
# So the minimum power of a city is 5.
# Since it is not possible to obtain a larger power, we return 5.

from itertools import accumulate

class Solution:
    def maxPower(self, stations, r, k):
        n = len(stations)
        df = [0] * (n + 5)
        
        # Build difference array for power coverage
        for i, j in enumerate(stations):
            df[max(0, i - r)] += j
            df[min(n - 1, i + r) + 1] -= j
        
        # Binary search bounds
        lo, hi = min(accumulate(df[:n])), 2 * 10**10

        def check(mid):
            # Verify if all cities can reach at least 'mid' power
            diff = df[:]
            cur, cnt = 0, 0
            for i in range(n):
                cur += diff[i]
                if cur < mid:
                    need = mid - cur
                    cnt += need
                    if cnt > k:  # Exceeds allowed boosts
                        return False
                    cur = mid
                    diff[min(n - 1, i + 2 * r) + 1] -= need  # Limit added power range
            return True

        # Binary search for max possible minimum power
        while lo < hi:
            mid = (lo + hi + 1) >> 1
            if check(mid):
                lo = mid
            else:
                hi = mid - 1

        return lo
