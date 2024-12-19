# https://leetcode.com/problems/maximum-average-pass-ratio/

# Example 1:
# Input: classes = [[1,2],[3,5],[2,2]], extraStudents = 2
# Output: 0.78333
# Explanation: You can assign the two extra students to the first class. The average pass ratio will be equal to (3/4 + 3/5 + 2/2) / 3 = 0.78333.

import heapq
from typing import List
class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        # Calculate the benefit of adding a student to each class and build a heap
        # Benefit: current_pass_ratio - new_pass_ratio after adding a student
        # Store tuples: (benefit, num_pass, num_total)
        class_heap = [((num / denom) - ((num + 1) / (denom + 1)), num, denom) for num, denom in classes]
        
        # Transform the list into a min-heap (Python uses min-heap by default)
        heapq.heapify(class_heap)

        # Assign extra students to classes that maximize the average pass ratio
        for _ in range(extraStudents):
            # Pop the class with the maximum benefit of adding a student
            benefit, num_pass, num_total = heapq.heappop(class_heap)

            # Add a student to this class and calculate the new benefit
            new_num_pass, new_num_total = num_pass + 1, num_total + 1
            new_benefit = (new_num_pass / new_num_total) - ((new_num_pass + 1) / (new_num_total + 1))

            # Push the updated class back into the heap
            heapq.heappush(class_heap, (new_benefit, new_num_pass, new_num_total))
        
        # Calculate the final average pass ratio
        total_average = sum(num_pass / num_total for _, num_pass, num_total in class_heap) / len(classes)
        return total_average

