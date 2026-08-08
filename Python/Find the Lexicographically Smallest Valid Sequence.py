# https://leetcode.com/problems/find-the-lexicographically-smallest-valid-sequence/

# Example 1:
# Input: word1 = "vbcca", word2 = "abc"
# Output: [0,1,2]
# Explanation:
# The lexicographically smallest valid sequence of indices is [0, 1, 2]:
# Change word1[0] to 'a'.
# word1[1] is already 'b'.
# word1[2] is already 'c'.


from typing import List

class Solution:
    def validSequence(self, word1: str, word2: str) -> List[int]:
        n, m = len(word1), len(word2)

        # last[j] stores the latest index in word1 where
        # word2[j] can be matched while still completing
        # the remaining suffix of word2.
        last = [-1] * m
        j = m - 1

        # Scan word1 from right to left to build the suffix information.
        for i in range(n - 1, -1, -1):
            if j >= 0 and word1[i] == word2[j]:
                last[j] = i
                j -= 1

        # Store the selected indices from word1.
        res = []

        # j = current position in word2.
        # skip = number of characters skipped/mismatched so far.
        # At most one mismatch is allowed.
        skip = j = 0

        for i, c in enumerate(word1):

            # All characters of word2 have been matched.
            if j == m:
                break

            # Choose the current index if:
            # 1. The character directly matches word2[j], or
            # 2. We have not used the allowed mismatch yet, and
            #    choosing this index still leaves enough characters
            #    to match the rest of word2.
            if c == word2[j] or skip == 0 and (
                j == m - 1 or i < last[j + 1]
            ):
                # Record whether this match uses the one allowed mismatch.
                skip += c != word2[j]

                # Add the selected index to the result.
                res.append(i)

                # Move to the next character of word2.
                j += 1

        # Return the selected indices only if the entire word2
        # has been successfully matched.
        return res if j == m else []