# https://leetcode.com/problems/minimum-difference-in-sums-after-removal-of-elements/

# Example 1:
# Input: nums = [3,1,2]
# Output: -1
# Explanation: Here, nums has 3 elements, so n = 1. 
# Thus we have to remove 1 element from nums and divide the array into two equal parts.
# - If we remove nums[0] = 3, the array will be [1,2]. The difference in sums of the two parts will be 1 - 2 = -1.
# - If we remove nums[1] = 1, the array will be [3,2]. The difference in sums of the two parts will be 3 - 2 = 1.
# - If we remove nums[2] = 2, the array will be [3,1]. The difference in sums of the two parts will be 3 - 1 = 2.
# The minimum difference between sums of the two parts is min(-1,1,2) = -1. 

import heapq

class Solution:
    def minimumDifference(self, nums):
        n = len(nums)
        k = n // 3  # We will split nums into three equal parts (left, middle, right)

        leftMins = [0] * n  # leftMins[i]: minimal sum of k smallest elements from first i+1 elements
        rightMaxs = [0] * n  # rightMaxs[i]: maximal sum of k largest elements from i to end

        # ------------------------
        # Step 1: Build leftMins[]
        # ------------------------

        maxLeft = []  # max heap (by pushing negative values) to keep track of k smallest elements
        leftSum = 0

        # Initialize heap with first k elements
        for i in range(k):
            heapq.heappush(maxLeft, -nums[i])
            leftSum += nums[i]
        leftMins[k - 1] = leftSum

        # Process the rest up to n - k
        for i in range(k, n - k):
            # If current element is smaller than the largest element in our k smallest so far
            if nums[i] < -maxLeft[0]:
                leftSum += nums[i] + heapq.heappop(maxLeft)  # remove largest, add current
                heapq.heappush(maxLeft, -nums[i])
            # Store current minimal sum
            leftMins[i] = leftSum

        # -------------------------
        # Step 2: Build rightMaxs[]
        # -------------------------

        minRight = []  # min heap to keep track of k largest elements
        rightSum = 0

        # Initialize heap with last k elements
        for i in range(n - 1, n - k - 1, -1):
            heapq.heappush(minRight, nums[i])
            rightSum += nums[i]
        rightMaxs[n - k] = rightSum

        # Process the rest backwards up to index k-1
        for i in range(n - k - 1, k - 2, -1):
            # If current element is larger than the smallest element in our k largest so far
            if nums[i] > minRight[0]:
                rightSum += nums[i] - heapq.heappop(minRight)  # remove smallest, add current
                heapq.heappush(minRight, nums[i])
            # Store current maximal sum
            rightMaxs[i] = rightSum

        # -------------------------------------
        # Step 3: Find minimal difference
        # -------------------------------------

        minDiff = float('inf')
        # Compare left sum up to index i with right sum starting from index i+1
        for i in range(k - 1, n - k):
            minDiff = min(minDiff, leftMins[i] - rightMaxs[i + 1])

        return minDiff
