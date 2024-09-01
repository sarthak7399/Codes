# https://www.geeksforgeeks.org/problems/construct-list-using-given-q-xor-queries/

# Example 1:
# Input:q = 5
# queries[] = {{0, 6}, {0, 3}, {0, 2}, {1, 4}, {1, 5}}
# Output:1 2 3 7
# Explanation:
# [0] (initial value)
# [0 6] (add 6 to list)
# [0 6 3] (add 3 to list)
# [0 6 3 2] (add 2 to list)
# [4 2 7 6] (XOR each element by 4)
# [1 7 2 3] (XOR each element by 5)
# The sorted list after performing all the queries is [1 2 3 7]. 

from typing import List
class Solution:
    def constructList(self, q : int, queries : List[List[int]]) -> List[int]:
        # Initialize the list with a single element 0
        s = [0]
        cumulative_xor = 0
        
        for query in queries:
            if query[0] == 0:
                # Insert x into the list (apply the cumulative XOR to new elements directly)
                s.append(query[1] ^ cumulative_xor)
            elif query[0] == 1:
                # Update the cumulative XOR value
                cumulative_xor ^= query[1]
        
        # Apply the cumulative XOR to all elements in the list
        s = [x ^ cumulative_xor for x in s]
        
        # Sort the list and return it
        s.sort()
        return s