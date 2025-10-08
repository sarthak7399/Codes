# https://leetcode.com/problems/successful-pairs-of-spells-and-potions/

# Example 1:
# Input: spells = [5,1,3], potions = [1,2,3,4,5], success = 7
# Output: [4,0,3]
# Explanation:
# - 0th spell: 5 * [1,2,3,4,5] = [5,10,15,20,25]. 4 pairs are successful.
# - 1st spell: 1 * [1,2,3,4,5] = [1,2,3,4,5]. 0 pairs are successful.
# - 2nd spell: 3 * [1,2,3,4,5] = [3,6,9,12,15]. 3 pairs are successful.
# Thus, [4,0,3] is returned.

from collections import Counter
from itertools import accumulate

class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        freq = Counter(potions)               # 🔢 Count frequency of each potion strength
        pMax = max(freq)                      # 🧪 Find maximum potion strength
        
        F = [0] * (1 + pMax)                  # Frequency array (index = potion strength)
        for p, f in freq.items():             # Fill the frequency array
            F[p] = f
        
        freq = list(accumulate(F))            # Prefix sum → freq[i] = no. of potions ≤ i
        n, m = len(spells), len(potions)
        res = [0] * n                         # Result array for each spell
        
        for i, x in enumerate(spells):        # For every spell power x
            k = (success + x - 1) // x        # Minimum potion power needed to succeed
            if k <= pMax:                     # If such potions exist
                res[i] = m - freq[k - 1]      # Potions ≥ k = total - potions < k
        
        return res                            # ✅ Return count of successful pairs for each spell
