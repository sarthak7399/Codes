# https://leetcode.com/problems/minimum-operations-to-equalize-binary-string/

# Example 1:
# Input: s = "110", k = 1
# Output: 1
# Explanation:
# There is one '0' in s.
# Since k = 1, we can flip it directly in one operation.

class Solution:
    def minOperations(self, s: str, k: int) -> int:
        n = len(s)
        z = s.count('0')
        if z == 0:
            return 0

        if k == n:
            return 1 if z == n else -1

        # If k is even, parity of zeros can't change -> must start with even zeros to reach 0
        if (k % 2 == 0) and (z % 2 == 1):
            return -1

        o = n - z

        def ok(t: int) -> bool:
            total = t * k
            # parity condition: total ≡ z (mod 2)
            if (total & 1) != (z & 1):
                return False

            oddMax = t if (t & 1) else (t - 1)      # largest odd <= t
            evenMax = (t - 1) if (t & 1) else t     # largest even <= t
            if oddMax < 1:
                return False

            L = max(z, total - o * evenMax)
            R = min(z * oddMax, total)
            if L > R:
                return False

            # need F0 parity == z parity
            if (L & 1) != (z & 1):
                L += 1
            return L <= R

        # lower bound ceil(z/k)
        t = (z + k - 1) // k
        if t < 1:
            t = 1

        upper = 2 * n + 5

        if k % 2 == 1:
            # need t parity == z parity
            if (t & 1) != (z & 1):
                t += 1
            while t <= upper:
                if ok(t):
                    return t
                t += 2
        else:
            while t <= upper:
                if ok(t):
                    return t
                t += 1

        return -1