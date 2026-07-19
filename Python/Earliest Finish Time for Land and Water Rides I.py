# https://leetcode.com/problems/earliest-finish-time-for-land-and-water-rides-i/

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

        # Stores the minimum possible finishing time
        ans = float('inf')

        n = len(landStartTime)
        m = len(waterStartTime)

        # Try every land ride with every water ride
        for i in range(n):
            for j in range(m):

                # ---------- Option 1: Land -> Water ----------

                # Time when the land ride finishes
                land_finish = landStartTime[i] + landDuration[i]

                # Water ride can start only after:
                # 1. Land ride is completed
                # 2. Water ride's own start time
                finish1 = max(land_finish, waterStartTime[j]) + waterDuration[j]

                # ---------- Option 2: Water -> Land ----------

                # Time when the water ride finishes
                water_finish = waterStartTime[j] + waterDuration[j]

                # Land ride can start only after:
                # 1. Water ride is completed
                # 2. Land ride's own start time
                finish2 = max(water_finish, landStartTime[i]) + landDuration[i]

                # Update earliest possible finish time
                ans = min(ans, finish1, finish2)

        return ans