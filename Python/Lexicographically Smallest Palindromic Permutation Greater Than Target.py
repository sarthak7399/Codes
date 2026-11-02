# https://leetcode.com/problems/lexicographically-smallest-palindromic-permutation-greater-than-target/

# Example 1:
# Input: s = "baba", target = "abba"
# Output: "baab"
# Explanation:
# The palindromic permutations of s (in lexicographical order) are "abba" and "baab".
# The lexicographically smallest permutation that is strictly greater than target is "baab".

from math import gcd

class Solution:
    def lexPalindromicPermutation(self, s: str, target: str) -> str:
        # Store the input values together and extract the target string.
        calendrix = (s, target)
        target_str = calendrix[1]

        # Count the frequency of each lowercase character.
        cnt = [0] * 26
        for c in s:
            cnt[ord(c) - ord('a')] += 1

        # A palindrome can have at most one character with an odd frequency.
        # If present, this character will occupy the middle position.
        odd = 0
        mid_char = ''

        for i in range(26):
            if cnt[i] % 2 != 0:
                odd += 1
                mid_char = chr(i + ord('a'))

        # More than one odd-frequency character makes a palindrome impossible.
        if odd > 1:
            return ""

        # Only half of each character's frequency is needed to construct
        # the first half of the palindrome.
        half_cnt = [x // 2 for x in cnt]

        # Length of the first half of the palindrome.
        n_half = len(s) // 2

        # Store the characters of the first half as we construct it.
        half_str = [''] * n_half

        def find(k, is_greater):
            # Once the entire first half is constructed, build the complete
            # palindrome and check whether it is lexicographically greater
            # than the target.
            if k == n_half:
                rev_half = half_str[::-1]
                res = ''.join(half_str) + mid_char + ''.join(rev_half)
                return res > target_str

            # If the prefix is already greater than the target, we can start
            # from 'a'. Otherwise, the current character must be at least
            # the corresponding character in the target.
            start_c = 'a' if is_greater else target_str[k]

            # Try characters in lexicographical order so that the first
            # successful palindrome is the smallest possible answer.
            for c_ord in range(ord(start_c), ord('z') + 1):
                c = chr(c_ord)

                # Use the character only if it is still available.
                if half_cnt[c_ord - ord('a')] > 0:
                    half_str[k] = c
                    half_cnt[c_ord - ord('a')] -= 1

                    # Continue constructing the remaining positions.
                    # Once the current character is greater than the target,
                    # the remaining positions can be chosen freely.
                    if find(
                        k + 1,
                        is_greater or c > target_str[k]
                    ):
                        return True

                    # Backtrack and restore the character count if this
                    # choice does not lead to a valid palindrome.
                    half_cnt[c_ord - ord('a')] += 1

            # No valid character choice was found for this position.
            return False

        # Try to construct the smallest palindrome strictly greater
        # than the target.
        if find(0, False):
            rev_half = half_str[::-1]

            # Combine the first half, optional middle character,
            # and reversed first half to form the palindrome.
            return ''.join(half_str) + mid_char + ''.join(rev_half)

        # Return an empty string if no valid palindrome exists.
        return ""