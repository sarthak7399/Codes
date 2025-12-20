# https://leetcode.com/problems/delete-columns-to-make-sorted/

# Example 1:
# Input: strs = ["cba","daf","ghi"]
# Output: 1
# Explanation: The grid looks as follows:
#   cba
#   daf
#   ghi
# Columns 0 and 2 are sorted, but column 1 is not, so you only need to delete 1 column.

class Solution:
    def minDeletionSize(self, strs):
        # Number of rows (strings)
        rows = len(strs)
        # Number of columns (characters per string)
        cols = len(strs[0])
        deletions = 0

        # Check each column
        for c in range(cols):
            # Compare adjacent rows in the same column
            for r in range(rows - 1):
                # If column is not sorted lexicographically
                if strs[r][c] > strs[r + 1][c]:
                    deletions += 1  # Mark this column for deletion
                    break            # Move to next column

        return deletions
