# https://leetcode.com/problems/minimum-number-of-people-to-teach/

# Example 1:
# Input: n = 2, languages = [[1],[2],[1,2]], friendships = [[1,2],[1,3],[2,3]]
# Output: 1
# Explanation: You can either teach user 1 the second language or user 2 the first language.

from typing import List

class Solution:
    def minimumTeachings(self, n: int, languages: List[List[int]], friendships: List[List[int]]) -> int:
        # `n` = number of possible languages
        # `languages[i]` = list of languages known by user i (1-indexed in input)
        # `friendships` = list of pairs [u, v] representing friendships
        
        # Step 1: Identify all users who *need new teaching*
        # A user needs teaching if they have at least one friend
        # with whom they cannot communicate (no common language).
        need = set()  # set of users who must be considered for teaching
        
        for u, v in friendships:
            u -= 1  # adjust to 0-indexing
            v -= 1
            ok = False
            # Check if users u and v already share a language
            for x in languages[u]:
                if x in languages[v]:
                    ok = True
                    break
            # If no common language, both u and v must be candidates for teaching
            if not ok:
                need.add(u)
                need.add(v)

        # Step 2: Try teaching each possible language (1..n) 
        # and compute the minimum number of people to teach
        ans = len(languages) + 1  # start with a large upper bound
        
        for i in range(1, n + 1):  # iterate over all languages
            cans = 0  # number of people we need to teach if we pick language i
            for v in need:
                # If user v does not know language i, we must teach them
                if i not in languages[v]:
                    cans += 1
            ans = min(ans, cans)  # minimize across all possible languages
        
        return ans
