# https://leetcode.com/problems/trionic-array-ii/

# Example 1:
# Input: nums = [0,-2,-1,-3,0,2,-1]
# Output: -4
# Explanation:
# Pick l = 1, p = 2, q = 3, r = 5:
# nums[l...p] = nums[1...2] = [-2, -1] is strictly increasing (-2 < -1).
# nums[p...q] = nums[2...3] = [-1, -3] is strictly decreasing (-1 > -3)
# nums[q...r] = nums[3...5] = [-3, 0, 2] is strictly increasing (-3 < 0 < 2).
# Sum = (-2) + (-1) + (-3) + 0 + 2 = -4.

class Solution:
    def maxSumTrionic(self, nums: List[int]) -> int:
        n = len(nums)
        res = -float('inf')   # maximum trionic sum found
        i = 1                # potential peak index

        # Iterate possible middle (decreasing) segments
        while i < n - 2:
            a = b = i
            net = nums[a]    # sum of the decreasing middle part

            # Extend strictly decreasing segment to the right
            while b + 1 < n and nums[b + 1] < nums[b]:
                net += nums[b + 1]
                b += 1

            # No decreasing part found
            if b == a:
                i += 1
                continue
            
            c = b            # end of decreasing segment
            left = right = 0
            lx = rx = -float('inf')

            # Extend strictly increasing segment to the left
            while a - 1 >= 0 and nums[a - 1] < nums[a]:
                left += nums[a - 1]
                lx = max(lx, left)
                a -= 1

            # No increasing part on the left
            if a == i:
                i += 1
                continue
            
            # Extend strictly increasing segment to the right
            while b + 1 < n and nums[b + 1] > nums[b]:
                right += nums[b + 1]
                rx = max(rx, right)
                b += 1

            # No increasing part on the right
            if b == c:
                i += 1
                continue
                
            # Update maximum trionic sum
            res = max(res, lx + rx + net)

            # Move index forward to avoid overlap
            i = b

        return res if res != -float('inf') else 0
