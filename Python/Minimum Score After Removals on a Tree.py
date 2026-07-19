# https://leetcode.com/problems/minimum-score-after-removals-on-a-tree/

# Example 1:
# Input: nums = [1,5,5,4,11], edges = [[0,1],[1,2],[1,3],[3,4]]
# Output: 9
# Explanation: The diagram above shows a way to make a pair of removals.
# - The 1st component has nodes [1,3,4] with values [5,4,11]. Its XOR value is 5 ^ 4 ^ 11 = 10.
# - The 2nd component has node [0] with value [1]. Its XOR value is 1 = 1.
# - The 3rd component has node [2] with value [5]. Its XOR value is 5 = 5.
# The score is the difference between the largest and smallest XOR value which is 10 - 1 = 9.
# It can be shown that no other pair of removals will obtain a smaller score than 9.

import collections

class Solution:
    def minimumScore(self, nums: list[int], edges: list[list[int]]) -> int:
        n = len(nums)
        graph = collections.defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        # subtree_xor[i] = XOR sum of the subtree rooted at i
        # descendants[i] = set of all nodes in the subtree of i
        subtree_xor = [0] * n
        descendants = [set() for _ in range(n)]

        # Perform a post-order DFS from root 0 to populate our data structures
        def dfs(node, parent):
            # Initialize with the node's own value and self
            subtree_xor[node] = nums[node]
            descendants[node].add(node)
            
            for neighbor in graph[node]:
                if neighbor != parent:
                    dfs(neighbor, node)
                    # After child returns, roll up its values
                    subtree_xor[node] ^= subtree_xor[neighbor]
                    descendants[node].update(descendants[neighbor])

        # Start the traversal from node 0, with -1 as a placeholder parent
        dfs(0, -1)
        
        total_xor = subtree_xor[0]
        min_score = float('inf')

        # Iterate through all pairs of nodes (i, j) to represent the two cuts.
        # The cuts are the edges between i/j and their parents.
        # We start from 1 because node 0 is the root and has no parent edge to cut above it.
        for i in range(1, n):
            for j in range(i + 1, n):
                xor_i = subtree_xor[i]
                xor_j = subtree_xor[j]
                
                # Case 1: j's subtree is inside i's subtree (nested cuts)
                if j in descendants[i]:
                    val1 = xor_j
                    val2 = xor_i ^ xor_j
                    val3 = total_xor ^ xor_i
                
                # Case 2: i's subtree is inside j's subtree (nested cuts)
                elif i in descendants[j]:
                    val1 = xor_i
                    val2 = xor_j ^ xor_i
                    val3 = total_xor ^ xor_j

                # Case 3: i and j are in independent branches
                else:
                    val1 = xor_i
                    val2 = xor_j
                    val3 = total_xor ^ xor_i ^ xor_j
                
                # Calculate score for this pair of cuts and update the minimum
                score = max(val1, val2, val3) - min(val1, val2, val3)
                min_score = min(min_score, score)
                
        return min_score