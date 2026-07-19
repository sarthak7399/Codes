# https://leetcode.com/problems/delete-columns-to-make-sorted-iii/

# Example 1:
# Input: strs = ["babca","bbazb"]
# Output: 3
# Explanation: After deleting columns 0, 1, and 4, the final array is strs = ["bc", "az"].
# Both these rows are individually in lexicographic order (ie. strs[0][0] <= strs[0][1] and strs[1][0] <= strs[1][1]).
# Note that strs[0] > strs[1] - the array strs is not necessarily in lexicographic order.

class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        m = len(strs[0])
        # dp[i] stores the max length of an increasing subsequence ending at index i
        dp = [1] * m
        
        for i in range(m):
            for j in range(i):
                # Check if column j can precede column i for ALL rows
                # We use a generator expression with all() for clean syntax
                if all(row[j] <= row[i] for row in strs):
                    dp[i] = max(dp[i], dp[j] + 1)
        
        # Result is total columns - max columns we can keep
        return m - max(dp)