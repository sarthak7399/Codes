# https://leetcode.com/problems/minimum-string-length-after-removing-substrings/

# Example 1:
# Input: s = "ABFCACDB"
# Output: 2
# Explanation: We can do the following operations:
# - Remove the substring "ABFCACDB", so s = "FCACDB".
# - Remove the substring "FCACDB", so s = "FCAB".
# - Remove the substring "FCAB", so s = "FC".
# So the resulting length of the string is 2.
# It can be shown that it is the minimum length that we can obtain.

class Solution:
    def minLength(self, s: str) -> int:
        stack = []
        
        for char in s:
            # Check if the last two characters form 'AB' or 'CD'
            if stack and ((stack[-1] == 'A' and char == 'B') or (stack[-1] == 'C' and char == 'D')):
                stack.pop()  # Remove the last character (either 'A' or 'C')
            else:
                stack.append(char)  # Otherwise, just add the character to the stack
        
        # The remaining characters in the stack are the unreducible part of the string
        return len(stack)