# https://leetcode.com/problems/final-value-of-variable-after-performing-operations/

# Example 1:
# Input: operations = ["--X","X++","X++"]
# Output: 1
# Explanation: The operations are performed as follows:
# Initially, X = 0.
# --X: X is decremented by 1, X =  0 - 1 = -1.
# X++: X is incremented by 1, X = -1 + 1 =  0.
# X++: X is incremented by 1, X =  0 + 1 =  1.

class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        count = 0  # variable to track the final value
        
        for op in operations:
            # if operation contains '-', decrement count
            if "-" in op:
                count -= 1
            else:  # otherwise increment count
                count += 1
        
        return count  # final value after all operations
