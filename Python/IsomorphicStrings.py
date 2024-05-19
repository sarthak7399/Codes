# https://leetcode.com/problems/isomorphic-strings/

# Example 1:
# Input: s = "egg", t = "add"
# Output: true

# Example 2:
# Input: s = "foo", t = "bar"
# Output: false

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mydict1, mydict2 = {}, {}  # Initialize dictionaries to store mappings
        for i in range(len(s)):
            # Check if the characters in s and t are already mapped differently
            if s[i] in mydict1 and mydict1[s[i]] != t[i]:
                return False
            # Check if the characters in t and s are already mapped differently
            if t[i] in mydict2 and mydict2[t[i]] != s[i]:
                return False
            # Update the mappings
            mydict1[s[i]] = t[i]
            mydict2[t[i]] = s[i]
        return True  # If no conflicts found, return True
