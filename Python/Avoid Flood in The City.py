# https://leetcode.com/problems/avoid-flood-in-the-city/

# Example 2:
# Input: rains = [1,2,0,0,2,1]
# Output: [-1,-1,2,1,-1,-1]
# Explanation: After the first day full lakes are [1]
# After the second day full lakes are [1,2]
# After the third day, we dry lake 2. Full lakes are [1]
# After the fourth day, we dry lake 1. There is no full lakes.
# After the fifth day, full lakes are [2].
# After the sixth day, full lakes are [1,2].
# It is easy that this scenario is flood-free. [-1,-1,1,2,-1,-1] is another acceptable scenario.

from collections import deque

class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        last = {}          # Stores the last day each lake was filled
        q = deque()        # Stores indices (days) when we can dry a lake (rains[i] == 0)
        res = []           # Final result array

        for i, lake in enumerate(rains):
            if lake:       # 🌧️ It rains over lake 'lake'
                if lake in last:
                    # 🧹 Need to dry this lake before today, else flood occurs
                    for j in q:
                        if j > last[lake]:  # Find a dry day after last rain on this lake
                            res[j] = lake    # Use that dry day to dry this lake
                            q.remove(j)
                            break
                    else:
                        return []            # No dry day available → flood unavoidable
                res.append(-1)               # -1 denotes a rainy day (cannot dry)
                last[lake] = i               # Update the last day it rained for this lake
            else:           # ☀️ A dry day — we can dry one lake (to decide later)
                res.append(1)  # Placeholder (we may update this later)
                q.append(i)    # Store this dry day index for future use

        return res
