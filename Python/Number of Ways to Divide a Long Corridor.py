# https://leetcode.com/problems/number-of-ways-to-divide-a-long-corridor/

# Example 1:
# Input: corridor = "SSPPSPS"
# Output: 3
# Explanation: There are 3 different ways to divide the corridor.
# The black bars in the above image indicate the two room dividers already installed.
# Note that in each of the ways, each section has exactly two seats.

class Solution(object):
    def numberOfWays(self, corridor):
        mod = 10**9 + 7

        # Count total seats
        s = corridor.count('S')
        # If no seats or odd number of seats, impossible
        if not s or s % 2:
            return 0

        ans = 1      # Final number of ways
        cnt = 0      # Seats seen so far
        p = 0        # Plants between a valid seat pair

        for ch in corridor:
            if ch == 'S':
                cnt += 1
                # When starting a new seat pair after the first
                if cnt > 2 and cnt % 2 == 1:
                    ans = ans * (p + 1) % mod
                    p = 0
            # Count plants only after completing a seat pair
            elif cnt and cnt % 2 == 0:
                p += 1

        return ans
