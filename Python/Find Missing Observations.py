# https://leetcode.com/problems/find-missing-observations/

# Example 1:
# Input: rolls = [3,2,4,3], mean = 4, n = 2
# Output: [6,6]
# Explanation: The mean of all n + m rolls is (3 + 2 + 4 + 3 + 6 + 6) / 6 = 4.

from typing import List
class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        target = mean*(n+len(rolls)) - sum(rolls)
        if target>6*n or target<n:
            return []
        x=1
        while x<7 and  x*n < target:
                x+=1    
        y=x-1
        a= target - n*y
        return   [x]*a + [y]*(n-a)
