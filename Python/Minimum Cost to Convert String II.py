# https://leetcode.com/problems/minimum-cost-to-convert-string-ii/

# Example 2:
# Input: source = "abcdefgh", target = "acdeeghh", original = ["bcd","fgh","thh"], changed = ["cde","thh","ghh"], cost = [1,3,5]
# Output: 9
# Explanation: To convert "abcdefgh" to "acdeeghh", do the following operations:
# - Change substring source[1..3] from "bcd" to "cde" at a cost of 1.
# - Change substring source[5..7] from "fgh" to "thh" at a cost of 3. We can do this operation because indices [5,7] are disjoint with indices picked in the first operation.
# - Change substring source[5..7] from "thh" to "ghh" at a cost of 5. We can do this operation because indices [5,7] are disjoint with indices picked in the first operation, and identical with indices picked in the second operation.
# The total cost incurred is 1 + 3 + 5 = 9.
# It can be shown that this is the minimum possible cost.

import math
from typing import List

class TrieNode(dict):
    __slots__ = ("sid",)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.sid = -1  # ID of string ending here, -1 means no string ends


class Solution:
    def minimumCost(
        self,
        source: str,
        target: str,
        original: List[str],
        changed: List[str],
        cost: List[int]
    ) -> int:

        n = len(source)

        # ------------------------------------------------------------------
        # Step 1: Index all unique strings (original + changed)
        # Each string gets a unique ID
        # ------------------------------------------------------------------
        index = {}
        for s in original + changed:
            if s not in index:
                index[s] = len(index)

        K = len(index)

        # ------------------------------------------------------------------
        # Step 2: Build distance matrix for string-to-string transformations
        # dist[u][v] = minimum cost to convert string u -> string v
        # ------------------------------------------------------------------
        dist = [[math.inf] * K for _ in range(K)]
        for i in range(K):
            dist[i][i] = 0  # zero cost to stay same

        for o, c, w in zip(original, changed, cost):
            u, v = index[o], index[c]
            dist[u][v] = min(dist[u][v], w)

        # ------------------------------------------------------------------
        # Step 3: Floyd–Warshall to compute all-pairs shortest paths
        # Allows multi-step transformations
        # ------------------------------------------------------------------
        for k in range(K):
            for u in range(K):
                if dist[u][k] != math.inf:
                    for v in range(K):
                        if dist[k][v] != math.inf:
                            dist[u][v] = min(dist[u][v], dist[u][k] + dist[k][v])

        # ------------------------------------------------------------------
        # Step 4: Build a Trie of all indexed strings
        # Helps match substrings efficiently
        # ------------------------------------------------------------------
        trie = TrieNode()
        maxlen = 0

        for s, sid in index.items():
            node = trie
            for ch in s:
                if ch not in node:
                    node[ch] = TrieNode()
                node = node[ch]
            node.sid = sid
            maxlen = max(maxlen, len(s))

        # ------------------------------------------------------------------
        # Step 5: For each position i, store all substrings starting at i
        # result[i][length] = string ID
        # ------------------------------------------------------------------
        def starts_map(s: str):
            result = [dict() for _ in range(n)]
            for i in range(n):
                node = trie
                for j in range(i, min(n, i + maxlen)):
                    if s[j] not in node:
                        break
                    node = node[s[j]]
                    if node.sid != -1:
                        result[i][j - i + 1] = node.sid
            return result

        src_starts = starts_map(source)
        tgt_starts = starts_map(target)

        # ------------------------------------------------------------------
        # Step 6: DP
        # dp[i] = minimum cost to transform source[:i] -> target[:i]
        # ------------------------------------------------------------------
        dp = [0] + [math.inf] * n

        for i in range(n):
            if dp[i] == math.inf:
                continue

            # Case 1: characters already match
            if source[i] == target[i]:
                dp[i + 1] = min(dp[i + 1], dp[i])

            # Case 2: try transforming substrings
            sm, tm = src_starts[i], tgt_starts[i]
            if not sm or not tm:
                continue

            # Only substrings of same length can be transformed
            for length in sm:
                if length not in tm:
                    continue

                d = dist[sm[length]][tm[length]]
                if d != math.inf:
                    dp[i + length] = min(dp[i + length], dp[i] + d)

        return dp[n] if dp[n] != math.inf else -1
