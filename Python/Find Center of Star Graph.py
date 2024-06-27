# https://leetcode.com/problems/find-center-of-star-graph/submissions/

# Example 1:
# Input: edges = [[1,2],[2,3],[4,2]]
# Output: 2
# Explanation: As shown in the figure above, node 2 is connected to every other node, so 2 is the center.

from typing import List
class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        counts=[]
        for e in edges:
            if e[0] in counts:
                return e[0]
            if e[1] in counts:
                return e[1]
            counts.append(e[0])
            counts.append(e[1])   