# https://leetcode.com/problems/divide-players-into-teams-of-equal-skill/

# Example 1:
# Input: skill = [3,2,5,1,3,4]
# Output: 22
# Explanation: 
# Divide the players into the following teams: (1, 5), (2, 4), (3, 3), where each team has a total skill of 6.
# The sum of the chemistry of all the teams is: 1 * 5 + 2 * 4 + 3 * 3 = 5 + 8 + 9 = 22.

from typing import List
class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        # 1. know the target value of two sums
        # 2. divide players.

        n = len(skill)        
        # 1-1. get the edge case
        if n == 2:
            return skill[0] * skill[1]
        
        # 1. check if dividable.
        total_skill = sum(skill)
        if total_skill % (n//2) != 0:
            return -1
        target = total_skill // (n//2)

        # 2. divide players
        skill.sort(reverse=True)
        res = 0
        for i in range(n//2):
            if skill[i] + skill[n-i-1] != target:
                return -1
            res += skill[i] * skill[n-i-1]
        
        return res