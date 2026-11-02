# https://leetcode.com/problems/lexicographically-smallest-permutation-greater-than-target/

# Example 1:
# Input: s = "abc", target = "bba"
# Output: "bca"
# Explanation:
# The permutations of s (in lexicographical order) are "abc", "acb", "bac", "bca", "cab", and "cba".
# The lexicographically smallest permutation that is strictly greater than target is "bca".

class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        # Count the frequency of each character in s.
        count = [0] * 26
        for ch in s:
            count[ord(ch) - ord('a')] += 1

        # Length of the permutation to construct.
        n = len(s)

        # Find how much of target can be matched exactly
        # using the available characters from s.
        matched = 0

        while (
            matched < n
            and count[ord(target[matched]) - ord('a')] > 0
        ):
            # Use the matching character.
            count[ord(target[matched]) - ord('a')] -= 1
            matched += 1

        # Start searching from the first unmatched position.
        # If target was fully matched, start from the last position
        # to find the next lexicographically greater permutation.
        start = matched if matched < n else n - 1

        # Try to increase a character, starting from right to left,
        # so that the resulting permutation is the smallest one
        # lexicographically greater than target.
        for i in range(start, -1, -1):

            # Restore the character at this position because we are
            # backtracking and will try a different character here.
            if i < matched:
                count[ord(target[i]) - ord('a')] += 1

            # Find the smallest available character greater than
            # target[i].
            bigger = -1

            for ch in range(ord(target[i]) - ord('a') + 1, 26):
                if count[ch] > 0:
                    bigger = ch
                    break

            # If a larger character is available, use it at position i.
            if bigger != -1:
                count[bigger] -= 1

                # Keep the prefix same as target and place the smallest
                # possible larger character at the current position.
                answer = target[:i] + chr(ord('a') + bigger)

                # Append all remaining characters in sorted order to make
                # the final permutation as small as possible.
                for ch in range(26):
                    answer += chr(ord('a') + ch) * count[ch]

                return answer

        # Return an empty string if no permutation greater than target exists.
        return ""