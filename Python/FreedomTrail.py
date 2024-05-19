# https://leetcode.com/problems/freedom-trail/

# Example 1:
# Input: ring = "godding", key = "gd"
# Output: 4
# Explanation:
# For the first key character 'g', since it is already in place, we just need 1 step to spell this character. 
# For the second key character 'd', we need to rotate the ring "godding" anticlockwise by two steps to make it become "ddinggo".
# Also, we need 1 more step for spelling.
# So the final output is 4.

from collections import defaultdict
class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        # Initialize memoization dictionary
        memo = {}
        
        # Create a dictionary to store positions of each character in the ring
        positions = defaultdict(list)
        for i, c in enumerate(ring):
            positions[c].append(i)
        
        # Call the helper function to find the minimum number of steps
        return self.helper(0, 0, positions, key, ring, memo)
    
    def helper(self, in_index, pos, positions, key, ring, memo):
        # Base case: if all characters in the key have been processed
        if in_index == len(key):
            return 0
        
        # Check if the current state has been memoized
        if (in_index, pos) in memo:
            return memo[(in_index, pos)]
        
        # Initialize minimum steps to infinity
        min_steps = float('inf')
        
        # Iterate over positions of the current character in the ring
        for i in positions[key[in_index]]:
            # Calculate the steps needed to move to the current position
            if i >= pos:
                steps = min(i - pos, pos + len(ring) - i)
            else:
                steps = min(pos - i, i + len(ring) - pos)
            
            # Recursively call the helper function for the next character in the key
            min_steps = min(min_steps, steps + self.helper(in_index + 1, i, positions, key, ring, memo))
        
        # Memoize the result and return the minimum steps
        memo[(in_index, pos)] = min_steps + 1
        return min_steps + 1
