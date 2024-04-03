# https://leetcode.com/problems/word-search/

# Example 2:
# Input: board = [["A","B","C","E"],
#                 ["S","F","C","S"],
#                 ["A","D","E","E"]], 
# word = "SEE"
# Output: true

# Example 3:
# Input: board = [["A","B","C","E"],
#                 ["S","F","C","S"],
#                 ["A","D","E","E"]], 
# word = "ABCB"
# Output: false

from typing import List
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # Define ROWS and COLS variables
        ROWS, COLS = len(board), len(board[0])
        path = set()  # Initialize a set to keep track of visited cells

        # Define the DFS function
        def dfs(r, c, i):
            # Base case: if all characters of the word are found
            if i == len(word):
                return True
            
            # Check for out-of-bounds or invalid cells
            if (r < 0 or c < 0 or
                r >= ROWS or c >= COLS or
                word[i] != board[r][c] or
                (r, c) in path):
                return False
            
            # Add the current cell to the path
            path.add((r, c))
            
            # Recursively check adjacent cells
            res = (dfs(r + 1, c, i + 1) or
                   dfs(r - 1, c, i + 1) or
                   dfs(r, c + 1, i + 1) or
                   dfs(r, c - 1, i + 1))
            
            # Remove the current cell from the path
            path.remove((r, c))
            return res

        # Iterate through each cell in the board
        for r in range(ROWS):
            for c in range(COLS):
                # Start DFS from each cell
                if dfs(r, c, 0):
                    return True  # If word is found, return True
        return False  # If word is not found, return False
