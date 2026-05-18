# https://leetcode.com/problems/jump-game-iv/

# Example 1:
# Input: arr = [100,-23,-23,404,100,23,23,23,3,404]
# Output: 3
# Explanation: You need three jumps from index 0 --> 4 --> 3 --> 9. Note that index 9 is the last index of the array.

from collections import defaultdict, deque
from typing import List

class Solution:
    def minJumps(self, arr: List[int]) -> int:
        n = len(arr)

        # If array has only one element, already at destination
        if n == 1:
            return 0

        # Map each value to all indices where it appears
        graph = defaultdict(list)
        for i, val in enumerate(arr):
            graph[val].append(i)

        # BFS queue starting from index 0
        q = deque([0])

        # Track visited indices
        visited = [False] * n
        visited[0] = True

        # Number of jumps taken
        cnt = 0

        # Perform BFS
        while q:

            # Process all nodes at current BFS level
            for _ in range(len(q)):
                idx = q.popleft()

                # Reached last index
                if idx == n - 1:
                    return cnt

                # Move to left neighbor
                if idx - 1 >= 0 and not visited[idx - 1]:
                    visited[idx - 1] = True
                    q.append(idx - 1)

                # Move to right neighbor
                if idx + 1 < n and not visited[idx + 1]:
                    visited[idx + 1] = True
                    q.append(idx + 1)

                # Jump to all indices having same value
                if arr[idx] in graph:
                    for nxt in graph[arr[idx]]:
                        if not visited[nxt]:
                            visited[nxt] = True
                            q.append(nxt)

                    # Remove processed value to avoid repeated traversal
                    del graph[arr[idx]]

            # Increment jump count after one BFS level
            cnt += 1

        # If destination is unreachable
        return -1