# https://leetcode.com/problems/minimum-number-of-increments-on-subarrays-to-form-a-target-array/

# Example 1:
# Input: target = [1,2,3,2,1]
# Output: 3
# Explanation: We need at least 3 operations to form the target array from the initial array.
# [0,0,0,0,0] increment 1 from index 0 to 4 (inclusive).
# [1,1,1,1,1] increment 1 from index 1 to 3 (inclusive).
# [1,2,2,2,1] increment 1 at index 2.
# [1,2,3,2,1] target array is formed.

class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        """
        Given an integer array `target`, this function finds the minimum number of 
        operations needed to form `target` from an array of zeros.
        
        Operation rule:
        - In one operation, you can increment every element of any subarray by 1.

        The idea:
        - The number of operations equals the total increase between consecutive elements.
        - Each time `target[i]` is greater than the previous element, 
          we need (target[i] - target[i-1]) more operations.
        """

        res = 0      # Total number of operations
        prev = 0     # Previous element (initially 0 since we start from zeros)

        # Traverse each element in the target array
        for x in target:
            # If current value > previous, additional (x - prev) operations are needed
            if x > prev:
                res += x - prev
            # Update previous value for next iteration
            prev = x

        # Return total operations required
        return res
