# https://leetcode.com/problems/count-the-number-of-ideal-arrays/

# Example 1:
# Input: n = 2, maxValue = 5
# Output: 10
# Explanation: The following are the possible ideal arrays:
# - Arrays starting with the value 1 (5 arrays): [1,1], [1,2], [1,3], [1,4], [1,5]
# - Arrays starting with the value 2 (2 arrays): [2,2], [2,4]
# - Arrays starting with the value 3 (1 array): [3,3]
# - Arrays starting with the value 4 (1 array): [4,4]
# - Arrays starting with the value 5 (1 array): [5,5]
# There are a total of 5 + 2 + 1 + 1 + 1 = 10 distinct ideal arrays.

from collections import Counter
from math import comb

class Solution:
    def idealArrays(self, length: int, max_value: int) -> int:
        MOD = 1_000_000_007  # To handle large numbers and return result modulo 10^9 + 7
        total_ways = max_value  # Initially, all arrays of length 1 (with values 1 to max_value) are ideal

        # Frequency map to track how many ways each number can appear at the end of an ideal array
        frequency_map = {num: 1 for num in range(1, max_value + 1)}
        
        # Iterate for increasing lengths of arrays from 2 to 'length'
        for array_size in range(1, length): 
            new_frequency = Counter()  # Temporary map for the next array size

            # Loop through all current values in the frequency map
            for base_value in frequency_map: 
                # Try multiplying base_value with all valid multipliers (that keep value <= max_value)
                for multiplier in range(2, max_value // base_value + 1): 
                    # Compute number of positions to place the current value (using combinations)
                    combinations = comb(length - 1, array_size)

                    # Add the total number of such valid combinations to total_ways
                    total_ways += combinations * frequency_map[base_value]

                    # Update frequency map for next level with new value (base_value * multiplier)
                    new_frequency[multiplier * base_value] += frequency_map[base_value]
            
            # Move to the next array size with updated frequencies
            frequency_map = new_frequency

            # Take modulo to keep the result within limits
            total_ways %= MOD
        
        return total_ways
