# https://leetcode.com/problems/maximum-number-of-non-overlapping-substrings/

# Example 1:
# Input: s = "adefaddaccc"
# Output: ["e","f","ccc"]
# Explanation: The following are all the possible substrings that meet the conditions:
# [
#   "adefaddaccc"
#   "adefadda",
#   "ef",
#   "e",
#   "f",
#   "ccc",
# ]
# If we choose the first string, we cannot choose anything else and we'd get only 1. If we choose "adefadda", we are left with "ccc" which is the only one that doesn't overlap, thus obtaining 2 substrings. Notice also, that it's not optimal to choose "ef" since it can be split into two. Therefore, the optimal way is to choose ["e","f","ccc"] which gives us 3 substrings. No other solution of the same number of substrings exist.

class Solution:
    def maxNumOfSubstrings(self, s):
        # Length of the string.
        n = len(s)

        # first[c] = first occurrence of character c.
        # last[c] = last occurrence of character c.
        first = [n] * 26
        last = [-1] * 26

        # Find the first and last occurrence of every character.
        for i, ch in enumerate(s):
            c = ord(ch) - ord('a')
            first[c] = min(first[c], i)
            last[c] = i

        # Store all valid intervals as (right, left).
        intervals = []

        # Try to build a valid substring starting from each character.
        for c in range(26):
            # Skip characters that do not appear in the string.
            if last[c] == -1:
                continue

            # Initially, the interval contains all occurrences
            # of character c.
            l, r = first[c], last[c]
            valid = True

            # Check every character inside the current interval.
            i = l
            while i <= r:
                x = ord(s[i]) - ord('a')

                # If this character appears before l, then its
                # complete range cannot be contained in this interval.
                if first[x] < l:
                    valid = False
                    break

                # The substring must include all occurrences of x,
                # so extend the right boundary if necessary.
                r = max(r, last[x])
                i += 1

            # Add the interval if it contains all occurrences
            # of every character inside it.
            if valid:
                intervals.append((r, l))

        # Sort by ending position so we can greedily choose
        # the earliest-ending non-overlapping intervals.
        intervals.sort()

        # Store the resulting substrings.
        ans = []

        # End position of the previously selected interval.
        prevEnd = -1

        # Select non-overlapping intervals greedily.
        for r, l in intervals:
            # The current interval must start after the previous
            # selected interval has ended.
            if l > prevEnd:
                # Add the corresponding substring to the answer.
                ans.append(s[l:r + 1])

                # Update the end of the last selected interval.
                prevEnd = r

        # Return the maximum set of non-overlapping valid substrings.
        return ans