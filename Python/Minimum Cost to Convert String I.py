# https://leetcode.com/problems/minimum-cost-to-convert-string-i/

# Example 1:
# Input: source = "abcd", target = "acbe", original = ["a","b","c","c","e","d"], changed = ["b","c","b","e","b","e"], cost = [2,5,5,1,2,20]
# Output: 28
# Explanation: To convert the string "abcd" to string "acbe":
# - Change value at index 1 from 'b' to 'c' at a cost of 5.
# - Change value at index 2 from 'c' to 'e' at a cost of 1.
# - Change value at index 2 from 'e' to 'b' at a cost of 2.
# - Change value at index 3 from 'd' to 'e' at a cost of 20.
# The total cost incurred is 5 + 1 + 2 + 20 = 28.
# It can be shown that this is the minimum possible cost.

from collections import defaultdict
from heapq import heappush, heappop
from math import inf
from typing import List

class Solution:

    # Dijkstra: find minimum cost to reach all characters starting from sourceChar
    def minimumCostFrom(self, sourceChar):
        bests = {}  # final shortest cost to each node
        seenCost = defaultdict(lambda: inf)  # best cost seen so far for each node
        seenCost[sourceChar] = 0

        # Min-heap: (current_cost, current_node)
        frontier = [(0, sourceChar)]

        while frontier:
            reachCost, current = heappop(frontier)

            # If already finalized, skip
            if current in bests:
                continue

            # Lock in the best cost for this node
            bests[current] = reachCost

            # Try all outgoing edges
            for d, edgeCost in self.edges[current].items():
                totalCost = reachCost + edgeCost

                # If we found a cheaper way to reach d, update heap
                if totalCost < seenCost[d]:
                    heappush(frontier, (totalCost, d))
                    seenCost[d] = totalCost

        return bests

    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        # Build graph: edges[u][v] = min cost to change u -> v
        self.edges = defaultdict(lambda: {})

        for i in range(len(original)):
            s = original[i]
            d = changed[i]
            c = cost[i]

            # Keep only the cheapest edge if multiple exist
            if d not in self.edges[s] or c < self.edges[s][d]:
                self.edges[s][d] = c

        # Cache of shortest paths: bests[s] = dict of min costs from s to others
        bests = defaultdict(lambda: {})

        totalCost = 0

        # For each character position
        for s, t in zip(source, target):
            if s != t:
                # If we already computed paths from s
                if t in bests[s]:
                    totalCost += bests[s][t]

                # If we computed before and t was not reachable
                elif len(bests[s]) > 0:
                    return -1

                # Otherwise, run Dijkstra from s
                else:
                    best = self.minimumCostFrom(s)
                    bests[s] = best

                    if t in best:
                        totalCost += best[t]
                    else:
                        return -1

        return totalCost
