# https://leetcode.com/problems/zero-array-transformation-ii/

# Example 1:
# Input: nums = [2,0,2], queries = [[0,2,1],[0,2,1],[1,1,3]]
# Output: 2
# Explanation:
# For i = 0 (l = 0, r = 2, val = 1):
# Decrement values at indices [0, 1, 2] by [1, 0, 1] respectively.
# The array will become [1, 0, 1].

from typing import List
class Solution:
    def minZeroArray(self, a: List[int], queries: List[List[int]]) -> int:
        n = len(a)
        m = len(queries)

        # you have a queue of queries in sorted order
        # only add them into the delta if you need to

        delta = [0] * (n+1)
        q = queries[::-1]

        cur = 0

        for i,x in enumerate(a):

            cur += delta[i]
            
            # keep accepting queries until you are able to satisfy the constraint at a[i]
            while q and cur < x:
                l,r,height = q.pop()

                if r >= i:
                    if l > i:
                        delta[l] += height
                    else: # l <= i
                        cur += height
                    delta[r+1] -= height
                
            if cur < x:
                return -1
            
        return m - len(q)