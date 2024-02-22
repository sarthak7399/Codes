# https://leetcode.com/problems/greatest-common-divisor-of-strings/submissions/1154746817/?envType=study-plan-v2&envId=leetcode-75

# Example 1:
# Input: str1 = "ABABAB", str2 = "ABAB"
# Output: "AB"

# Example 2:
# Input: str1 = "LEET", str2 = "CODE"
# Output: ""

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1+str2 != str2+str1:
            return ""
        gcd = lambda a, b: a if b == 0 else gcd(b, a%b) # equivalent to below func
        # def hcf(a, b):
        #     if(b == 0):
        #         return a
        #     else:
        #         return hcf(b, a % b)
        divisor = gcd(len(str1), len(str2))
        return str1[:divisor]