# https://leetcode.com/problems/find-the-pivot-integer/?envType=daily-question&envId=2024-03-13

# Example 1:
# Input: n = 8
# Output: 6
# Explanation: 6 is the pivot integer since: 1 + 2 + 3 + 4 + 5 + 6 = 6 + 7 + 8 = 21.

class Solution:
    def pivotInteger(self, n: int) -> int:
        curr_sum, total_natural_sum = 0, int(n*(n+1)/2)  # Initialize current sum and total sum of natural numbers
        for i in range(n,0,-1):  # Iterate from n to 1 in reverse order
            curr_sum+=i  # Add the current number to the current sum
            if(total_natural_sum==curr_sum):  # Check if the current sum is equal to the total sum
                return i  # If yes, return the current number as the pivot integer
            total_natural_sum-=i  # Update the total sum by subtracting the current number
        return -1  # If no pivot integer is found, return -1
