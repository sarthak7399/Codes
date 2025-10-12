# https://leetcode.com/problems/find-sum-of-array-product-of-magical-sequences/

# Example 1:
# Input: m = 5, k = 5, nums = [1,10,100,10000,1000000]
# Output: 991600007
# Explanation:
# All permutations of [0, 1, 2, 3, 4] are magical sequences, each with an array product of 10^^13.

class Solution(object):
    def magicalSum(self, m, k, nums):
        """
        :type m: int          # Total number of elements to choose (with repetition)
        :type k: int          # Target binary property (number of 1s)
        :type nums: List[int] # Given list of numbers
        :rtype: int           # Result modulo 10^9 + 7
        """
        M = 10**9 + 7
        l = len(nums)
        d = {}  # Memoization dictionary

        # Recursive helper function
        def f(r, n, i, c):
            """
            r : remaining count to pick
            n : remaining bit-count requirement
            i : current index in nums
            c : carry value (represents binary sum carry bits)
            """
            # ❌ Base invalid cases
            if r < 0 or n < 0 or r + bin(c).count('1') < n:
                return 0

            # ✅ Base case: all elements chosen
            if r == 0:
                return 1 if n == bin(c).count('1') else 0

            # ❌ No more numbers left
            if i >= l:
                return 0

            key = (r, n, i, c)
            if key in d:
                return d[key]  # Return cached result

            res = 0
            # 🔁 Try choosing t times the current number nums[i]
            for t in range(r + 1):
                # Compute binomial coefficient C(r, t)
                w = 1
                for j in range(t):
                    w = w * (r - j) // (j + 1)
                w %= M

                # v = nums[i]^t mod M
                v = pow(nums[i], t, M)

                # Update carry and remaining
                nc = c + t
                res = (res + w * v % M * f(r - t, n - (nc % 2), i + 1, nc // 2)) % M

            d[key] = res
            return res

        return f(m, k, 0, 0)
