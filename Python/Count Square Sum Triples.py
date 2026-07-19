# https://leetcode.com/problems/count-square-sum-triples/

# Example 1:
# Input: n = 5
# Output: 2
# Explanation: The square triples are (3,4,5) and (4,3,5).

class Solution:
    def countTriples(self, n: int) -> int:
        cnt = 0
        # Try all a < b < n
        for a in range(1, n):
            for b in range(a + 1, n):
                c_sq = a*a + b*b
                c = int(c_sq**0.5)
                
                # Check if c is an integer ≤ n
                if c*c == c_sq and c <= n:
                    cnt += 2  # (a,b,c) and (b,a,c)
        return cnt
