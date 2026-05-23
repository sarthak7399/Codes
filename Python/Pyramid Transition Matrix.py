# https://leetcode.com/problems/pyramid-transition-matrix/

# Example 1:
# Input: bottom = "BCD", allowed = ["BCC","CDE","CEA","FFF"]
# Output: true
# Explanation: The allowed triangular patterns are shown on the right.
# Starting from the bottom (level 3), we can build "CE" on level 2 and then build "A" on level 1.
# There are three triangular patterns in the pyramid, which are "BCC", "CDE", and "CEA". All are allowed.

from collections import defaultdict
from typing import List

class Solution:
    def pyramidTransition(self, bottom: str, allowed: List[str]) -> bool:
        # Map each pair (u, v) to possible top characters
        tab = defaultdict(set)
        for u, v, w in allowed:
            tab[u, v].add(w)

        # Generate all possible next-level strings from current level
        def add_neighbor(node):
            res = ['']
            for i in range(1, len(node)):
                eles = tab[(node[i - 1], node[i])]
                if eles:
                    # Append all valid characters for this position
                    res = [a + e for e in eles for a in res]
                else:
                    return []
            return res
        
        visited = set()  # Memo to avoid recomputation

        def dfs(node):
            # Reached the top of the pyramid
            if len(node) == 1:
                return True
            # Already checked and failed
            if node in visited:
                return False

            # Try all possible next levels
            for nxt in add_neighbor(node):
                if dfs(nxt):
                    return True

            visited.add(node)
            return False

        return dfs(bottom)
