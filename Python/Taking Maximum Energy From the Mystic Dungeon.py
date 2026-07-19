# https://leetcode.com/problems/taking-maximum-energy-from-the-mystic-dungeon/

# Example 1:
# Input: energy = [5,2,-10,-5,1], k = 3
# Output: 3
# Explanation: We can gain a total energy of 3 by starting from magician 1 absorbing 2 + 1 = 3.

class Solution:
    def maximumEnergy(self, energy: list[int], k: int) -> int:
        n = len(energy)
        ans = float('-inf')
        
        # 🔁 Start from last k elements and move backwards
        for i in range(n - k, n):
            s = 0
            # ⬅️ Move backwards by steps of size k
            for j in range(i, -1, -k):
                s += energy[j]
                ans = max(ans, s)
                
        return ans
