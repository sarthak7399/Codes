# https://leetcode.com/problems/custom-sort-string/description/?envType=daily-question&envId=2024-03-11

# Example 1:
# Input:  order = "cba", s = "abcd" 
# Output:  "cbad" 
# Explanation: "a", "b", "c" appear in order, so the order of "a", "b", "c" should be "c", "b", and "a".
# Since "d" does not appear in order, it can be at any position in the returned string. "dcba", "cdba", "cbda" are also valid outputs.

class Solution:
    def customSortString(self, order: str, s: str) -> str:
        char_count={}
        for char in s:
            char_count[char]=char_count.get(char,0)+1
        result = ''
        for char in order:
            if char in char_count:
                result+=char*char_count[char]
                del char_count[char]
        for char in char_count:
            result+=char*char_count[char]
        return result