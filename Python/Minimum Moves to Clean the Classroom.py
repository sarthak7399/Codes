# https://leetcode.com/problems/minimum-moves-to-clean-the-classroom/

# Example 1:
# Input: classroom = ["S.", "XL"], energy = 2
# Output: 2
# Explanation:
# The student starts at cell (0, 0) with 2 units of energy.
# Since cell (1, 0) contains an obstacle 'X', the student cannot move directly downward.
# A valid sequence of moves to collect all litter is as follows:
# Move 1: From (0, 0) → (0, 1) with 1 unit of energy and 1 unit remaining.
# Move 2: From (0, 1) → (1, 1) to collect the litter 'L'.
# The student collects all the litter using 2 moves. Thus, the output is 2.

from typing import List
from collections import deque

class Solution:
    def minMoves(self, classroom: List[str], energy: int) -> int:
        # Get the dimensions of the classroom grid.
        m = len(classroom)
        n = len(classroom[0])

        # Assign a unique ID to every litter cell ('L').
        # This allows us to represent collected litter using a bitmask.
        id = [[-1] * n for _ in range(m)]

        k = 0
        sr = 0
        sc = 0

        # Find the starting position and assign IDs to all litter cells.
        for r in range(m):
            for c in range(n):
                if classroom[r][c] == 'S':
                    sr = r
                    sc = c
                elif classroom[r][c] == 'L':
                    id[r][c] = k
                    k += 1

        # If there is no litter to collect, no movement is required.
        if k == 0:
            return 0

        # When all k litter cells are collected, all k bits will be 1.
        total_mask = (1 << k) - 1

        # best[r][c][mask] stores the maximum remaining energy
        # with which we have reached (r, c) after collecting the
        # litter represented by 'mask'.
        #
        # A higher remaining energy is always better for the same
        # position and collected-litter state.
        best = [
            [
                [-1] * (1 << k)
                for _ in range(n)
            ]
            for _ in range(m)
        ]

        # BFS queue stores:
        # (row, column, collected_litter_mask, remaining_energy, moves)
        queue = deque()

        # Initially, we are at the starting cell with full energy
        # and have not collected any litter.
        best[sr][sc][0] = energy
        queue.append((sr, sc, 0, energy, 0))

        # Four possible movement directions.
        directions = [
            (-1, 0),
            (1, 0),
            (0, -1),
            (0, 1)
        ]

        # BFS guarantees that states are processed in increasing
        # order of number of moves.
        while queue:
            r, c, mask, e, moves = queue.popleft()

            # Try moving in each of the four directions.
            for dr, dc in directions:
                nr = r + dr
                nc = c + dc

                # Ignore positions outside the classroom.
                if nr < 0 or nr >= m or nc < 0 or nc >= n:
                    continue

                # 'X' represents an obstacle and cannot be entered.
                if classroom[nr][nc] == 'X':
                    continue

                # Moving to a neighbouring cell consumes one unit of energy.
                ne = e - 1

                # We cannot move if we have no energy remaining.
                if ne < 0:
                    continue

                # Initially, keep the same set of collected litter.
                nmask = mask

                # Reaching a recharge cell restores energy to its maximum.
                if classroom[nr][nc] == 'R':
                    ne = energy

                # If the new cell contains litter, mark it as collected
                # by setting its corresponding bit in the mask.
                if classroom[nr][nc] == 'L':
                    nmask |= 1 << id[nr][nc]

                # If all litter has now been collected, return the number
                # of moves. BFS ensures this is the minimum number of moves.
                if nmask == total_mask:
                    return moves + 1

                # If we have already reached this state with at least
                # as much remaining energy, there is no benefit in
                # exploring it again.
                if ne <= best[nr][nc][nmask]:
                    continue

                # Record the better remaining-energy state.
                best[nr][nc][nmask] = ne

                # Add the new state to the BFS queue.
                queue.append(
                    (nr, nc, nmask, ne, moves + 1)
                )

        # If all possible states are exhausted without collecting
        # all litter, the task is impossible.
        return -1