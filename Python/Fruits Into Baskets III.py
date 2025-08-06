# https://leetcode.com/problems/fruits-into-baskets-iii/

# Example 1:
# Input: fruits = [4,2,5], baskets = [3,5,4]
# Output: 1
# Explanation:
# fruits[0] = 4 is placed in baskets[1] = 5.
# fruits[1] = 2 is placed in baskets[0] = 3.
# fruits[2] = 5 cannot be placed in baskets[2] = 4.
# Since one fruit type remains unplaced, we return 1.

from typing import List

class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        n = len(baskets)

        # Find the next power of 2 greater than or equal to n (needed for segment tree size)
        N = 1
        while N <= n:
            N <<= 1  # Same as N *= 2

        # Initialize segment tree with 0 values (size: 2 * N)
        segTree = [0] * (2 * N)

        # Place basket capacities in the leaf nodes of the segment tree
        for i in range(n):
            segTree[N + i] = baskets[i]

        # Build the segment tree by taking max from children
        for i in range(N - 1, 0, -1):
            segTree[i] = max(segTree[2 * i], segTree[2 * i + 1])

        count = 0  # Count of unplaced fruits

        # Try placing each fruit in a basket using segment tree
        for fruit in fruits:
            index = 1  # Start from root of the segment tree

            # If the root node (max basket capacity) is less than fruit size, cannot place
            if segTree[index] < fruit:
                count += 1  # Fruit remains unplaced
                continue

            # Traverse down the tree to find leftmost basket that can fit the fruit
            while index < N:
                if segTree[2 * index] >= fruit:
                    index = 2 * index  # Go to left child
                else:
                    index = 2 * index + 1  # Go to right child

            # Mark the selected basket as used (assign -1 so it won't be selected again)
            segTree[index] = -1

            # Update the parent nodes to reflect the change
            while index > 1:
                index //= 2  # Move to parent
                segTree[index] = max(segTree[2 * index], segTree[2 * index + 1])

        return count  # Return total number of fruits that couldn't be placed
