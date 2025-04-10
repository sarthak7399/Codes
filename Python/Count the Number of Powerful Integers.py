# https://leetcode.com/problems/count-the-number-of-powerful-integers/


# Example 1:
# Input: start = 1, finish = 6000, limit = 4, s = "124"
# Output: 5
# Explanation: The powerful integers in the range [1..6000] are 124, 1124, 2124, 3124, and, 4124. All these integers have each digit <= 4, and "124" as a suffix. Note that 5124 is not a powerful integer because the first digit is 5 which is greater than 4.
# It can be shown that there are only 5 powerful integers in this range.

class Solution:
    def numberOfPowerfulInt(self, start: int, finish: int, limit: int, suffix: str) -> int:
        # Function to count how many powerful integers are ≤ num
        def count_powerful_up_to(num: int) -> int:
            num_str = str(num)
            suffix_len = len(suffix)
            prefix_len = len(num_str) - suffix_len

            # If number is shorter than suffix, it's not a valid powerful integer
            if prefix_len < 0:
                return 0

            # dp[i][0] = number of valid numbers from position i with prefix less than num_str
            # dp[i][1] = number of valid numbers from position i with prefix equal to num_str
            dp = [[0] * 2 for _ in range(prefix_len + 1)]

            # Base case: at the suffix boundary
            dp[prefix_len][0] = 1  # Any number formed before the suffix is valid if it was less
            suffix_from_num = num_str[prefix_len:]
            # If the suffix part of the number is >= the given suffix, it's valid for equal path
            dp[prefix_len][1] = int(suffix_from_num) >= int(suffix)

            # Build DP table backwards from right to left of prefix
            for i in range(prefix_len - 1, -1, -1):
                digit = int(num_str[i])
                
                # Case 0: if previous digits were already less, we can use (limit + 1) options (0 to limit)
                dp[i][0] = (limit + 1) * dp[i + 1][0]

                if digit <= limit:
                    # Case 1: current digit is within limit, so:
                    # - digits less than current go to case 0
                    # - equal digit continues the equal path
                    dp[i][1] = digit * dp[i + 1][0] + dp[i + 1][1]
                else:
                    # If digit > limit, all numbers from here fall into case 0
                    dp[i][1] = (limit + 1) * dp[i + 1][0]

            return dp[0][1]  # Total number of valid powerful integers ≤ num

        # Answer is how many powerful integers are in [start, finish]
        return count_powerful_up_to(finish) - count_powerful_up_to(start - 1)
