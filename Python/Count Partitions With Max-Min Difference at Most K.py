# https://leetcode.com/problems/count-partitions-with-max-min-difference-at-most-k/

# Example 1:
# Input: nums = [9,4,1,3,7], k = 4
# Output: 6
# Explanation:
# There are 6 valid partitions where the difference between the maximum and minimum elements in each segment is at most k = 4:
# [[9], [4], [1], [3], [7]]
# [[9], [4], [1], [3, 7]]
# [[9], [4], [1, 3], [7]]
# [[9], [4, 1], [3], [7]]
# [[9], [4, 1], [3, 7]]
# [[9], [4, 1, 3], [7]]

class Solution:
    def countPartitions(self, nums: List[int], k: int) -> int:
        n = len(nums)
        MOD = 10**9 + 7
        
        dp = [0] * (n + 1)
        dp[0] = 1  # Empty prefix has one valid way
        
        from collections import deque
        mx, mn = deque(), deque()  # Monotonic deques for max and min
        
        l = 0
        s = 0  # Running sum of valid dp values
        
        for r in range(n):
            # Maintain decreasing deque for max
            while mx and nums[mx[-1]] <= nums[r]:
                mx.pop()
            # Maintain increasing deque for min
            while mn and nums[mn[-1]] >= nums[r]:
                mn.pop()
            mx.append(r)
            mn.append(r)
            
            # Shrink window until max-min ≤ k
            while nums[mx[0]] - nums[mn[0]] > k:
                if mx[0] == l:
                    mx.popleft()
                if mn[0] == l:
                    mn.popleft()
                s = (s - dp[l]) % MOD  # Remove dp[l] from window sum
                l += 1
            
            # Add dp[r] to running sum
            s = (s + dp[r]) % MOD
            dp[r + 1] = s  # dp for prefix ending at r
        
        return dp[n]
