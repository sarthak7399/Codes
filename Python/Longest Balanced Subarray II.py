# https://leetcode.com/problems/longest-balanced-subarray-ii/

# Example 1:
# Input: nums = [2,5,4,3]
# Output: 4
# Explanation:
# The longest balanced subarray is [2, 5, 4, 3].
# It has 2 distinct even numbers [2, 4] and 2 distinct odd numbers [5, 3]. Thus, the answer is 4.

from collections import deque
from typing import List

class segmentTreeNode:
    def __init__(self, maxV=0, minV=0, lazyTag=0):
        # mx → maximum value in this segment
        # mn → minimum value in this segment
        # tag → lazy propagation value (pending update)
        self.mx = maxV
        self.mn = minV
        self.tag = lazyTag

class segmentTree:
    def addTag(self, val: int, id: int) -> None:
        # Apply lazy update to current node
        self.tree[id].tag += val
        self.tree[id].mx += val
        self.tree[id].mn += val

    def push(self, id: int) -> None:
        # Push lazy value to children
        val = self.tree[id].tag
        self.addTag(val, 2 * id + 1)
        self.addTag(val, 2 * id + 2)
        self.tree[id].tag = 0  # clear after pushing

    def pull(self, id: int) -> None:
        # Recalculate current node from children
        self.tree[id].mx = max(self.tree[2 * id + 1].mx,
                               self.tree[2 * id + 2].mx)
        self.tree[id].mn = min(self.tree[2 * id + 1].mn,
                               self.tree[2 * id + 2].mn)

    def build(self, nums: List[int], left: int, right: int, id: int) -> None:
        # Build tree from prefix array
        if left == right:
            self.tree[id].mx = nums[left]
            self.tree[id].mn = nums[left]
            return

        mid = (left + right) >> 1
        self.build(nums, left, mid, 2 * id + 1)
        self.build(nums, mid + 1, right, 2 * id + 2)
        self.pull(id)

    def query(self, l: int, r: int, val: int,
              left: int, right: int, id: int) -> int:
        """
        Find index in range [l, r] where prefix value == val.
        If no such value exists → return -1.
        """

        # If entire segment cannot contain val → prune
        if self.tree[id].mx < val or self.tree[id].mn > val:
            return -1

        # If leaf node
        if left == right:
            return left

        mid = (left + right) >> 1
        self.push(id)  # ensure children values are updated

        # Search right first (to maximise length)
        if r > mid:
            res = self.query(l, r, val, mid + 1, right, 2 * id + 2)
            if res > -1:
                return res

        # Then search left
        if l <= mid:
            return self.query(l, r, val, left, mid, 2 * id + 1)

        return -1

    def update(self, l: int, r: int, val: int,
               left: int, right: int, id: int) -> None:
        """
        Add val to all elements in range [l, r]
        """

        # If fully inside update range
        if l <= left and right <= r:
            self.addTag(val, id)
            return

        mid = (left + right) >> 1
        self.push(id)

        # Update children
        if l <= mid:
            self.update(l, r, val, left, mid, 2 * id + 1)
        if r > mid:
            self.update(l, r, val, mid + 1, right, 2 * id + 2)

        self.pull(id)

    def __init__(self, nums: List[int]):
        # Initialise tree
        self.sz = len(nums)
        self.tree = [segmentTreeNode() for _ in range(4 * self.sz)]
        self.build(nums, 0, self.sz - 1, 0)

    def search(self, l: int, r: int, val: int) -> int:
        # Public search function
        return self.query(l, r, val, 0, self.sz - 1, 0)

    def modify(self, l: int, r: int, val: int) -> None:
        # Public range update function
        self.update(l, r, val, 0, self.sz - 1, 0)


class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
        n = len(nums)

        # Step 1: Build parity-based prefix sum
        # Even → -1
        # Odd  → +1
        prefix = [0] * n
        exist = dict()  # tracks all positions of each number

        for i in range(n):
            prefix[i] += prefix[i - 1]

            # First occurrence affects prefix
            if nums[i] not in exist:
                exist[nums[i]] = deque()
                prefix[i] += (1 if nums[i] & 1 else -1)

            exist[nums[i]].append(i)

        # Append n to mark end boundary
        for deq in exist.values():
            deq.append(n)

        # Build segment tree on prefix array
        seg = segmentTree(prefix)

        maxlen = 0

        # Step 2: Slide left boundary
        for i in range(n):

            if i > 0:
                # Remove influence of nums[i-1]
                exist[nums[i - 1]].popleft()

                # Reverse its prefix effect for remaining occurrences
                seg.modify(
                    i - 1,
                    exist[nums[i - 1]][0] - 1,
                    (-1 if nums[i - 1] & 1 else 1)
                )

            # Early stopping
            if i + maxlen >= n:
                break

            # Find farthest index where prefix becomes 0
            idx = seg.search(i + maxlen, n - 1, 0)

            if idx > -1:
                maxlen = idx - i + 1

        return maxlen
