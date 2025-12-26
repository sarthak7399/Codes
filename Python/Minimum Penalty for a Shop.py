# https://leetcode.com/problems/minimum-penalty-for-a-shop/

# Example 1:
# Input: customers = "YYNY"
# Output: 2
# Explanation: 
# - Closing the shop at the 0th hour incurs in 1+1+0+1 = 3 penalty.
# - Closing the shop at the 1st hour incurs in 0+1+0+1 = 2 penalty.
# - Closing the shop at the 2nd hour incurs in 0+0+0+1 = 1 penalty.
# - Closing the shop at the 3rd hour incurs in 0+0+1+1 = 2 penalty.
# - Closing the shop at the 4th hour incurs in 0+0+1+0 = 1 penalty.
# Closing the shop at 2nd or 4th hour gives a minimum penalty. Since 2 is earlier, the optimal closing time is 2.

# Method 1: Greedy
# Time: O(n)
# Space: O(1)
class Solution:
    def bestClosingTime(self, customers: str) -> int:
        # Initial penalty: all 'Y' customers are unhappy if shop closes at time 0
        pen = customers.count('Y')
        best = pen
        ans = 0

        # Try closing at each hour
        for i, c in enumerate(customers):
            if c == 'Y':
                pen -= 1      # One less unhappy customer after this hour
            else:
                pen += 1      # One more unhappy customer if closed before this hour

            # Update best (minimum) penalty and closing time
            if pen < best:
                best = pen
                ans = i + 1

        return ans


# # Method 2: Prefix and Suffix Counts
# # Time: O(n)
# # Space: O(n)
# def bestClosingTime(s: str) -> int:
#     n = len(s)
    
#     # prefixN[i]: number of 'N' in s[0 : i]
#     prefixN = [0] * (n + 1)
#     # suffixY[i]: number of 'Y' in s[i : n]
#     suffixY = [0] * (n + 1)

#     # Build prefix count of 'N'
#     for i in range(1, n + 1):
#         prefixN[i] = prefixN[i - 1]
#         if s[i - 1] == 'N':
#             prefixN[i] += 1

#     # Build suffix count of 'Y'
#     for i in range(n - 1, -1, -1):
#         suffixY[i] = suffixY[i + 1]
#         if s[i] == 'Y':
#             suffixY[i] += 1

#     best = float('inf')
#     ans = 0

#     # Try closing at every time j
#     for j in range(n + 1):
#         # Penalty = unhappy 'N' before j + unhappy 'Y' after j
#         pen = prefixN[j] + suffixY[j]
#         if pen < best:
#             best = pen
#             ans = j

#     return ans
