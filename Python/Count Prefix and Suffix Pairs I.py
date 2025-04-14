# https://leetcode.com/problems/count-prefix-and-suffix-pairs-i/

# Example 1:
# Input: words = ["a","aba","ababa","aa"]
# Output: 4
# Explanation: In this example, the counted index pairs are:
# i = 0 and j = 1 because isPrefixAndSuffix("a", "aba") is true.
# i = 0 and j = 2 because isPrefixAndSuffix("a", "ababa") is true.
# i = 0 and j = 3 because isPrefixAndSuffix("a", "aa") is true.
# i = 1 and j = 2 because isPrefixAndSuffix("aba", "ababa") is true.
# Therefore, the answer is 4.

from typing import List
class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        n = len(words)  # Get the total number of words
        ans = 0  # Initialize a counter for valid prefix-suffix pairs
        
        # Loop through each word
        for i in range(n):
            s1 = words[i]  # Get the current word (s1)
            
            # Loop through remaining words after s1
            for j in range(i + 1, n):
                s2 = words[j]  # Get the next word (s2)
                
                # Skip if s2 is shorter than s1
                if len(s2) < len(s1):
                    continue
                
                # Get prefix and suffix of s2 with length equal to s1
                pre = s2[:len(s1)]
                suf = s2[-len(s1):]
                
                # Check if both prefix and suffix match s1
                if pre == s1 and suf == s1:
                    ans += 1  # Increment the counter if a match is found
        
        return ans  # Return the final count
