# https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/?envType=study-plan-v2&envId=leetcode-75&__cf_chl_tk=HyYodGpGHXln3lCBwgSgMz5Mt5F17V1WwKfbVKqTu9I-1706898763-0-gaNycGzNElA

# Example 1:
# Input: s = "abciiidef", k = 3
# Output: 3
# Explanation: The substring "iii" contains 3 vowel letters.

class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        count, ans, vowels = 0, 0, "aeiou"

        for letter in s[:k]:
            if letter in vowels: count += 1
        ans = count

        for i in range(k, len(s)): 
            if s[i-k] in vowels: count -= 1
            if s[i] in vowels: count += 1
            ans = max(ans, count)
        return ans