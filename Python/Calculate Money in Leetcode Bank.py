# https://leetcode.com/problems/calculate-money-in-leetcode-bank/

# Example 1:
# Input: n = 4
# Output: 10
# Explanation: After the 4th day, the total is 1 + 2 + 3 + 4 = 10.

class Solution:
    def totalMoney(self, n: int) -> int:
        monday = 0     # Tracks the amount deposited on Monday (increases weekly)
        count = 0      # Tracks days in the current week (1 to 7)
        total = 0      # Stores total amount deposited

        for i in range(1, n + 1):        # Loop through each day
            if count == 7:               # If a week is completed
                monday = i // 7 + 1      # Next Monday starts with one more dollar
                count = 0                # Reset the day counter for new week
            else:
                monday += 1              # Increment daily deposit amount

            total += monday              # Add today’s deposit to total
            count += 1                   # Move to next day

        return total                     # Return total amount after n days
