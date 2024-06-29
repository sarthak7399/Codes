# https://leetcode.com/problems/all-ancestors-of-a-node-in-a-directed-acyclic-graph/

# Example 1:
# Input: n = 8, edgeList = [[0,3],[0,4],[1,3],[2,4],[2,7],[3,5],[3,6],[3,7],[4,6]]
# Output: [[],[],[],[0,1],[0,2],[0,1,3],[0,1,2,3,4],[0,1,2,3]]
# Explanation:
# The above diagram represents the input graph.
# - Nodes 0, 1, and 2 do not have any ancestors.
# - Node 3 has two ancestors 0 and 1.
# - Node 4 has two ancestors 0 and 2.
# - Node 5 has three ancestors 0, 1, and 3.
# - Node 6 has five ancestors 0, 1, 2, 3, and 4.
# - Node 7 has four ancestors 0, 1, 2, and 3.

from typing import List
class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        ans = [[] for _ in range(n)]
        directChild = [[] for _ in range(n)]
        for e in edges:
            directChild[e[0]].append(e[1])
        for i in range(n):
            self.dfs(i, i, ans, directChild)
        return ans

    def dfs(self, x: int, curr: int, ans: List[List[int]], directChild: List[List[int]]) -> None:
        for ch in directChild[curr]:
            if not ans[ch] or ans[ch][-1] != x:
                ans[ch].append(x)
                self.dfs(x, ch, ans, directChild)