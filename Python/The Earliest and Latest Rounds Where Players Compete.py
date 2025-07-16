# https://leetcode.com/problems/the-earliest-and-latest-rounds-where-players-compete/

# Example 1:
# Input: n = 11, firstPlayer = 2, secondPlayer = 4
# Output: [3,4]
# Explanation:
# One possible scenario which leads to the earliest round number:
# First round: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11
# Second round: 2, 3, 4, 5, 6, 11
# Third round: 2, 3, 4
# One possible scenario which leads to the latest round number:
# First round: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11
# Second round: 1, 2, 3, 4, 5, 6
# Third round: 1, 2, 4
# Fourth round: 2, 4

class Solution:
    def earliestAndLatest(self, n: int, firstPlayer: int, secondPlayer: int) -> list[int]:
        def dfs(n, p1, p2):
            # Step 1: Normalize
            if p1 + p2 == n + 1:
                return (1, 1)
            if p1 > p2:
                p1, p2 = p2, p1
            if n <= 4:
                return (2, 2)

            m = (n + 1) // 2
            minR, maxR = float('inf'), float('-inf')

            # Step 2: Use symmetry
            if p1 - 1 > n - p2:
                t = n + 1 - p1
                p1 = n + 1 - p2
                p2 = t

            # Step 3: Simulate possibilities
            if p2 * 2 <= n + 1:
                a = p1 - 1
                b = p2 - p1 - 1

                for i in range(a + 1):
                    for j in range(b + 1):
                        r1, r2 = dfs(m, i + 1, i + j + 2)
                        minR = min(minR, r1 + 1)
                        maxR = max(maxR, r2 + 1)
            else:
                p4 = n + 1 - p2
                a = p1 - 1
                b = p4 - p1 - 1
                c = p2 - p4 - 1

                for i in range(a + 1):
                    for j in range(b + 1):
                        offset = i + j + 1 + (c + 1) // 2 + 1
                        r1, r2 = dfs(m, i + 1, offset)
                        minR = min(minR, r1 + 1)
                        maxR = max(maxR, r2 + 1)

            # Step 4: Return earliest and latest round
            return (minR, maxR)

        return list(dfs(n, firstPlayer, secondPlayer))