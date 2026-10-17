# https://leetcode.com/problems/minimum-swaps-to-sort-by-digit-sum/

# Example 1:
# Input: nums = [37,100]
# Output: 1
# Explanation:
# Compute the digit sum for each integer: [3 + 7 = 10, 1 + 0 + 0 = 1] → [10, 1]
# Sort the integers based on digit sum: [100, 37]. Swap 37 with 100 to obtain the sorted order.
# Thus, the minimum number of swaps required to rearrange nums is 1.

class Pair:
    def __init__(self, d, val, idx):
        # Store the sum of digits of the number.
        self.dsum = d

        # Store the original number.
        self.val = val

        # Store the original index of the number.
        self.idx = idx


class Solution:
    def digitSum(self, num):
        # Convert the number to a string and sum its digits.
        return sum(int(d) for d in str(num))

    def minSwaps(self, nums):
        # Length of the input array.
        n = len(nums)

        # Create a Pair object for each number, storing its digit sum,
        # value, and original index.
        pairs = [Pair(self.digitSum(nums[i]), nums[i], i) for i in range(n)]

        # Sort by digit sum first, then by number value.
        pairs.sort(key=lambda x: (x.dsum, x.val))

        # Pointer to process each position.
        i = 0

        # Count the number of swaps required.
        cnt = 0

        while i < n:
            # If the current element originally belongs at another index,
            # swap it with the element at its original index.
            if pairs[i].idx != i:
                cnt += 1

                # Find the position where the current element belongs.
                j = pairs[i].idx

                # Swap the elements to move one element closer to its
                # correct position.
                pairs[i], pairs[j] = pairs[j], pairs[i]
            else:
                # The current element is already in its correct position.
                i += 1

        # Return the total number of swaps.
        return cnt