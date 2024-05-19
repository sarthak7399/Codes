# https://leetcode.com/problems/boats-to-save-people/

# Example 1:
# Input: people = [1,2], limit = 3
# Output: 1
# Explanation: 1 boat (1, 2)

from typing import List
class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        # Sort the list of people by their weights
        people.sort()
        
        # Initialize variables for the left and right pointers
        left, right = 0, len(people) - 1
        
        # Initialize variable to count the number of boats
        num_boats = 0
        
        # Iterate through the list of people using two pointers
        while left <= right:
            # Increment the boat count
            num_boats += 1
            
            # Check if the weight of the person at the left pointer plus the weight of the person at the right pointer is less than or equal to the limit
            if people[left] + people[right] <= limit:
                # If it is, move the left pointer to the right to include the lighter person in the boat
                left += 1
            
            # Move the right pointer to the left to include the heavier person in the boat
            right -= 1
        
        # Return the total number of boats required
        return num_boats
