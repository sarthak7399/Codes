# https://leetcode.com/problems/find-the-town-judge/description/?envType=daily-question&envId=2024-03-15

# Example 2:
# Input: n = 3, trust = [[1,3],[2,3]]
# Output: 3

# Example 3:
# Input: n = 3, trust = [[1,3],[2,3],[3,1]]
# Output: -1

from typing import List
class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        candidates = [0] * (n + 1)  # Initialize a list to store potential town judges
        for pair in trust:
            candidates[pair[0]] -= 1    # Decrease the trust count for the person making the trust
            candidates[pair[1]] += 1    # Increase the trust count for the person being trusted

        for i in range(1, n + 1):
            if candidates[i] == n - 1:  # If a person is trusted by everyone except themselves
                return i
                
        return -1
