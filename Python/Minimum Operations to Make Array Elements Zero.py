# https://leetcode.com/problems/minimum-operations-to-make-array-elements-zero/

# Example 1:
# Input: queries = [[1,2],[2,4]]
# Output: 3
# Explanation:
# For queries[0]:
# The initial array is nums = [1, 2].
# In the first operation, select nums[0] and nums[1]. The array becomes [0, 0].
# The minimum number of operations required is 1.
# For queries[1]:
# The initial array is nums = [2, 3, 4].
# In the first operation, select nums[0] and nums[2]. The array becomes [0, 3, 1].
# In the second operation, select nums[1] and nums[2]. The array becomes [0, 0, 0].
# The minimum number of operations required is 2.
# The output is 1 + 2 = 3.

class Solution:
    def __init__(self):
        # Max bit length considered (since integers can go up to 2^31 range here)
        self.K = 31  

        # cnt[k] = number of integers having exactly k bits
        # steps[k] = steps required for numbers of bit length k
        # prefWeighted[k] = prefix sum of cnt[i] * steps[i] up to i=k
        self.cnt = [0] * (self.K + 1)
        self.steps = [0] * (self.K + 1)
        self.prefWeighted = [0] * (self.K + 1)

        for k in range(1, self.K + 1):
            self.cnt[k] = 1 << (k - 1)       # 2^(k-1) numbers in range [2^(k-1), 2^k - 1]
            self.steps[k] = (k + 1) // 2     # formula for steps needed
            self.prefWeighted[k] = self.prefWeighted[k - 1] + self.cnt[k] * self.steps[k]

    def count_in_block(self, L, R, blockL, blockR):
        """
        Count how many numbers from interval [L, R]
        fall inside the current bit-length block [blockL, blockR].
        """
        a = max(L, blockL)
        b = min(R, blockR)
        return (b - a + 1) if a <= b else 0

    def bit_length(self, x):
        """Return the bit length of integer x (same as Python's x.bit_length())."""
        return x.bit_length()

    def minOperations(self, queries: list[list[int]]) -> int:
        ans = 0  # Final result across all queries

        for l, r in queries:
            # Get bit-length of L and R
            kl = self.bit_length(l)
            kr = self.bit_length(r)

            S = 0  # Weighted sum of steps for range [l, r]

            # Contribution from the first block (bit-length = kl)
            lowL = 1 << (kl - 1)
            lowR = (1 << kl) - 1
            S += self.count_in_block(l, r, lowL, lowR) * ((kl + 1) // 2)

            # Contribution from the last block (bit-length = kr), if different
            if kr != kl:
                upL = 1 << (kr - 1)
                upR = (1 << kr) - 1
                S += self.count_in_block(l, r, upL, upR) * ((kr + 1) // 2)

                # Full intermediate blocks [kl+1, kr-1] can be added directly using prefix sums
                if kl + 1 <= kr - 1:
                    S += self.prefWeighted[kr - 1] - self.prefWeighted[kl]

            # Max steps for any single number in [l, r] = (kr+1)//2
            dMax = (kr + 1) // 2

            # Minimum ops must satisfy both constraints:
            #   ≥ dMax  (hardest single element)
            #   ≥ ceil(S/2)  (sum constraint)
            ops = max(dMax, (S + 1) // 2)

            ans += ops  # Add result for this query

        return ans
