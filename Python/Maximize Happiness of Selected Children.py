# https://leetcode.com/problems/maximize-happiness-of-selected-children/

# Example 1:
# Input: happiness = [1,2,3], k = 2
# Output: 4
# Explanation: We can pick 2 children in the following way:
# - Pick the child with the happiness value == 3. The happiness value of the remaining children becomes [0,1].
# - Pick the child with the happiness value == 1. The happiness value of the remaining child becomes [0]. Note that the happiness value cannot become less than 0.
# The sum of the happiness values of the selected children is 3 + 1 = 4.

class Solution:
    def maximumHappinessSum(self, h: List[int], k: int) -> int:
        # Sort happiness values in descending order
        h.sort(reverse=True)
        
        i = 0
        Ans = 0
        
        # Pick up to k people while adjusted happiness is positive
        while k > 0 and h[i] - i > 0:
            Ans += h[i] - i   # Reduce happiness by number of picks already made
            i += 1
            k -= 1
        
        return Ans
