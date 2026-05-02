# https://leetcode.com/problems/rotated-digits/

# Example 1:
# Input: n = 10
# Output: 4
# Explanation: There are four good numbers in the range [1, 10] : 2, 5, 6, 9.
# Note that 1 and 10 are not good numbers, since they remain unchanged after rotating.

class Solution:
    def rotatedDigits(self, n: int) -> int:
        # dp[i] states:
        # 0 → invalid after rotation
        # 1 → valid but unchanged after rotation
        # 2 → valid and changes to a different number (good number)
        dp = [0] * (n + 1)

        count = 0  # Count of good numbers

        # Process every number from 0 to n
        for i in range(n + 1):

            # Base case: single-digit numbers
            if i < 10:
                if i in (0, 1, 8):
                    # Valid but unchanged
                    dp[i] = 1

                elif i in (2, 5, 6, 9):
                    # Valid and changes after rotation
                    dp[i] = 2
                    count += 1

                else:
                    # Invalid digits (3,4,7)
                    dp[i] = 0

            else:
                # Split number into prefix and last digit
                a = dp[i // 10]
                b = dp[i % 10]

                # Both parts valid but unchanged
                if a == 1 and b == 1:
                    dp[i] = 1

                # At least one part changes and both are valid
                elif a >= 1 and b >= 1:
                    dp[i] = 2
                    count += 1

                # If any part is invalid
                else:
                    dp[i] = 0

        return count