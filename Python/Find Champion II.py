# https://leetcode.com/problems/find-champion-ii/

# Example 2:
# Input: n = 4, edges = [[0,2],[1,3],[1,2]]
# Output: -1
# Explanation: Team 2 is weaker than team 0 and team 1. Team 3 is weaker than team 1. But team 1 and team 0 are not weaker than any other teams. So the answer is -1.

from typing import List
class Solution:
    def findChampion(self, num_teams: int, match_results: List[List[int]]) -> int:
        # Initialize a list to keep track of whether each team is undefeated.
        # True indicates the team is undefeated.
        undefeated_teams = [True] * num_teams
        
        # Iterate through the match results to mark losing teams as defeated.
        for winner, loser in match_results:
            undefeated_teams[loser] = False  # Mark the loser team as defeated.
            
        # Variable to store the potential champion's team index.
        potential_champion = -1
        
        # Count the number of undefeated teams.
        undefeated_count = 0
        
        # Check each team to see if it is undefeated.
        for team in range(num_teams):
            if undefeated_teams[team]:
                # Update the potential champion and increment the count.
                potential_champion = team
                undefeated_count += 1
                
        # If there is exactly one undefeated team, return it as the champion.
        if undefeated_count == 1:
            return potential_champion
            
        # If there are no undefeated teams or multiple undefeated teams, return -1.
        return -1
