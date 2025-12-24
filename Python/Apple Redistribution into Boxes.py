# https://leetcode.com/problems/apple-redistribution-into-boxes/

# Example 1:
# Input: apple = [1,3,2], capacity = [4,3,1,5,2]
# Output: 2
# Explanation: We will use boxes with capacities 4 and 5.
# It is possible to distribute the apples as the total capacity is greater than or equal to the total number of apples.

class Solution:
    def minimumBoxes(self, apple: list[int], capacity: list[int]) -> int:
        # Total apples to be packed
        total = sum(apple)

        # Frequency array for box capacities (1 to 50)
        fq = [0] * 51
        high, low = 0, 51

        # Count available boxes of each capacity
        for c in capacity:
            fq[c] += 1
            high = max(high, c)
            low = min(low, c)

        res = 0
        # Use boxes from largest capacity to smallest
        for i in range(high, low - 1, -1):
            while fq[i] > 0 and total > 0:
                total -= i      # Fill apples using this box
                fq[i] -= 1
                res += 1        # One box used

        return res
