# https://leetcode.com/problems/minimum-jumps-to-reach-end-via-prime-teleportation/

# Example 1:
# Input: nums = [1,2,4,6]
# Output: 2
# Explanation:
# One optimal sequence of jumps is:
# Start at index i = 0. Take an adjacent step to index 1.
# At index i = 1, nums[1] = 2 is a prime number. Therefore, we teleport to index i = 3 as nums[3] = 6 is divisible by 2.
# Thus, the answer is 2.

from collections import deque
from typing import List

class Solution:
    # Maximum limit for prime sieve
    N = 10**6 + 5

    # Precompute prime numbers using Sieve of Eratosthenes
    prime = [True] * N
    prime[0] = prime[1] = False
    
    for i in range(2, 1001):
        if prime[i]:
            for j in range(i * i, N, i):
                prime[j] = False

    def minJumps(self, nums: List[int]) -> int:
        n = len(nums)

        # Find maximum value in nums
        limit = nums[0]
        for c in nums:
            limit = max(limit, c)

        # Build linked-list style structure for indices of each value
        # head[val] = latest index where val appears
        # nxt[i] = previous index with same value
        head = [-1] * (limit + 1)
        nxt = [-1] * n

        for i in range(n):
            val = nums[i]
            nxt[i] = head[val]
            head[val] = i

        # dp[i] = minimum jumps needed to reach index i
        dp = [-1] * n
        dp[0] = 0

        # BFS queue starting from index 0
        queue = deque([0])

        # Track prime values already processed
        seen = set()

        while queue:
            dq = queue.popleft()

            # Reached destination
            if dq == n - 1:
                return dp[dq]

            # Move to right neighbor
            right = dq + 1
            if right < n and dp[right] == -1:
                dp[right] = dp[dq] + 1
                queue.append(right)

            # Move to left neighbor
            left = dq - 1
            if left >= 0 and dp[left] == -1:
                dp[left] = dp[dq] + 1
                queue.append(left)

            val = nums[dq]

            # If current value is prime, jump to all indices
            # whose values are multiples of this prime
            if Solution.prime[val] and val not in seen:
                seen.add(val)

                # Traverse all multiples of val
                for i in range(val, limit + 1, val):
                    j = head[i]

                    # Visit all indices containing this multiple
                    while j != -1:
                        if dp[j] == -1:
                            dp[j] = dp[dq] + 1
                            queue.append(j)
                        j = nxt[j]

                    # Mark processed to avoid repeated traversal
                    head[i] = -1

        # If destination is unreachable
        return -1