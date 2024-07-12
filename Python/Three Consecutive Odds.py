# https://leetcode.com/problems/three-consecutive-odds/

# Example 1:
# Input: arr = [2,6,4,1]
# Output: false
# Explanation: There are no three consecutive odds.

from typing import List
class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        i=0
        while(i<len(arr)-2):
            if((arr[i]%2!=0) and (arr[i+1]%2!=0) and (arr[i+2]%2!=0)):
                return True
            i+=1
        return False