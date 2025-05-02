# https://leetcode.com/problems/push-dominoes/description/

# Example 1:
# Input: dominoes = "RR.L"
# Output: "RR.L"
# Explanation: The first domino expends no additional force on the second domino.

from collections import deque

class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        domi = list(dominoes)  # Convert the string to a list for in-place updates
        q = deque()  # Queue to simulate domino pushes: stores (index, direction)
        visit = set()  # Set to keep track of indices that have already been processed

        # Initialize the queue with initially pushed dominoes (either 'L' or 'R')
        for i in range(len(domi)):
            if domi[i] in {'L', 'R'}:
                q.append((i, domi[i]))

        # Helper to check if an index is within bounds
        def inBound(id):
            return 0 <= id < len(domi)

        # Helper to check if the current domino is in a conflict situation ('R.L')
        def isStill(id):
            if inBound(id - 1) and inBound(id + 1):
                return domi[id - 1] == 'R' and domi[id + 1] == 'L'
            else:
                return False

        # Breadth-first simulation of domino effects
        while q:
            for _ in range(len(q)):  # Process all dominoes in the current time step
                idx, dire = q.popleft()

                if idx in visit:
                    continue  # Skip already processed dominoes
                visit.add(idx)

                if domi[idx] == 'R':  # Domino is pushing to the right
                    if inBound(idx + 1) and idx + 1 not in visit:
                        if isStill(idx + 1):
                            visit.add(idx + 1)  # Don't push it due to balanced push ('R.L')
                            continue
                        elif domi[idx + 1] == '.':
                            domi[idx + 1] = 'R'
                            q.append((idx + 1, 'R'))  # Continue pushing to the right

                elif domi[idx] == 'L':  # Domino is pushing to the left
                    if inBound(idx - 1):
                        if idx - 1 not in visit:
                            if domi[idx - 1] == '.':
                                domi[idx - 1] = 'L'
                                q.append((idx - 1, 'L'))  # Continue pushing to the left
                        else:
                            if isStill(idx - 1):
                                visit.add(idx - 1)  # Prevent further conflict
                                continue

        return ''.join(domi)  # Convert the final state back to a string
