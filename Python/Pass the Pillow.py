# https://leetcode.com/problems/pass-the-pillow/

# Example 1:
# Input: n = 4, time = 5
# Output: 2
# Explanation: People pass the pillow in the following way: 1 -> 2 -> 3 -> 4 -> 3 -> 2.
# After five seconds, the 2nd person is holding the pillow.\

class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        cycle_length = (n - 1) * 2

        position_in_cycle = time % cycle_length
        
        if position_in_cycle < n:
            return position_in_cycle + 1
        else:
            return 2 * n - position_in_cycle - 1
        