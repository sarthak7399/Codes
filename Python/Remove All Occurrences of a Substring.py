# https://leetcode.com/problems/remove-all-occurrences-of-a-substring/

# Example 1:
# Input: s = "daabcbaabcbc", part = "abc"
# Output: "dab"
# Explanation: The following operations are done:
# - s = "daabcbaabcbc", remove "abc" starting at index 2, so s = "dabaabcbc".
# - s = "dabaabcbc", remove "abc" starting at index 4, so s = "dababc".
# - s = "dababc", remove "abc" starting at index 3, so s = "dab".
# Now s has no occurrences of "abc".

class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        
        # Loop until 'part' is no longer found in 's'
        while True:
            idx = s.find(part)  # Find the index of 'part' in 's'
            if idx == -1:  # If 'part' is not found, exit loop
                break
            s = s[:idx] + s[idx + len(part):]  # Remove 'part' from 's'
        return s  # Return the modified string
