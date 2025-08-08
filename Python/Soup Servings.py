# https://leetcode.com/problems/soup-servings/

# Example 1:
# Input: n = 50
# Output: 0.62500
# Explanation: 
# If we perform either of the first two serving operations, soup A will become empty first.
# If we perform the third operation, A and B will become empty at the same time.
# If we perform the fourth operation, B will become empty first.
# So the total probability of A becoming empty first plus half the probability that A and B become empty at the same time, is 0.25 * (1 + 1 + 0.5 + 0) = 0.625.

from functools import cache

class Solution:
    def soupServings(self, n: int) -> float:
        # Optimization: For large n, probability approaches 1
        # If n > 50000 ml, return 1.0 directly without simulation
        if n > 50000:
            return 1.0

        @cache  # Memoization to avoid recalculating the same state
        def dfs(A, B):
            """
            A and B represent the remaining servings of soup A and soup B,
            measured in units of 25 ml (to reduce state space).
            Returns the probability that soup A will become empty first
            plus half the probability that both become empty at the same time.
            """

            # Case 1: Soup A is empty, Soup B still has soup → Probability = 1
            if A <= 0 and B > 0:
                return 1

            # Case 2: Both A and B are empty → Probability = 0.5
            if A <= 0 and B <= 0:
                return 0.5

            # Case 3: Soup A still has soup, Soup B is empty → Probability = 0
            if A > 0 and B <= 0:
                return 0

            # Case 4: Both soups have soup left
            # Four possible serving operations, each with equal probability (0.25)
            return 0.25 * (
                dfs(A - 4, B) +       # Serve 100 ml A, 0 ml B
                dfs(A - 3, B - 1) +   # Serve 75 ml A, 25 ml B
                dfs(A - 2, B - 2) +   # Serve 50 ml A, 50 ml B
                dfs(A - 1, B - 3)     # Serve 25 ml A, 75 ml B
            )

        # Convert ml to "units" of 25 ml to simplify states
        N = (n + 24) // 25

        # Start recursion with both soups full
        return dfs(N, N)
