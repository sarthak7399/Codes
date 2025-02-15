# https://leetcode.com/problems/find-the-punishment-number-of-an-integer/

# Example 1:
# Input: n = 10
# Output: 182
# Explanation: There are exactly 3 integers i in the range [1, 10] that satisfy the conditions in the statement:
# - 1 since 1 * 1 = 1
# - 9 since 9 * 9 = 81 and 81 can be partitioned into 8 and 1 with a sum equal to 8 + 1 == 9.
# - 10 since 10 * 10 = 100 and 100 can be partitioned into 10 and 0 with a sum equal to 10 + 0 == 10.
# Hence, the punishment number of 10 is 1 + 81 + 100 = 182

class Solution:
    def punishmentNumber(self, n: int) -> int:
        # Helper function to check if a number can be partitioned into parts that sum to the target
        def canPartition(num: str, index: int, target: int) -> bool:
            # Base case: if we've used up all digits, check if the remaining target is 0
            if index == len(num):
                return target == 0

            sum_val = 0
            # Try all possible partitions of the number
            for i in range(index, len(num)):
                sum_val = sum_val * 10 + int(num[i])  # Build the current part
                if sum_val > target:  # Stop if the current part exceeds the target
                    break
                # Recursively check if we can partition the remaining digits
                if canPartition(num, i + 1, target - sum_val):
                    return True
            return False

        # Sum squares of numbers that can be partitioned to match the number
        return sum(i * i for i in range(1, n + 1) if canPartition(str(i * i), 0, i))
