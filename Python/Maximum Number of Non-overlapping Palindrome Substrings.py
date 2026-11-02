# https://leetcode.com/problems/maximum-number-of-non-overlapping-palindrome-substrings/

# Example 1:
# Input: s = "abaccdbbd", k = 3
# Output: 2
# Explanation: We can select the substrings underlined in s = "abaccdbbd". Both "aba" and "dbbd" are palindromes and have a length of at least k = 3.
# It can be shown that we cannot find a selection with more than two valid substrings.

class Solution:
    def maxPalindromes(self, S: str, k: int) -> int:
        # n = length of the string.
        # i = current starting index.
        # res = maximum number of non-overlapping palindromes found.
        n, i, res = len(S), 0, 0

        # Continue while there are at least k characters remaining.
        while i <= n - k:

            # Only lengths k and k + 1 need to be checked.
            # Any longer palindrome can be reduced to one of these
            # lengths while maintaining the required condition.
            for l in [k, k + 1]:

                # Make sure the substring of length l fits in the string.
                if i + l <= n:

                    # A string is a palindrome if it is equal to its reverse.
                    if S[i:i+l] == S[i:i+l][::-1]:
                        # Found a valid palindrome.
                        res += 1

                        # Move i to the end of the selected palindrome.
                        # l - 1 is added here because i is incremented
                        # once again after the loop.
                        i += (l - 1)
                        break

            # Move to the next available position.
            i += 1

        # Return the maximum number of non-overlapping palindromes.
        return res