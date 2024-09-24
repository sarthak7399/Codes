# https://leetcode.com/problems/find-the-length-of-the-longest-common-prefix/

# Example 1:
# Input: arr1 = [1,10,100], arr2 = [1000]
# Output: 3
# Explanation: There are 3 pairs (arr1[i], arr2[j]):
# - The longest common prefix of (1, 1000) is 1.
# - The longest common prefix of (10, 1000) is 10.
# - The longest common prefix of (100, 1000) is 100.
# The longest common prefix is 100 with a length of 3.

from typing import List
class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        X, Y = len(arr1), len(arr2)

        s = set()
        for i in arr2:
            copy = i
            # 12345 -> 1, 12, 123, 1234, 12345
            s.add(copy)
            copy = copy // 10
            while copy > 0:
                s.add(copy)
                copy = copy // 10
        
        t = set()
        for i in arr1:
            copy = i
            # 12345 -> 1, 12, 123, 1234, 12345
            t.add(copy)
            copy = copy // 10
            while copy > 0:
                t.add(copy)
                copy = copy // 10
                
        ans = 0
        for i in t:
            if i in s:
                ans = max(ans, len(str(i)))
                
        return ans