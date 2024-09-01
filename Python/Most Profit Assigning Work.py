# https://leetcode.com/problems/most-profit-assigning-work/

# Example 1:
# Input: difficulty = [2,4,6,8,10], profit = [10,20,30,40,50], worker = [4,5,6,7]
# Output: 100
# Explanation: Workers are assigned jobs of difficulty [4,4,6,6] and they get a profit of [20,20,30,30] separately.

from typing import List
class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        max_profit = 0  # Initialize the total maximum profit to 0
        worker.sort()  # Sort the worker abilities in ascending order
        vals = sorted(zip(difficulty, profit))  # Combine and sort difficulty and profit by difficulty
        
        i = 0  # Pointer for iterating through the sorted difficulty-profit pairs
        cur_profit = 0  # Variable to track the maximum profit achievable at the current point
        
        # Iterate through each worker's ability
        for ability in worker:
            # Update cur_profit with the highest profit for tasks the worker can perform
            while i < len(difficulty) and ability >= vals[i][0]:
                cur_profit = max(cur_profit, vals[i][1])  # Update cur_profit to the highest profit seen so far
                i += 1  # Move to the next task
            
            max_profit += cur_profit  # Add the best possible profit for the current worker to max_profit
        
        return max_profit  # Return the total maximum profit
