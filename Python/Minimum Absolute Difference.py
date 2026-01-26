# https://leetcode.com/problems/minimum-absolute-difference/

# Example 1:
# Input: arr = [4,2,1,3]
# Output: [[1,2],[2,3],[3,4]]
# Explanation: The minimum absolute difference is 1. List all pairs with difference equal to 1 in ascending order.

class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        # Sort the array so closest numbers come next to each other
        arr.sort()

        # Store the smallest difference found so far
        min_diff = float('inf')

        # This will store all pairs having the minimum difference
        result = []

        # Check difference between every adjacent pair
        for i in range(len(arr) - 1):
            curr_diff = arr[i + 1] - arr[i]

            # Found a smaller difference → reset result list
            if curr_diff < min_diff:
                min_diff = curr_diff
                result = [[arr[i], arr[i + 1]]]

            # Found another pair with same minimum difference → add it
            elif curr_diff == min_diff:
                result.append([arr[i], arr[i + 1]])

        return result
