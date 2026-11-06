# https://leetcode.com/problems/find-the-distance-value-between-two-arrays/

# Example 1:
# Input: arr1 = [4,5,8], arr2 = [10,9,1,8], d = 2
# Output: 2
# Explanation: 
# For arr1[0]=4 we have: 
# |4-10|=6 > d=2 
# |4-9|=5 > d=2 
# |4-1|=3 > d=2 
# |4-8|=4 > d=2 
# For arr1[1]=5 we have: 
# |5-10|=5 > d=2 
# |5-9|=4 > d=2 
# |5-1|=4 > d=2 
# |5-8|=3 > d=2
# For arr1[2]=8 we have:
# |8-10|=2 <= d=2
# |8-9|=1 <= d=2
# |8-1|=7 > d=2
# |8-8|=0 <= d=2

from typing import List

class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        def far(a):  # Check whether no element in arr2 is within distance d of a.
            # Return True only if the absolute difference from every b is greater than d.
            return all(abs(a - b) > d for b in arr2)

        # Count the elements in arr1 that satisfy the distance condition.
        return sum(map(far, arr1))