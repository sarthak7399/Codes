# https://leetcode.com/problems/lexicographically-minimum-string-after-removing-stars/

# Example 1:
# Input: s = "aaba*"
# Output: "aab"
# Explanation:
# We should delete one of the 'a' characters with '*'. If we choose s[3], s becomes the lexicographically smallest.

import heapq
import itertools

class Solution:
    def clearStars(self, s: str) -> str:
        h = []  # Min-heap to keep track of smallest characters' indices (based on `ord`)
        stacks = [[] for _ in range(26)]  # Array of stacks for each character 'a' to 'z'

        for i, c in enumerate(s):
            if c == "*":
                # When a '*' is encountered, remove the most recent occurrence of 
                # the **smallest character available** (lexicographically)
                
                # Clean up heap top until it points to a non-empty stack
                while h and not stacks[h[0]]:
                    heapq.heappop(h)

                # If there is still a valid character to remove
                if h:
                    stacks[h[0]].pop()  # Remove the most recent occurrence
            else:
                # Convert character to index (0 for 'a', ..., 25 for 'z')
                x = ord(c) - 97

                # If this character wasn't in heap (first occurrence), push to heap
                if not stacks[x]:
                    heapq.heappush(h, x)

                # Store the index of this character's occurrence
                stacks[x].append(i)

        # Flatten the stacks and sort indices to reconstruct the final string
        all_indices = list(itertools.chain.from_iterable(stacks))
        all_indices.sort()
        
        # Build the final string from remaining character indices
        return "".join(s[i] for i in all_indices)
