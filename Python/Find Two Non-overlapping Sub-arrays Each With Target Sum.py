# https://leetcode.com/problems/find-two-non-overlapping-sub-arrays-each-with-target-sum/

# Example 1:
# Input: arr = [3,2,2,4,3], target = 3
# Output: 2
# Explanation: Only two sub-arrays have sum = 3 ([3] and [3]). The sum of their lengths is 2.

class Solution:
    def minSumOfLengths(self, arr, target):
        # Length of the array.
        n = len(arr)

        # INF represents that no valid subarray has been found.
        INF = n + 1

        # min_len[i] stores the minimum length of a valid subarray
        # with sum = target that ends at or before index i.
        min_len = [INF] * n

        # 'left' is the left boundary of the sliding window.
        left = 0

        # Current sum of the sliding window.
        total = 0

        # Minimum length of any valid subarray found so far.
        best = INF

        # Minimum combined length of two non-overlapping valid subarrays.
        ans = INF

        # Expand the sliding window using the right pointer.
        for right in range(n):
            # Add the current element to the window.
            total += arr[right]

            # Shrink the window while its sum is greater than target.
            while total > target:
                total -= arr[left]
                left += 1

            # If the current window has the required sum,
            # we have found a valid subarray.
            if total == target:
                # Calculate the length of the current subarray.
                length = right - left + 1

                # If there is a valid subarray completely before
                # the current one, combine their lengths.
                if left > 0 and min_len[left - 1] != INF:
                    ans = min(ans, length + min_len[left - 1])

                # Keep the shortest valid subarray found so far.
                best = min(best, length)

            # Store the best valid subarray length found up to 'right'.
            min_len[right] = best

        # Return -1 if two non-overlapping subarrays were not found.
        return -1 if ans == INF else ans