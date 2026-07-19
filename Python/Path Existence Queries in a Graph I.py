# https://leetcode.com/problems/path-existence-queries-in-a-graph-i/

# Example 1:
# Input: n = 2, nums = [1,3], maxDiff = 1, queries = [[0,0],[0,1]]
# Output: [true,false]
# Explanation:
# Query [0,0]: Node 0 has a trivial path to itself.
# Query [0,1]: There is no edge between Node 0 and Node 1 because |nums[0] - nums[1]| = |1 - 3| = 2, which is greater than maxDiff.
# Thus, the final answer after processing all the queries is [true, false].

from typing import List

class Solution:
    def pathExistenceQueries(
        self,
        n: int,
        nums: List[int],
        maxDiff: int,
        queries: List[List[int]]
    ) -> List[bool]:

        # prev = previous element in the sorted array
        # cid  = current connected component id
        qz, prev, cid = len(queries), -1, 0

        # comp[i] stores the component id of nums[i]
        comp = [-1] * n

        # Assign a component id to every element
        for i, curr in enumerate(nums):

            # If the gap between consecutive elements exceeds maxDiff,
            # a new connected component starts.
            cid += (prev + maxDiff < curr)

            comp[i] = cid
            prev = curr

        # Two indices are connected if they belong
        # to the same connected component.
        return [comp[x] == comp[y] for x, y in queries]