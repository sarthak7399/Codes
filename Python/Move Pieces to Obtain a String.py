# https://leetcode.com/problems/move-pieces-to-obtain-a-string/

# Example 1:
# Input: start = "_L__R__R_", target = "L______RR"
# Output: true
# Explanation: We can obtain the string target from start by doing the following moves:
# - Move the first piece one step to the left, start becomes equal to "L___R__R_".
# - Move the last piece one step to the right, start becomes equal to "L___R___R".
# - Move the second piece three steps to the right, start becomes equal to "L______RR".
# Since it is possible to get the string target from start, we return true.

class Solution:
    def canChange(self, start: str, target: str) -> bool:
        # If start and target are already the same, return True
        if start == target:
            return True

        # Counters to track mismatched positions for 'L' and 'R'
        waitL = 0  # Tracks extra 'L' in `target` not yet matched
        waitR = 0  # Tracks extra 'R' in `start` not yet matched

        # Iterate over corresponding characters in `start` and `target`
        for curr, goal in zip(start, target):
            # If the current character in `start` is 'R'
            if curr == 'R':
                # There cannot be unmatched 'L' ahead of 'R' as 'R' can only move right
                if waitL > 0:
                    return False
                # Increment unmatched 'R' count
                waitR += 1

            # If the target character is 'L'
            if goal == 'L':
                # There cannot be unmatched 'R' ahead of 'L' as 'L' can only move left
                if waitR > 0:
                    return False
                # Increment unmatched 'L' count
                waitL += 1

            # If the target character is 'R'
            if goal == 'R':
                # Ensure there's an unmatched 'R' in `start` to match
                if waitR == 0:
                    return False
                # Match an unmatched 'R'
                waitR -= 1

            # If the current character in `start` is 'L'
            if curr == 'L':
                # Ensure there's an unmatched 'L' in `target` to match
                if waitL == 0:
                    return False
                # Match an unmatched 'L'
                waitL -= 1

        # Ensure all 'L' and 'R' mismatches have been resolved
        return waitL == 0 and waitR == 0
