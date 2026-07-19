# https://leetcode.com/problems/water-bottles-ii/

# Example 1:
# Input: numBottles = 13, numExchange = 6
# Output: 15
# Explanation: The table above shows the number of full water bottles, empty water bottles, the value of numExchange, and the number of bottles drunk.

class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        res = numBottles   # total bottles drunk initially
        emp = numBottles   # empty bottles available after drinking

        # keep exchanging while enough empty bottles exist
        while emp >= numExchange:
            emp -= numExchange   # spend bottles for exchange
            res += 1             # drink new bottle
            emp += 1             # new empty bottle added back
            numExchange += 1     # exchange requirement increases each time

        return res               # total bottles drunk
