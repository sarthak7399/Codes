# https://leetcode.com/problems/delete-columns-to-make-sorted-ii/

# Example 1:
# Input: strs = ["ca","bb","ac"]
# Output: 1
# Explanation: 
# After deleting the first column, strs = ["a", "b", "c"].
# Now strs is in lexicographic order (ie. strs[0] <= strs[1] <= strs[2]).
# We require at least 1 deletion since initially strs was not in lexicographic order, so the answer is 1.

class Solution:
    def minDeletionSize(self, strs):
        n, m = len(strs), len(strs[0])
        # Tracks which adjacent row pairs are already confirmed sorted
        sorted_pairs = [False] * (n - 1)
        delCount = 0

        # Iterate column by column
        for col in range(m):
            bad = False
            # Check if this column breaks ordering for any unsorted pair
            for i in range(n - 1):
                if not sorted_pairs[i] and strs[i][col] > strs[i + 1][col]:
                    bad = True
                    break

            # If column is bad, delete it
            if bad:
                delCount += 1
                continue

            # Update sorted pairs where this column confirms order
            for i in range(n - 1):
                if not sorted_pairs[i] and strs[i][col] < strs[i + 1][col]:
                    sorted_pairs[i] = True

            # If all pairs are sorted, no need to check further columns
            if all(sorted_pairs):
                break

        return delCount
