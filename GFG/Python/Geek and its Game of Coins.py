# https://www.geeksforgeeks.org/problems/geek-and-its-game-of-coins

# Example 1:
# Input: # n = 5, x = 3, y = 4
# Output: 1
# Explanation:
# There are 5 coins, every player can pick 1 or 3 or 4 coins on his/her turn. Geek can win by picking 3 coins in first chance. Now 2 coins will be left so his friend will pick one coin and now Geek can win by picking the last coin.

class Solution:
    def findWinner(self, n : int, x : int, y : int) -> int:
        # code here
        # Initialize dp array with False, meaning initially assume Geek can't win
        dp = [False] * (n + 1)
        
        # Base case: if there are 0 coins, Geek cannot win
        dp[0] = False
        
        # Fill the dp array
        for i in range(1, n + 1):
            # Check if Geek can pick 1 coin and leave opponent in a losing state
            if i >= 1 and not dp[i - 1]:
                dp[i] = True
            # Check if Geek can pick x coins and leave opponent in a losing state
            elif i >= x and not dp[i - x]:
                dp[i] = True
            # Check if Geek can pick y coins and leave opponent in a losing state
            elif i >= y and not dp[i - y]:
                dp[i] = True
        
        # The result is whether Geek can win with n coins
        return 1 if dp[n] else 0
