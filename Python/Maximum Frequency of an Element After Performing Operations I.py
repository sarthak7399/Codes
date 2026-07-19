# https://leetcode.com/problems/maximum-frequency-of-an-element-after-performing-operations-i/

# Example 1:
# Input: nums = [1,4,5], k = 1, numOperations = 2
# Output: 2
# Explanation:
# We can achieve a maximum frequency of two by:
# Adding 0 to nums[1]. nums becomes [1, 4, 5].
# Adding -1 to nums[2]. nums becomes [1, 4, 4].

class Solution:
    def maxFrequency(self, nums: List[int], k: int, numOperations: int) -> int:
        M = max(nums) + 2                # Maximum possible value range (+2 for boundaries)
        freq, sweep = [0] * M, [0] * M   # freq: count of each number; sweep: range coverage
        mm = M                            # smallest start index across all sweeps
        
        for x in nums:
            freq[x] += 1                  # count occurrences of each number
            s, t = max(1, x - k), min(M - 1, x + k + 1)  # range where x can influence
            sweep[s] += 1                 # mark start of influence
            sweep[t] -= 1                 # mark end of influence
            mm = min(mm, s)               # update lowest sweep start
        
        ans, cnt = 0, 0                   # ans: max frequency, cnt: cumulative sweep value
        for x in range(mm, M):
            cnt += sweep[x]               # add active influence ranges
            # combine existing freq with extra achievable using operations
            ans = max(ans, freq[x] + min(numOperations, cnt - freq[x]))
        return ans                        # return max possible frequency
