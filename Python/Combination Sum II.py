# https://leetcode.com/problems/combination-sum-ii/

# Example 1:
# Input: candidates = [10,1,2,7,6,1,5], target = 8
# Output: 
# [
# [1,1,6],
# [1,2,5],
# [1,7],
# [2,6]
# ]

from typing import List
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
         candidates.sort()
         res = []

         def dfs(target, start, comb):
             if target < 0:
                 return
             if target == 0:
                 res.append(comb)
                 return
             for i in range(start, len(candidates)):
                 if i > start and candidates[i] == candidates[i-1]:
                     continue
                 if candidates[i] > target:
                     break
                 dfs(target-candidates[i], i+1, comb+[candidates[i]])

         dfs(target, 0, [])
         return res