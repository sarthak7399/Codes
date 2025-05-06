# https://leetcode.com/problems/number-of-equivalent-domino-pairs/

# Example 1:
# Input: dominoes = [[1,2],[2,1],[3,4],[5,6]]
# Output: 1

class Solution:
    def numEquivDominoPairs(self, dominoes):
        from collections import defaultdict

        # Dictionary to count equivalent domino occurrences.
        # Dominoes like [1,2] and [2,1] are considered the same, so we use sorted tuples as keys.
        count_map = defaultdict(int)
        count = 0

        # Iterate through each domino
        for a, b in dominoes:
            # Sort the pair to handle unordered equivalence (e.g., [1,2] == [2,1])
            key = tuple(sorted((a, b)))
            count_map[key] += 1

        # For each unique domino configuration, count the number of pairs possible
        # If a domino occurs `freq` times, the number of pairs is freq * (freq - 1) / 2
        for freq in count_map.values():
            count += freq * (freq - 1) // 2

        return count
