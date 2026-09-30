# https://leetcode.com/problems/maximum-nesting-depth-of-two-valid-parentheses-strings/

# Example 1:
# Input: seq = "(()())"
# Output: [0,1,1,1,1,0]

class Solution:
    def maxDepthAfterSplit(self, seq: str) -> list[int]:
        # Store the group (0 or 1) assigned to each parenthesis.
        res = []

        # Process each parenthesis in the sequence.
        for i in range(len(seq)):
            # Use the index and character to alternate parentheses
            # between the two groups while maintaining valid depth.
            res.append((i ^ ord(seq[i])) & 1)

        # Return the group assignment for each parenthesis.
        return res