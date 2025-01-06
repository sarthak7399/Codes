# https://leetcode.com/problems/minimum-number-of-operations-to-move-all-balls-to-each-box/

# Example 1:
# Input: boxes = "110"
# Output: [1,1,3]
# Explanation: The answer for each box is as follows:
# 1) First box: you will have to move one ball from the second box to the first box in one operation.
# 2) Second box: you will have to move one ball from the first box to the second box in one operation.
# 3) Third box: you will have to move one ball from the first box to the third box in two operations, and move one ball from the second box to the third box in one operation.

from typing import List
class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n = len(boxes)  # Length of the input string 'boxes'
        
        # pre_move[i] will store the total number of moves required to move all balls to the left of box i
        # post_move[i] will store the total number of moves required to move all balls to the right of box i
        pre_move = [0] * n  
        post_move = [0] * n

        # Left to right pass: calculate moves to bring all balls to the left of each box
        left_ball_count = 0  # Number of balls encountered while traversing from left to right
        left_moves = 0  # Total number of moves made to bring balls to the left of each box
        for i in range(n):
            pre_move[i] = left_moves  # Store the total moves for the current box
            # Update the count of balls encountered so far
            left_ball_count += 1 if boxes[i] == "1" else 0
            # Add the number of balls encountered so far to the left_moves
            left_moves += left_ball_count
        
        # Right to left pass: calculate moves to bring all balls to the right of each box
        right_ball_count = 0  # Number of balls encountered while traversing from right to left
        right_moves = 0  # Total number of moves made to bring balls to the right of each box
        for j in range(n-1, -1, -1):  # Traverse from right to left
            post_move[j] = right_moves  # Store the total moves for the current box
            # Update the count of balls encountered so far
            right_ball_count += 1 if boxes[j] == "1" else 0
            # Add the number of balls encountered so far to the right_moves
            right_moves += right_ball_count
        
        # Calculate the total moves for each box by summing the left and right moves
        result = [(left + right) for left, right in zip(pre_move, post_move)]
        
        return result
