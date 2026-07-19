# https://leetcode.com/problems/max-dot-product-of-two-subsequences/

# Example 1:
# Input: nums1 = [2,1,-2,5], nums2 = [3,0,-6]
# Output: 18
# Explanation: Take subsequence [2,-2] from nums1 and subsequence [3,-6] from nums2.
# Their dot product is (2*3 + (-2)*(-6)) = 18.

class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        # n = length of nums1, m = length of nums2
        n, m = len(nums1), len(nums2)
        
        # Always keep nums2 as the smaller array to save memory
        if m > n:
            return self.maxDotProduct(nums2, nums1)
            
        # dp[j] = maximum dot product using nums1[0..i-1] and nums2[0..j-1]
        # Initialize with -infinity because we must take at least one pair
        dp = [float('-inf')] * (m + 1)
        
        # Loop over nums1
        for i in range(1, n + 1):
            # This stores dp[j-1] from the previous row (diagonal value)
            prev_diag = float('-inf')
            
            # Loop over nums2
            for j in range(1, m + 1):
                # Current product if we pair nums1[i-1] and nums2[j-1]
                curr_product = nums1[i-1] * nums2[j-1]
                
                # Save old dp[j] before overwriting (this becomes next prev_diag)
                temp = dp[j]
                
                # Update dp[j] with the best of:
                # 1. Start new subsequence with current pair
                # 2. Extend previous subsequence (prev_diag + curr_product)
                # 3. Skip current element from nums1 (keep dp[j])
                # 4. Skip current element from nums2 (keep dp[j-1])
                dp[j] = max(
                    curr_product,                # take only this pair
                    curr_product + prev_diag,    # extend previous subsequence
                    dp[j],                       # skip nums1[i-1]
                    dp[j-1]                      # skip nums2[j-1]
                )
                
                # Move diagonal value for next j
                prev_diag = temp

        # Final answer is dp[m]
        return dp[m]
