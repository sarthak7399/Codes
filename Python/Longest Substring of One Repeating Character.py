# https://leetcode.com/problems/longest-substring-of-one-repeating-character/

# Example 1:
# Input: s = "babacc", queryCharacters = "bcb", queryIndices = [1,3,3]
# Output: [3,3,4]
# Explanation: 
# - 1st query updates s = "bbbacc". The longest substring consisting of one repeating character is "bbb" with length 3.
# - 2nd query updates s = "bbbccc". 
#   The longest substring consisting of one repeating character can be "bbb" or "ccc" with length 3.
# - 3rd query updates s = "bbbbcc". The longest substring consisting of one repeating character is "bbbb" with length 4.
# Thus, we return [3,3,4].

from itertools import accumulate, groupby
from typing import List

from sortedcontainers import SortedList


class Solution:
    def longestRepeating(
        self,
        s: str,
        queryCharacters: str,
        queryIndices: List[int]
    ) -> List[int]:

        # Convert the string into a list so that individual
        # characters can be updated efficiently.
        s, n = list(s), len(s)

        # Find the lengths of all consecutive groups/runs.
        # Example: "aaabbc" -> [3, 2, 1]
        runs = [len(list(g)) for _, g in groupby(s)]

        # Store the starting index of every run.
        # accumulate(runs, initial=0) gives the boundaries between runs.
        starts = SortedList(accumulate(runs, initial=0))

        # Store all run lengths as a multiset.
        # The largest value in this structure is the current
        # longest repeating substring.
        lens = SortedList(runs)

        def add_break(p):
            # Add a new boundary at position p.
            # Find the run that currently contains this position.
            j = starts.bisect_left(p)

            # Get the existing run boundaries.
            l, r = starts[j - 1], starts[j]

            # Insert the new boundary.
            starts.add(p)

            # The old run [l, r) is split into two smaller runs.
            lens.remove(r - l)
            lens.add(p - l)
            lens.add(r - p)

        def remove_break(p):
            # Remove an existing boundary at position p.
            j = starts.bisect_left(p)

            # Get the boundaries on both sides of p.
            l, r = starts[j - 1], starts[j + 1]

            # Remove the boundary.
            starts.pop(j)

            # Remove the two smaller runs created by this boundary.
            lens.remove(p - l)
            lens.remove(r - p)

            # Merge them back into one larger run.
            lens.add(r - l)

        result = []

        # Process each character update along with its index.
        for i, c in zip(queryIndices, queryCharacters):

            # Only process the update if the character actually changes.
            if c != (old := s[i]):

                # Check the two possible boundaries around index i:
                # p = i     -> boundary between i-1 and i
                # p = i + 1 -> boundary between i and i+1
                for p, nb in ((i, i - 1), (i + 1, i + 1)):

                    # Make sure the neighbouring index is valid.
                    if 0 <= nb < n:

                        # If the neighbour had the old character,
                        # changing s[i] breaks the existing run.
                        if s[nb] == old:
                            add_break(p)

                        # If the neighbour has the new character,
                        # changing s[i] removes the boundary between them.
                        elif s[nb] == c:
                            remove_break(p)

                # Apply the character update.
                s[i] = c

            # The largest run length is the answer after this update.
            result.append(lens[-1])

        return result