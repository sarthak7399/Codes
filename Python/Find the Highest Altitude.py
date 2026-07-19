# https://leetcode.com/problems/find-the-highest-altitude/

# Example 1:
# Input: gain = [-5,1,5,0,-7]
# Output: 1
# Explanation: The altitudes are [0,-5,-4,1,1,-6]. The highest is 1.

from typing import List

class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        # Maximum altitude reached so far.
        # Start with 0 because the biker begins at altitude 0.
        ans = 0

        # Create a copy of gain to store prefix sums
        vect2 = []

        for i in range(len(gain)):
            vect2.append(gain[i])

        # Convert vect2 into prefix sums
        # vect2[i] represents altitude after the i-th segment
        for i in range(1, len(gain)):
            vect2[i] = vect2[i] + vect2[i - 1]

        # Find the maximum altitude reached
        for i in range(len(gain)):
            if ans < vect2[i]:
                ans = vect2[i]

        return ans