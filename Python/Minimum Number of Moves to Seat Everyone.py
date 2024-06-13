# https://leetcode.com/problems/minimum-number-of-moves-to-seat-everyone/

# Example 1:
# Input: seats = [3,1,5], students = [2,7,4]
# Output: 4
# Explanation: The students are moved as follows:
# - The first student is moved from from position 2 to position 1 using 1 move.
# - The second student is moved from from position 7 to position 5 using 2 moves.
# - The third student is moved from from position 4 to position 3 using 1 move.
# In total, 1 + 2 + 1 = 4 moves were used.

from typing import List
class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        seats.sort()
        students.sort()
        moves = 0

        for i in range(len(seats)) :
            moves += abs(seats[i] - students[i])

        return moves