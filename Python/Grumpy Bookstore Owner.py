# https://leetcode.com/problems/grumpy-bookstore-owner/

# Example 1:
# Input: customers = [1,0,1,2,1,1,7,5], grumpy = [0,1,0,1,0,1,0,1], minutes = 3
# Output: 16
# Explanation: The bookstore owner keeps themselves not grumpy for the last 3 minutes. 
# The maximum number of customers that can be satisfied = 1 + 1 + 1 + 1 + 7 + 5 = 16.

class Solution:
    def maxSatisfied(self, customers: list, grumpy: list, minutes: int) -> int:
        n = len(customers)
        ans = 0
        for i in range(n):
            if grumpy[i] == 0:
                ans += customers[i]
        
        unsatis = 0
        for i in range(minutes):
            if grumpy[i] == 1:
                unsatis += customers[i]
        
        max_ = unsatis
        for i in range(minutes, n):
            if grumpy[i - minutes] == 1:
                unsatis -= customers[i - minutes]
            if grumpy[i] == 1:
                unsatis += customers[i]
            max_ = max(max_, unsatis)
        
        return ans + max_