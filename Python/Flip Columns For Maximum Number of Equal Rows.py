# https://leetcode.com/problems/flip-columns-for-maximum-number-of-equal-rows/

# Example 3:
# Input: matrix = [[0,0,0],[0,0,1],[1,1,0]]
# Output: 2
# Explanation: After flipping values in the first two columns, the last two rows have equal values.

import collections
from typing import List
class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        # Initialize a counter to track patterns of rows
        patterns = collections.Counter()
        # OR
        # patterns = {}

        # Iterate over each row in the matrix
        for row in matrix:
            # If the first element of the row is 1, normalize the row by flipping all its bits
            # This ensures all rows start with a 0 after normalization
            if row[0] == 1:
                normalized_row = tuple(1 - x for x in row)
            else:
                # If the first element is 0, use the row as is
                normalized_row = tuple(row)
            
            # Increment the count of this normalized row pattern in the counter
            patterns[normalized_row] = patterns[normalized_row] + 1

            # OR
            # if normalized_row not in patterns:
            #     patterns[normalized_row] = 1
            # else:
            #     patterns[normalized_row] = patterns[normalized_row] + 1

        # Return the maximum count of any normalized pattern
        # This represents the maximum number of rows that can become identical
        return max(patterns.values())