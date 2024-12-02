# https://leetcode.com/problems/xor-queries-of-a-subarray/

# Example 1:
# Input: arr = [1,3,4,8], queries = [[0,1],[1,2],[0,3],[3,3]]
# Output: [2,7,14,8] 
# Explanation: 
# The binary representation of the elements in the array are:
# 1 = 0001 
# 3 = 0011 
# 4 = 0100 
# 8 = 1000 
# The XOR values for queries are:
# [0,1] = 1 xor 3 = 2 
# [1,2] = 3 xor 4 = 7 
# [0,3] = 1 xor 3 xor 4 xor 8 = 14 
# [3,3] = 8

from typing import List
class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        # Step 1: Precompute prefix XOR
        n = len(arr)
        prefix_xor = [0] * (n + 1)  # prefix_xor[i] will store XOR from arr[0] to arr[i-1]
        
        # Fill the prefix XOR array
        for i in range(1, n + 1):
            prefix_xor[i] = prefix_xor[i - 1] ^ arr[i - 1]
        
        # Step 2: Process each query using the prefix XOR array
        res = []
        for l, r in queries:
            # XOR of subarray from index lelf to right is:
            # prefix_xor[r + 1] ^ prefix_xor[l]
            res.append(prefix_xor[r + 1] ^ prefix_xor[l])
        
        return res
