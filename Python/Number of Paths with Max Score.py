# https://leetcode.com/problems/number-of-paths-with-max-score/

# Example 1:
# Input: board = ["E23","2X2","12S"]
# Output: [7,1]

from typing import List

class Solution:
    def pathsWithMaxScore(self, board: List[str]) -> List[int]:
        MOD = 10**9 + 7
        n = len(board)

        # score[c] = maximum score reachable from the row below
        score = [-1] * (n + 1)

        # ways[c] = number of ways to achieve score[c]
        ways = [0] * (n + 1)

        # Process rows from bottom to top
        for r in range(n - 1, -1, -1):

            # DP arrays for the current row
            new_score = [-1] * (n + 1)
            new_ways = [0] * (n + 1)

            # Process columns from right to left
            for c in range(n - 1, -1, -1):

                # Cannot step on an obstacle
                if board[r][c] == "X":
                    continue

                # Starting position ('S')
                if board[r][c] == "S":
                    new_score[c] = 0
                    new_ways[c] = 1
                    continue

                # Best score among the three possible moves:
                # 1. Down      -> score[c]
                # 2. Right     -> new_score[c + 1]
                # 3. Diagonal  -> score[c + 1]
                best = max(
                    score[c],
                    new_score[c + 1],
                    score[c + 1]
                )

                # No valid path reaches this cell
                if best == -1:
                    continue

                # Count the number of ways that achieve 'best'
                cnt = 0

                if score[c] == best:
                    cnt += ways[c]

                if new_score[c + 1] == best:
                    cnt += new_ways[c + 1]

                if score[c + 1] == best:
                    cnt += ways[c + 1]

                # Cell value:
                # 'E' contributes 0, digits contribute their value
                val = 0 if board[r][c] == "E" else int(board[r][c])

                # Maximum score obtainable from this cell
                new_score[c] = best + val

                # Number of maximum-score paths
                new_ways[c] = cnt % MOD

            # Move current row into previous-row DP
            score = new_score
            ways = new_ways

        # No valid path from 'S' to 'E'
        if score[0] == -1:
            return [0, 0]

        # Maximum score and number of such paths
        return [score[0], ways[0]]