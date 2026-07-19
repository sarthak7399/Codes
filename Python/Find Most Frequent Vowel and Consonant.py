# https://leetcode.com/problems/find-most-frequent-vowel-and-consonant/

# Example 1:
# Input: s = "successes"
# Output: 6
# Explanation:
# The vowels are: 'u' (frequency 1), 'e' (frequency 2). The maximum frequency is 2.
# The consonants are: 's' (frequency 4), 'c' (frequency 2). The maximum frequency is 4.
# The output is 2 + 4 = 6.

class Solution:
    def maxFreqSum(self, s: str) -> int:
        con = 0  # max frequency of any consonant
        vow = 0  # max frequency of any vowel
        d_set = set(s)  # unique characters in the string

        for i in d_set:
            if i in "aeiou":  
                # check vowel frequency and update max
                vow = max(vow, s.count(i))
            else:
                # check consonant frequency and update max
                con = max(con, s.count(i))

        # return sum of the most frequent vowel + most frequent consonant
        return con + vow
