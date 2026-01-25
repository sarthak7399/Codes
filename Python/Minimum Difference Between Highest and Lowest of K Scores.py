# Example 2:

# Input: nums = [9,4,1,7], k = 2
# Output: 2
# Explanation: There are six ways to pick score(s) of two students:
# - [9,4,1,7]. The difference between the highest and lowest score is 9 - 4 = 5.
# - [9,4,1,7]. The difference between the highest and lowest score is 9 - 1 = 8.
# - [9,4,1,7]. The difference between the highest and lowest score is 9 - 7 = 2.
# - [9,4,1,7]. The difference between the highest and lowest score is 4 - 1 = 3.
# - [9,4,1,7]. The difference between the highest and lowest score is 7 - 4 = 3.
# - [9,4,1,7]. The difference between the highest and lowest score is 7 - 1 = 6.
# The minimum possible difference is 2.

class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        # Sort the array so close values come near each other
        nums.sort()

        # ans will store the minimum difference found
        ans = float('inf')

        # j is the index offset for a window of size k
        j = k - 1

        # Slide a window of size k over the sorted array
        for i in range(len(nums) - j):
            # Difference between max and min in current window
            ans = min(ans, nums[i + j] - nums[i])

        # Return the minimum difference found
        return ans
