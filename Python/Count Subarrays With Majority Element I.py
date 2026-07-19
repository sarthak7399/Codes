# https://leetcode.com/problems/count-subarrays-with-majority-element-i/

# Example 1:
# Input: nums = [1,2,2,3], target = 2
# Output: 5
# Explanation:
# Valid subarrays with target = 2 as the majority element:
# nums[1..1] = [2]
# nums[2..2] = [2]
# nums[1..2] = [2,2]
# nums[0..2] = [1,2,2]
# nums[1..3] = [2,2,3]
# So there are 5 such subarrays.

from typing import List

class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        n, ans = len(nums), 0

        # Try every possible starting index of a subarray
        for i in range(n):

            # Count of target occurrences in the current subarray
            cnt = 0

            # Extend the subarray from i to j
            for j in range(i, n):

                # Increase count if current element equals target
                if nums[j] == target:
                    cnt += 1

                # A target is the majority element if it appears
                # more than half the length of the subarray
                #
                # Subarray length = j - i + 1
                # Majority condition:
                # cnt > (j - i + 1) / 2
                #
                # To avoid floating-point division:
                # 2 * cnt > j - i + 1
                if 2 * cnt > j - i + 1:
                    ans += 1

        # Return the total number of subarrays
        # where target is the majority element
        return ans