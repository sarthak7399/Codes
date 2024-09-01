# https://leetcode.com/problems/minimum-number-of-pushes-to-type-word-ii/

# Example 1:
# Input: word = "abcde"
# Output: 5
# Explanation: The remapped keypad given in the image provides the minimum cost.
# "a" -> one push on key 2
# "b" -> one push on key 3
# "c" -> one push on key 4
# "d" -> one push on key 5
# "e" -> one push on key 6
# Total cost is 1 + 1 + 1 + 1 + 1 = 5.
# It can be shown that no other mapping can provide a lower cost.

class Solution:
    def minimumPushes(self, word: str) -> int:
        l=[0]*(32)
        for i in range(26):
            l[i]=word.count(chr(97+i))
        l.sort(reverse=True)
        res=0
        for i in range(4):
            for j in range(8):
                res+=(i+1)*l[8*i+j]
        return res