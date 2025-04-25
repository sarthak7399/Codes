# https://leetcode.com/problems/count-of-interesting-subarrays/

# Example 1:
# Input: nums = [3,2,4], modulo = 2, k = 1
# Output: 3
# Explanation: In this example the interesting subarrays are: 
# The subarray nums[0..0] which is [3]. 
# - There is only one index, i = 0, in the range [0, 0] that satisfies nums[i] % modulo == k. 
# - Hence, cnt = 1 and cnt % modulo == k.  
# The subarray nums[0..1] which is [3,2].
# - There is only one index, i = 0, in the range [0, 1] that satisfies nums[i] % modulo == k.  
# - Hence, cnt = 1 and cnt % modulo == k.
# The subarray nums[0..2] which is [3,2,4]. 
# - There is only one index, i = 0, in the range [0, 2] that satisfies nums[i] % modulo == k. 
# - Hence, cnt = 1 and cnt % modulo == k. 
# It can be shown that there are no other interesting subarrays. So, the answer is 3.

from collections import defaultdict

class Solution(object):
    def countInterestingSubarrays(self, nums, modulo, k):
        count = 0                # Final count of interesting subarrays
        equals = 0              # Running count of elements satisfying (num % modulo == k)
        mpp = defaultdict(int)  # Map to store prefix frequency counts based on (equals % modulo)
        mpp[0] = 1              # Initialize with 0 to handle subarrays starting at index 0

        for i in nums:
            # If current element satisfies the condition, increment the count
            if i % modulo == k:
                equals += 1

            # Current prefix modulo
            rem = equals % modulo

            # We want previous prefix such that: (previous_rem + k) % modulo == current_rem
            # Solving for previous_rem gives us: (rem - k + modulo) % modulo
            needed = (rem - k + modulo) % modulo

            # Add the number of such prefixes seen so far
            count += mpp[needed]

            # Store the current prefix modulo
            mpp[rem] += 1

        return count
