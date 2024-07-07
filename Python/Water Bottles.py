# https://leetcode.com/problems/water-bottles/

# Example 1:
# Input: numBottles = 9, numExchange = 3
# Output: 13
# Explanation: You can exchange 3 empty bottles to get 1 full water bottle.
# Number of water bottles you can drink: 9 + 3 + 1 = 13.

class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        totalBottles = numBottles

        while numBottles >= numExchange:
            totalBottles += numBottles // numExchange
            numBottles = numBottles // numExchange + numBottles % numExchange

        return totalBottles