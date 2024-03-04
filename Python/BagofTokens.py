# https://leetcode.com/problems/bag-of-tokens/description/?envType=daily-question&envId=2024-03-04

# Example 1:
# Input: tokens = [100], power = 50
# Output: 0
# Explanation: Since your score is 0 initially, you cannot play the token face-down. You also cannot play it face-up since your power (50) is less than tokens[0] (100).

# Example 3:
# Input: tokens = [100,200,300,400], power = 200
# Output: 2
# Explanation: Play the tokens in this order to get a score of 2:
# Play token0 (100) face-up, reducing power to 100 and increasing score to 1.
# Play token3 (400) face-down, increasing power to 500 and reducing score to 0.
# Play token1 (200) face-up, reducing power to 300 and increasing score to 1.
# Play token2 (300) face-up, reducing power to 0 and increasing score to 2.
# The maximum score achievable is 2.

from typing import List
class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()
        n, score, max_score, left, right = len(tokens), 0, 0, 0, len(tokens)-1
        
        while left <= right:            
            if power >= tokens[left]:   # If we have enough power to use the token at left pointer  
                power -= tokens[left]   # Use the token, increment score, and update power and left pointer
                score += 1
                left += 1
                max_score = max(max_score, score)
            
            elif score > 0:     # If we can trade tokens for power                
                power += tokens[right]      # Trade token for power, decrement score, and update power and right pointer
                score -= 1
                right -= 1
            else:
                break

        return max_score