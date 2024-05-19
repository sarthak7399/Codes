# https://leetcode.com/problems/open-the-lock/

# Example 1:
# Input: deadends = ["0201","0101","0102","1212","2002"], target = "0202"
# Output: 6
# Explanation: 
# A sequence of valid moves would be "0000" -> "1000" -> "1100" -> "1200" -> "1201" -> "1202" -> "0202".
# Note that a sequence like "0000" -> "0001" -> "0002" -> "0102" -> "0202" would be invalid,
# because the wheels of the lock become stuck after the display becomes the dead end "0102".

from collections import deque
from typing import List
class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if target == "0000": return 0  # If target is already '0000', no turns needed
        queue, target = deque([0]), int(target)  # Initialize queue with starting point and convert target to integer
        seen, turns = [0] * 10000, 1  # Initialize seen array and turns counter
        for d in deadends: seen[int(d)] = 1  # Mark deadends in seen array
        if seen[0]: return -1  # If '0000' is a deadend, return -1
        while len(queue):  # While queue is not empty
            qlen = len(queue)  # Get the current length of the queue
            for i in range(qlen):  # Iterate over all elements in the queue
                curr, j = queue.popleft(), 1  # Get the current combination from the queue and initialize j
                while j < 10000:  # Iterate over all digits of the combination
                    mask = curr % (j * 10) // j  # Extract the digit at position j
                    masked = curr - (mask * j)  # Mask the digit at position j
                    for k in range(1,10,8):  # Generate all possible combinations by rotating digits
                        nxt = masked + (mask + k) % 10 * j  # Generate the next combination
                        if seen[nxt]: continue  # If combination is already visited, skip
                        if nxt == target: return turns  # If target is reached, return the number of turns
                        seen[nxt] = 1  # Mark the combination as visited
                        queue.append(nxt)  # Add the combination to the queue
                    j *= 10  # Move to the next digit position
            turns += 1  # Increment the number of turns
        return -1  # If target cannot be reached, return -1
