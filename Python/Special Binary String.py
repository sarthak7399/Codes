# https://leetcode.com/problems/special-binary-string/

# Example 1:
# Input: s = "11011000"
# Output: "11100100"
# Explanation: The strings "10" [occuring at s[1]] and "1100" [at s[3]] are swapped.
# This is the lexicographically largest string possible after some number of swaps.

class Solution:
    def makeLargestSpecial(self, s: str) -> str:
        # Base case:
        # empty string has no transformation
        if s == '':
            return ''

        ans = []      # stores valid special substrings
        cnt = 0       # balance counter (1 → +1, 0 → -1)
        i = j = 0     # i → scanning pointer, j → start of current block

        # Traverse the string to split into smallest special substrings
        while i < len(s):

            # Update balance:
            # '1' increases count, '0' decreases count
            cnt += 1 if s[i] == '1' else -1

            # When balance becomes 0 → we found a SPECIAL substring
            # (equal number of 1s and 0s with valid prefix property)
            if cnt == 0:
                # Recursively optimize the inside portion
                # structure of special string:
                #   1 + (inner special string) + 0
                ans.append(
                    '1' + self.makeLargestSpecial(s[j + 1:i]) + '0'
                )

                # Move start pointer to next segment
                j = i + 1

            i += 1

        # Sort substrings in descending order
        # to form lexicographically largest result
        ans.sort(reverse=True)

        # Combine all parts
        return ''.join(ans)