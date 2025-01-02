# https://leetcode.com/problems/count-vowel-strings-in-ranges/

# Example 1:
# Input: words = ["aba","bcb","ece","aa","e"], queries = [[0,2],[1,4],[1,1]]
# Output: [2,3,0]
# Explanation: The strings starting and ending with a vowel are "aba", "ece", "aa" and "e".
# The answer to the query [0,2] is 2 (strings "aba" and "ece").
# to query [1,4] is 3 (strings "ece", "aa", "e").
# to query [1,1] is 0.
# We return [2,3,0].

from typing import List
class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        # Initialize a prefix sum array where the first element is 0
        prefix = [0]
        cur = 0  # This will keep track of the number of valid words up to current index
        vowelSet = set(['a', 'e', 'i', 'o', 'u'])  # A set of vowels for easy lookup
        
        # Loop through each word in the `words` list
        for s in words:
            # Check if the first and last characters of the word are vowels
            if s[0] in vowelSet and s[-1] in vowelSet:
                cur += 1  # If the word is valid, increment the count
            prefix.append(cur)  # Append the current count to the prefix sum array
        
        res = []  # This will store the results for each query
        
        # Loop through each query (start and end index pairs)
        for s, e in queries:
            # For each query, calculate the number of valid words between index `s` and `e` inclusive
            res.append(prefix[e + 1] - prefix[s])  # Use the prefix sum array to quickly calculate this
        
        # Return the results as a list
        return res
