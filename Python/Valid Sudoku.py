# Example 1:
# Input: board = 
# [["5","3",".",".","7",".",".",".","."]
# ,["6",".",".","1","9","5",".",".","."]
# ,[".","9","8",".",".",".",".","6","."]
# ,["8",".",".",".","6",".",".",".","3"]
# ,["4",".",".","8",".","3",".",".","1"]
# ,["7",".",".",".","2",".",".",".","6"]
# ,[".","6",".",".",".",".","2","8","."]
# ,[".",".",".","4","1","9",".",".","5"]
# ,[".",".",".",".","8",".",".","7","9"]]
# Output: true

from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Boolean trackers:
        # rows[i][num]   → whether digit `num` is already used in row i
        # cols[j][num]   → whether digit `num` is already used in column j
        # boxes[k][num]  → whether digit `num` is already used in 3x3 sub-box k
        rows = [[False] * 9 for _ in range(9)]
        cols = [[False] * 9 for _ in range(9)]
        boxes = [[False] * 9 for _ in range(9)]

        # Traverse each cell of the board
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':  # ignore empty cells
                    # Convert character '1'–'9' into index 0–8
                    num = ord(board[i][j]) - ord('1')

                    # Calculate 3x3 box index
                    # (0..8 numbered left-to-right, top-to-bottom)
                    boxIndex = (i // 3) * 3 + (j // 3)

                    # If digit already exists in row, column, or box → invalid
                    if rows[i][num] or cols[j][num] or boxes[boxIndex][num]:
                        return False

                    # Mark digit as used in row, column, and box
                    rows[i][num] = cols[j][num] = boxes[boxIndex][num] = True

        # If no conflicts found → valid Sudoku
        return True
