# https://leetcode.com/problems/sum-of-digits-of-string-after-convert/

# Example 1:
# Input: s = "iiii", k = 1
# Output: 36
# Explanation: The operations are as follows:
# - Convert: "iiii" ➝ "(9)(9)(9)(9)" ➝ "9999" ➝ 9999
# - Transform #1: 9999 ➝ 9 + 9 + 9 + 9 ➝ 36
# Thus the resulting integer is 36.

class Solution:
    def getLucky(self, s: str, k: int) -> int:
        res=""
        for i in s:
            n=ord(i)-96
            res+=str(n)
        for i in range(k):
            s=0
            for i in res:
                s+=int(i)
            res=str(s)
        return s