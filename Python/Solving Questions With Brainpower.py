# https://leetcode.com/problems/solving-questions-with-brainpower/

# Example 1:
# Input: questions = [[3,2],[4,3],[4,4],[2,5]]
# Output: 5
# Explanation: The maximum points can be earned by solving questions 0 and 3.
# - Solve question 0: Earn 3 points, will be unable to solve the next 2 questions
# - Unable to solve questions 1 and 2
# - Solve question 3: Earn 2 points
# Total points earned: 3 + 2 = 5. There is no other way to earn 5 or more points.

from typing import List
class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions)
        dp = [0] * (n + 1)  # DP array to store the maximum points possible from each index

        # Iterate backwards to compute optimal choices
        for i in range(n - 1, -1, -1):
            points = questions[i][0]  # Points earned from the current question
            brainpower = questions[i][1]  # Brainpower needed (skipped questions)
            next_q = i + brainpower + 1  # Index of the next question that can be attempted

            # Choice 1: Take the current question and add points from the next valid question
            take = points + (dp[next_q] if next_q < n else 0)
            
            # Choice 2: Skip the current question and take the next available one
            skip = dp[i + 1]

            # Store the maximum of both choices
            dp[i] = max(take, skip)

        return dp[0]  # Maximum points achievable from the first question onward
