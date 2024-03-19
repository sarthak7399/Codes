# https://leetcode.com/problems/task-scheduler/description/?envType=daily-question&envId=2024-03-19

# Example 1:
# Input: tasks = ["A","A","A","B","B","B"], n = 2
# Output: 8
# Explanation: A possible sequence is: A -> B -> idle -> A -> B -> idle -> A -> B.
# After completing task A, you must wait two cycles before doing A again. The same applies to task B. In the 3rd interval, neither A nor B can be done, so you idle. By the 4th cycle, you can do A again as 2 intervals have passed.

from typing import List
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = [0] * 26         # Initialize a frequency array to count the occurrences of each task
        for task in tasks:              # Count the occurrences of each task
            freq[ord(task) - ord('A')] += 1                
        freq.sort()     # Sort the frequency array to have the task with the highest frequency at the end               
        chunk = freq[25] - 1     # Calculate the number of chunks required (chunks between the most frequent tasks)      
        idle = chunk * n        # Calculate the number of idle slots based on chunks and cooldown period       
        for i in range(24, -1, -1):      # Iterate over the remaining tasks to update the idle slots
            idle -= min(chunk, freq[i])      # Subtract the minimum between the current chunk and the frequency of the task
        return len(tasks) + idle if idle >= 0 else len(tasks)       # Return the total number of slots needed for all tasks, including idle slots if necessary
