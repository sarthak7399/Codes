# https://leetcode.com/problems/check-if-all-1s-are-at-least-length-k-places-away/

# Example 1:
# Input: nums = [1,0,0,0,1,0,0,1], k = 2
# Output: true
# Explanation: Each of the 1s are at least 2 places away from each other.

class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        p = 0
        app = -1   # index of previous 1

        while p < n:
            if nums[p] == 1 and app == -1:
                app = p   # first 1 found

            elif nums[p] == 1:
                d = p - app - 1   # distance between consecutive 1's
                app = p
                if d < k:         # check required gap
                    return False

            p += 1

        return True
