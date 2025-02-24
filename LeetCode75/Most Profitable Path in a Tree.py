# https://leetcode.com/problems/most-profitable-path-in-a-tree/

# Example 1:
# Input: edges = [[0,1],[1,2],[1,3],[3,4]], bob = 3, amount = [-2,4,2,-4,6]
# Output: 6
# Explanation: 
# The above diagram represents the given tree. The game goes as follows:
# - Alice is initially on node 0, Bob on node 3. They open the gates of their respective nodes.
#   Alice's net income is now -2.
# - Both Alice and Bob move to node 1. 
#   Since they reach here simultaneously, they open the gate together and share the reward.
#   Alice's net income becomes -2 + (4 / 2) = 0.
# - Alice moves on to node 3. Since Bob already opened its gate, Alice's income remains unchanged.
#   Bob moves on to node 0, and stops moving.
# - Alice moves on to node 4 and opens the gate there. Her net income becomes 0 + 6 = 6.
# Now, neither Alice nor Bob can make any further moves, and the game ends.
# It is not possible for Alice to get a higher net income.

from typing import List
class Solution:
    def mostProfitablePath(self, edges: List[List[int]], bob: int, amount: List[int]) -> int:
        # Build an adjacency list representation of the graph
        graph = {i: [] for i in range(len(amount))}
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        bobPath = [-1] * len(amount)  # Stores the time Bob reaches each node
        path = []  # Tracks Bob's path from his node to root

        # DFS to find Bob's path from his node to the root (0)
        def fillBobPath(node, parent):
            if node == 0:
                return True
            for neighbor in graph[node]:
                if neighbor != parent:
                    path.append(node)
                    if fillBobPath(neighbor, node):
                        return True
                    path.pop()

        fillBobPath(bob, -1)
        for i, node in enumerate(path):
            bobPath[node] = i  # Store the timestamp Bob reaches each node

        # DFS to compute Alice's max possible score while traversing the tree
        def getAliceMaxScore(node, parent, currScore, timestamp):
            if bobPath[node] == -1 or bobPath[node] > timestamp:  # Alice alone at this node
                currScore += amount[node]
            elif bobPath[node] == timestamp:  # Both Alice and Bob reach at the same time
                currScore += amount[node] // 2

            # If this is a leaf node (except root), return current score
            if len(graph[node]) == 1 and node != 0:
                return currScore

            # Recur for child nodes and take the max score
            return max(getAliceMaxScore(neighbor, node, currScore, timestamp + 1) 
                       for neighbor in graph[node] if neighbor != parent)

        return getAliceMaxScore(0, -1, 0, 0)  # Start DFS from root (Alice's start)
