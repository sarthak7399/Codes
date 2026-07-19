# https://leetcode.com/problems/find-the-minimum-amount-of-time-to-brew-potions/

# Example 1:
# Input: skill = [1,5,2,4], mana = [5,1,4,2]
# Output: 110
# Explanation:
# Potion Number	Start time	Wizard 0 done by	Wizard 1 done by	Wizard 2 done by	Wizard 3 done by
# 0	0	5	30	40	60
# 1	52	53	58	60	64
# 2	54	58	78	86	102
# 3	86	88	98	102	110
# As an example for why wizard 0 cannot start working on the 1st potion before time t = 52, consider the case where the wizards started preparing the 1st potion at time t = 50. At time t = 58, wizard 2 is done with the 1st potion, but wizard 3 will still be working on the 0th potion till time t = 60.

from typing import List

class Solution:
    def minTime(self, skills: List[int], energy: List[int]) -> int:
        n, m = len(skills), len(energy)
        prefix_skills = [0] * n
        
        # 🧮 Compute prefix sum of skills
        for i in range(1, n):
            prefix_skills[i] = prefix_skills[i - 1] + skills[i]

        # 🏁 Initial total time for first skill-energy pair
        total_time = skills[0] * energy[0]

        # 🔁 Calculate max time for each energy level
        for j in range(1, m):
            max_time = skills[0] * energy[j]
            for i in range(1, n):
                # Compare current skill group vs previous energy level
                diff_time = prefix_skills[i] * energy[j - 1] - prefix_skills[i - 1] * energy[j]
                if diff_time > max_time:
                    max_time = diff_time
            total_time += max_time

        # ➕ Add final segment contribution
        return total_time + prefix_skills[-1] * energy[-1]
