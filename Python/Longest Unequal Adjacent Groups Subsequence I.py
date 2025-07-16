# https://leetcode.com/problems/longest-unequal-adjacent-groups-subsequence-i/

# Example 1:
# Input: words = ["e","a","b"], groups = [0,0,1]
# Output: ["e","b"]
# Explanation: A subsequence that can be selected is ["e","b"] because groups[0] != groups[2]. Another subsequence that can be selected is ["a","b"] because groups[1] != groups[2]. It can be demonstrated that the length of the longest subsequence of indices that satisfies the condition is 2.

class Solution:
    def getLongestSubsequence(self, words, groups):
        result = []   # List to store the longest valid subsequence
        last = -1     # Variable to track the last group that was added to result
        
        for i in range(len(words)):
            # Only include the word if its group is different from the last added one
            if groups[i] != last:
                result.append(words[i])  # Add the current word to the result
                last = groups[i]         # Update last seen group

        return result  # Return the longest subsequence where adjacent elements have different groups
