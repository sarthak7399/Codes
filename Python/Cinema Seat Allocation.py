# https://leetcode.com/problems/cinema-seat-allocation/

# Example 1:
# Input: n = 3, reservedSeats = [[1,2],[1,3],[1,8],[2,6],[3,1],[3,10]]
# Output: 4
# Explanation: The figure above shows an optimal allocation of four groups. Seats marked in blue are already reserved, and each set of four contiguous seats marked in orange is assigned to one group.

import collections

class Solution:
  def maxNumberOfFamilies(self, n, reservedSeats):
    # Create a dictionary of sets to store the reserved seats by row
    seats = collections.defaultdict(set)
    # Iterate through the reserved seats
    for i,j in reservedSeats:
      # If the seat is an outside seat in the row, add it to tallies 0 and 1
      if j in {4,5}: 
        seats[i].add(0) 
        seats[i].add(1)
      # If the seat is a middle seat in the row, add it to tallies 1 and 2
      elif j in {6,7}: 
        seats[i].add(1)
        seats[i].add(2)
      # If the seat is another type of seat, add it to the corresponding tally
      elif j in {8,9}: 
        seats[i].add(2)
      elif j in {2,3}:
        seats[i].add(0)
      # Initialize the result to twice the number of rows
      res = 2*n
    # Iterate through the rows of seats
    for i in seats:
      # If a row has all three tallies, subtract two from the result
      if len(seats[i]) == 3: res -= 2
      # Otherwise, subtract one from the result
      else: res -= 1

    # Return the final result
    return res