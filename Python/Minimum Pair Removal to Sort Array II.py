# https://leetcode.com/problems/minimum-pair-removal-to-sort-array-ii/

# Example 1:
# Input: nums = [5,2,3,1]
# Output: 2
# Explanation:
# The pair (3,1) has the minimum sum of 4. After replacement, nums = [5,2,4].
# The pair (2,4) has the minimum sum of 6. After replacement, nums = [5,6].
# The array nums became non-decreasing in two operations.

class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        n = len(nums)

        # Add sentinel to avoid boundary checks
        nums.append(inf)

        # Doubly linked list representation using arrays
        left = [-1] * (n + 1)
        right = [i + 1 for i in range(n + 1)]

        for i in range(1, n + 1):
            left[i] = i - 1

        # Min-heap storing (sum of adjacent pair, left index of the pair)
        heap = [(a + b, i) for i, (a, b) in enumerate(pairwise(nums))]
        heapify(heap)

        # Count how many positions violate non-decreasing order
        rest = sum(1 for a, b in pairwise(nums) if a > b)

        ans = 0  # Number of merge operations

        # Continue until array becomes non-decreasing
        while rest > 0:
            v, i = heappop(heap)   # v = sum, i = left index of pair
            r = right[i]           # r = right neighbour index

            # Skip if this heap entry is outdated / invalid
            if r == -1 or nums[i] + nums[r] != v or left[r] != i:
                continue

            rr = right[r]  # right neighbour of r

            # Remove old order violations involving i, r, rr
            if left[i] != -1 and nums[left[i]] > nums[i]:
                rest -= 1
            if nums[i] > nums[r]:
                rest -= 1
            if rr != -1 and nums[r] > nums[rr]:
                rest -= 1

            # Merge nums[i] and nums[r] into nums[i]
            nums[i] = v
            right[i] = rr
            if rr != -1:
                left[rr] = i

            # Add new violations created after merge
            if left[i] != -1 and nums[left[i]] > nums[i]:
                rest += 1
            if rr != -1 and nums[i] > nums[rr]:
                rest += 1

            # Push newly formed adjacent pairs into heap
            if left[i] != -1:
                heappush(heap, (nums[left[i]] + nums[i], left[i]))
            if rr != -1:
                heappush(heap, (nums[i] + nums[rr], i))

            ans += 1  # One merge operation done

        return ans
