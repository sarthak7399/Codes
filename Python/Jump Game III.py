# https://leetcode.com/problems/jump-game-iii/

# Example 1:
# Input: arr = [4,2,3,0,3,1,2], start = 5
# Output: true
# Explanation: 
# All possible ways to reach at index 3 with value 0 are: 
# index 5 -> index 4 -> index 1 -> index 3 
# index 5 -> index 6 -> index 4 -> index 1 -> index 3 

from collections import deque
from typing import List

class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        n = len(arr)

        # BFS queue starting from 'start' index
        q = deque([start])

        # Track visited indices to avoid infinite loops
        visited = [False] * n
        visited[start] = True

        # Perform BFS
        while q:
            node = q.popleft()

            # If current value is 0, destination is reached
            if arr[node] == 0:
                return True

            # Possible next positions:
            # jump left and jump right
            l = node - arr[node]
            r = node + arr[node]

            # Move to left index if valid and unvisited
            if l >= 0 and not visited[l]:
                q.append(l)
                visited[l] = True

            # Move to right index if valid and unvisited
            if r < n and not visited[r]:
                q.append(r)
                visited[r] = True

        # No path found to any index containing 0
        return False