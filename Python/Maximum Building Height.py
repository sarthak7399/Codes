# https://leetcode.com/problems/maximum-building-height/

# Example 1:
# Input: n = 5, restrictions = [[2,1],[4,1]]
# Output: 2
# Explanation: The green area in the image indicates the maximum allowed height for each building.
# We can build the buildings with heights [0,1,2,1,2], and the tallest building has a height of 2.

from typing import List

class Solution:
    def maxBuilding(self, n: int, restrictions: List[List[int]]) -> int:
        # Building 1 must always have height 0
        restrictions.append([1, 0])

        # Sort restrictions by building index
        restrictions.sort()

        # If building n has no restriction,
        # add the maximum possible restriction:
        # height <= n - 1
        if restrictions[-1][0] != n:
            restrictions.append([n, n - 1])

        m = len(restrictions)

        # --------------------------------------------------
        # Left -> Right pass
        # Enforce height difference constraint:
        # height change between adjacent buildings
        # cannot exceed 1
        # --------------------------------------------------
        for i in range(1, m):

            dist = restrictions[i][0] - restrictions[i - 1][0]

            restrictions[i][1] = min(
                restrictions[i][1],
                restrictions[i - 1][1] + dist
            )

        # --------------------------------------------------
        # Right -> Left pass
        # Enforce the same constraint in reverse direction
        # --------------------------------------------------
        for i in range(m - 2, -1, -1):

            dist = restrictions[i + 1][0] - restrictions[i][0]

            restrictions[i][1] = min(
                restrictions[i][1],
                restrictions[i + 1][1] + dist
            )

        # Stores the maximum achievable building height
        ans = 0

        # --------------------------------------------------
        # Find the highest peak possible between every pair
        # of consecutive restricted buildings
        # --------------------------------------------------
        for i in range(1, m):

            x1, h1 = restrictions[i - 1]
            x2, h2 = restrictions[i]

            # Distance between the two restricted buildings
            d = x2 - x1

            # Maximum peak achievable between them.
            # The peak grows from the lower side and then
            # decreases toward the other restriction.
            ans = max(
                ans,
                (h1 + h2 + d) // 2
            )

        return ans