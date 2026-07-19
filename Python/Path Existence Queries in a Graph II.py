# https://leetcode.com/problems/path-existence-queries-in-a-graph-ii/

# Example 1:
# Input: n = 5, nums = [1,8,3,4,2], maxDiff = 3, queries = [[0,3],[2,4]]
# Output: [1,1]
# Explanation:
# The resulting graph is:
# Query	Shortest Path	Minimum Distance
# [0, 3]	0 → 3	1
# [2, 4]	2 → 4	1
# Thus, the output is [1, 1].

from typing import List

class Solution:
    def pathExistenceQueries(
        self,
        n: int,
        nums: List[int],
        maxDiff: int,
        queries: List[List[int]]
    ) -> List[int]:

        # Sort elements while keeping their original indices
        new_nums = sorted(enumerate(nums), key=lambda x: x[1])

        # get_i[original_index] = position in the sorted array
        get_i = [0] * n
        for i, (orig, _) in enumerate(new_nums):
            get_i[orig] = i

        # Binary lifting table
        LOG = 18
        st = [[0] * LOG for _ in range(n)]

        # ----------------------------------------------------
        # Build the first jump table using a sliding window
        #
        # st[i][0] = farthest sorted index reachable
        #            from index i in one jump.
        # ----------------------------------------------------
        r = 0
        for i in range(n):
            if r < i:
                r = i

            while (
                r + 1 < n and
                new_nums[r + 1][1] - new_nums[r][1] <= maxDiff and
                new_nums[r + 1][1] - new_nums[i][1] <= maxDiff
            ):
                r += 1

            st[i][0] = r

        # ----------------------------------------------------
        # Binary lifting preprocessing
        #
        # st[i][j] = position reached after 2^j jumps
        #            starting from index i.
        # ----------------------------------------------------
        for j in range(1, LOG):
            for i in range(n):
                st[i][j] = st[st[i][j - 1]][j - 1]

        ans = []

        # Process each query
        for u, v in queries:

            # Convert original indices to sorted positions
            a = get_i[u]
            b = get_i[v]

            # Always move from left to right
            if a > b:
                a, b = b, a

            # Same element requires no jumps
            if a == b:
                ans.append(0)
                continue

            curr = a
            steps = 0

            # Binary lift to make the largest jumps possible
            # while still staying before b.
            for j in range(LOG - 1, -1, -1):
                if st[curr][j] < b:
                    curr = st[curr][j]
                    steps += (1 << j)

            # One more jump may reach or cross b
            if st[curr][0] >= b:
                ans.append(steps + 1)
            else:
                ans.append(-1)

        return ans