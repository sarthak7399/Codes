# https://leetcode.com/problems/earliest-finish-time-for-land-and-water-rides-ii/

# Example 1:
# Input: landStartTime = [2,8], landDuration = [4,1], waterStartTime = [6], waterDuration = [3]
# Output: 9
# Explanation:​​​​​​​
# Plan A (land ride 0 → water ride 0):
# Start land ride 0 at time landStartTime[0] = 2. Finish at 2 + landDuration[0] = 6.
# Water ride 0 opens at time waterStartTime[0] = 6. Start immediately at 6, finish at 6 + waterDuration[0] = 9.
# Plan B (water ride 0 → land ride 1):
# Start water ride 0 at time waterStartTime[0] = 6. Finish at 6 + waterDuration[0] = 9.
# Land ride 1 opens at landStartTime[1] = 8. Start at time 9, finish at 9 + landDuration[1] = 10.
# Plan C (land ride 1 → water ride 0):
# Start land ride 1 at time landStartTime[1] = 8. Finish at 8 + landDuration[1] = 9.
# Water ride 0 opened at waterStartTime[0] = 6. Start at time 9, finish at 9 + waterDuration[0] = 12.
# Plan D (water ride 0 → land ride 0):
# Start water ride 0 at time waterStartTime[0] = 6. Finish at 6 + waterDuration[0] = 9.
# Land ride 0 opened at landStartTime[0] = 2. Start at time 9, finish at 9 + landDuration[0] = 13.
# Plan A gives the earliest finish time of 9.

from typing import List

class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
        # Minimum finishing time found so far
        ans = float("inf")

        # Earliest possible completion time among all land rides
        mln = float("inf")

        # Earliest possible completion time among all water rides
        mnw = float("inf")

        # Find the earliest finishing land ride
        for i in range(len(landStartTime)):
            mln = min(
                mln,
                landStartTime[i] + landDuration[i]
            )

        # Try taking the earliest-finishing land ride first,
        # then each water ride
        for i in range(len(waterStartTime)):
            ans = min(
                ans,
                max(mln, waterStartTime[i]) + waterDuration[i]
            )

        # Find the earliest finishing water ride
        for i in range(len(waterStartTime)):
            mnw = min(
                mnw,
                waterStartTime[i] + waterDuration[i]
            )

        # Try taking the earliest-finishing water ride first,
        # then each land ride
        for i in range(len(landStartTime)):
            ans = min(
                ans,
                max(mnw, landStartTime[i]) + landDuration[i]
            )

        # Return the minimum overall finishing time
        return ans