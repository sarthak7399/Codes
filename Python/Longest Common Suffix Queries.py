# https://leetcode.com/problems/longest-common-suffix-queries/

# Example 1:
# Input: wordsContainer = ["abcd","bcd","xbcd"], wordsQuery = ["cd","bcd","xyz"]
# Output: [1,1,1]
# Explanation:
# Let's look at each wordsQuery[i] separately:
# For wordsQuery[0] = "cd", strings from wordsContainer that share the longest common suffix "cd" are at indices 0, 1, and 2. Among these, the answer is the string at index 1 because it has the shortest length of 3.
# For wordsQuery[1] = "bcd", strings from wordsContainer that share the longest common suffix "bcd" are at indices 0, 1, and 2. Among these, the answer is the string at index 1 because it has the shortest length of 3.
# For wordsQuery[2] = "xyz", there is no string from wordsContainer that shares a common suffix. Hence the longest common suffix is "", that is shared with strings at index 0, 1, and 2. Among these, the answer is the string at index 1 because it has the shortest length of 3.

from typing import List

class TrieNode:
    # Restrict attributes to save memory
    __slots__ = ['children', 'bestLen', 'bestIdx']
    
    def __init__(self):
        # children -> maps character to next TrieNode
        self.children = {}

        # bestLen -> length of shortest word passing through this node
        self.bestLen = float('inf')

        # bestIdx -> index of shortest word in wordsContainer
        self.bestIdx = float('inf')


class Solution:
    def stringIndices(self, wordsContainer: List[str], wordsQuery: List[str]) -> List[int]:

        # Root of reversed trie
        root = TrieNode()
        
        # Build trie using reversed words
        for i, word in enumerate(wordsContainer):

            n = len(word)
            curr = root
            
            # Update best answer at root node
            # (handles empty suffix match case)
            if n < curr.bestLen or (n == curr.bestLen and i < curr.bestIdx):
                curr.bestLen = n
                curr.bestIdx = i
                
            # Insert reversed word into trie
            for char in reversed(word):

                # Create child node if not present
                if char not in curr.children:
                    curr.children[char] = TrieNode()
                
                curr = curr.children[char]
                
                # Store shortest word info for this suffix path
                # If tie in length, choose smaller index
                if n < curr.bestLen or (n == curr.bestLen and i < curr.bestIdx):
                    curr.bestLen = n
                    curr.bestIdx = i
                    
        ans = []
        
        # Process each query
        for query in wordsQuery:

            curr = root
            
            # Traverse trie using reversed query
            for char in reversed(query):

                # Stop if suffix path does not exist
                if char not in curr.children:
                    break

                curr = curr.children[char]
            
            # Best matching index for longest suffix found
            ans.append(curr.bestIdx)
            
        return ans