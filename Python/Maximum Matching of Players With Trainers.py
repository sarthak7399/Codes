# https://leetcode.com/problems/maximum-matching-of-players-with-trainers/

# Example 1:
# Input: players = [4,7,9], trainers = [8,2,5,8]
# Output: 2
# Explanation:
# One of the ways we can form two matchings is as follows:
# - players[0] can be matched with trainers[0] since 4 <= 8.
# - players[1] can be matched with trainers[3] since 7 <= 8.
# It can be proven that 2 is the maximum number of matchings that can be formed.

from typing import List

class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort()   # Sort players by their required strength
        trainers.sort()  # Sort trainers by their available strength

        j, n = 0, len(trainers)  # j: pointer for trainers, n: total number of trainers

        # Loop through each player in order of increasing strength
        for i, p in enumerate(players):
            # Move the trainer pointer forward until we find a trainer strong enough
            while j < n and trainers[j] < p:
                j += 1

            # If we've run out of trainers, return number of matched players so far (i)
            if j == n:
                return i

            # Match current player p with current trainer trainers[j]
            j += 1

        # All players could be matched, return total number of players
        return len(players)
