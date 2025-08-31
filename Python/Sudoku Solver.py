# https://leetcode.com/problems/sudoku-solver/

# Example 1:
# Input: board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
# Output: [["5","3","4","6","7","8","9","1","2"],["6","7","2","1","9","5","3","4","8"],["1","9","8","3","4","2","5","6","7"],["8","5","9","7","6","1","4","2","3"],["4","2","6","8","5","3","7","9","1"],["7","1","3","9","2","4","8","5","6"],["9","6","1","5","3","7","2","8","4"],["2","8","7","4","1","9","6","3","5"],["3","4","5","2","8","6","1","7","9"]]

import collections
from typing import List

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Solves the Sudoku puzzle by filling the empty cells ('.').
        Modifies the board in-place using backtracking.
        """

        # Use sets to track digits already used in each row, column, and 3x3 subgrid
        rows = collections.defaultdict(set)      # rows[i] contains digits in row i
        columns = collections.defaultdict(set)   # columns[j] contains digits in column j
        grid = collections.defaultdict(set)      # grid[k] contains digits in 3x3 subgrid k

        # Helper function: check if we can place 'digit' in (row, column)
        def matched(digit, row, column, rows, columns, grid):
            return (
                digit not in rows[row] and
                digit not in columns[column] and
                digit not in grid[(row // 3) * 3 + (column // 3)]
            )

        # Recursive backtracking function
        def fun(i, j, board, rows, columns, grid):
            # Base case: reached beyond the last row → solved!
            if i == 9:
                return True

            # Move to next row if we’re past last column
            if j == 9:
                return fun(i + 1, 0, board, rows, columns, grid)

            # Skip already filled cells
            if board[i][j] != ".":
                return fun(i, j + 1, board, rows, columns, grid)

            # Try placing digits 1–9
            for digit in range(1, 10):
                if matched(digit, i, j, rows, columns, grid):
                    # Place digit
                    board[i][j] = str(digit)
                    rows[i].add(digit)
                    columns[j].add(digit)
                    grid[(i // 3) * 3 + (j // 3)].add(digit)

                    # Recurse to next cell
                    if fun(i, j + 1, board, rows, columns, grid):
                        return True

                    # Backtrack if failed
                    board[i][j] = "."
                    rows[i].remove(digit)
                    columns[j].remove(digit)
                    grid[(i // 3) * 3 + (j // 3)].remove(digit)

            # No digit fits → backtrack
            return False

        # Pre-fill sets with existing numbers from the board
        for i in range(9):
            for j in range(9):
                if board[i][j] != ".":
                    num = int(board[i][j])
                    rows[i].add(num)
                    columns[j].add(num)
                    grid[(i // 3) * 3 + (j // 3)].add(num)

        # Start backtracking from top-left
        fun(0, 0, board, rows, columns, grid)
