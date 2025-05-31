# https://leetcode.com/problems/snakes-and-ladders/

# Example 1:
# Input: board = [[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,35,-1,-1,13,-1],[-1,-1,-1,-1,-1,-1],[-1,15,-1,-1,-1,-1]]
# Output: 4
# Explanation: 
# In the beginning, you start at square 1 (at row 5, column 0).
# You decide to move to square 2 and must take the ladder to square 15.
# You then decide to move to square 17 and must take the snake to square 13.
# You then decide to move to square 14 and must take the ladder to square 35.
# You then decide to move to square 36, ending the game.
# This is the lowest possible number of moves to reach the last square, so return 4.

from collections import deque

class Solution:
    def snakesAndLadders(self, board: list[list[int]]) -> int:
        n = len(board)  # Size of the board (n x n)

        def get_coordinates(pos: int) -> tuple[int, int]:
            """
            Convert a 1-based board position to (row, col) coordinates.
            The board is numbered in a zig-zag fashion.
            """
            r, c = divmod(pos - 1, n)  # Get row and col in 0-based indexing
            row = n - 1 - r  # Convert to board row from bottom up
            col = c if r % 2 == 0 else n - 1 - c  # Handle zigzag direction
            return row, col

        visited = set()  # To track visited cells and prevent cycles
        queue = deque([(1, 0)])  # Start BFS from square 1 with 0 moves

        while queue:
            pos, moves = queue.popleft()

            # Try all dice rolls from 1 to 6
            for i in range(1, 7):
                next_pos = pos + i
                if next_pos > n * n:
                    continue  # Skip if the move exceeds the board

                r, c = get_coordinates(next_pos)  # Convert position to coordinates
                if board[r][c] != -1:
                    # There's a snake or ladder at this square
                    next_pos = board[r][c]

                if next_pos == n * n:
                    # Reached final cell, return total moves
                    return moves + 1

                if next_pos not in visited:
                    visited.add(next_pos)
                    queue.append((next_pos, moves + 1))  # Add next position with incremented move

        return -1  # If end is unreachable
