# https://leetcode.com/problems/path-with-maximum-probability/

# Example 1:
# Input: n = 3, edges = [[0,1],[1,2],[0,2]], succProb = [0.5,0.5,0.2], start = 0, end = 2
# Output: 0.25000
# Explanation: There are two paths from start to end, one having a probability of success = 0.2 and the other has 0.5 * 0.5 = 0.25.

from heapq import heappop, heappush
from typing import List
class Solution:
    def maxProbability(
        self,
        n: int,
        edges: List[List[int]],
        succProb: List[float],
        start_node: int,
        end_node: int,
    ) -> float:
        adj = [[] for _ in range(n)]
        for (v1, v2), prob in zip(edges, succProb):
            adj[v1].append((v2, prob))
            adj[v2].append((v1, prob))
        probs = [0.0 for _ in range(n)]
        probs[start_node] = 1.0
        heap = [(-1.0, start_node)]
        while heap:
            prob1, v1 = heappop(heap)
            prob1 *= -1.0
            if v1 == end_node:
                break
            if prob1 < probs[v1]:
                continue
            for v2, prob2 in adj[v1]:
                prob2 *= prob1
                if prob2 > probs[v2]:
                    probs[v2] = prob2
                    heappush(heap, (-prob2, v2))
        return probs[end_node]