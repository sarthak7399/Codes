# https://leetcode.com/problems/remove-max-number-of-edges-to-keep-graph-fully-traversable/

# Example 1:
# Input: n = 4, edges = [[3,1,2],[3,2,3],[1,1,3],[1,2,4],[1,1,2],[2,3,4]]
# Output: 2
# Explanation: If we remove the 2 edges [1,1,2] and [1,1,3]. The graph will still be fully traversable by Alice and Bob. Removing any additional edge will not make it so. So the maximum number of edges we can remove is 2.

from typing import List
class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        """
        Union Find

        Union all the edge with the type 3 first and keeping track of the count
        When union, check if 2 nodes are connected already then we increase the count

        Then do it for Alice and Bob with the same process, if nodes are conencted increment the count
        return the sum of all
        """

        par = [i for i in range(n)]

        # union find with type 3 to connect all the node
        saveCommon = self.findCommon(n, edges, par, 3)
        # IMPORTANT, we work Alice and Bob starting the par we modified after saveCommon which have different parents so need the copy of par
        saveAlice = self.findCommon(n, edges, par.copy(), 1)
        if saveAlice == -1: return -1
        saveBob = self.findCommon(n, edges, par.copy(), 2)
        if saveBob == -1: return -1
        return saveCommon + saveAlice + saveBob
    
    def findCommon(self, n, edges, par, type):
        res = 0
        for e in edges:
            if e[0] != type:
                continue

            # make to index 0, find the parent and compare if these 2 nodes are connected
            p1 = self.find(e[1] - 1, par)
            p2 = self.find(e[2] - 1, par)
            # connected, therefore we can remove this edge
            if p1 == p2:
                res += 1
                continue
            if p1 > p2:
                par[p1] = p2
            else:
                par[p2] = p1
            
        if type == 3:
            return res
        # check if all the nodes point to 0 which is the root
        for i in range(n):
            p = self.find(i, par)
            if p != 0:
                return -1
        return res
    
    def find(self, curr, par):
        if curr != par[curr]:
            # compression and recursive making the curr point to the root
            par[curr] = self.find(par[curr], par)
        return par[curr]