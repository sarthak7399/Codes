# https://leetcode.com/problems/count-the-number-of-computer-unlocking-permutations/

# Example 1:
# Input: complexity = [1,2,3]
# Output: 2
# Explanation:
# The valid permutations are:
# [0, 1, 2]
# Unlock computer 0 first with root password.
# Unlock computer 1 with password of computer 0 since complexity[0] < complexity[1].
# Unlock computer 2 with password of computer 1 since complexity[1] < complexity[2].
# [0, 2, 1]
# Unlock computer 0 first with root password.
# Unlock computer 2 with password of computer 0 since complexity[0] < complexity[2].
# Unlock computer 1 with password of computer 0 since complexity[0] < complexity[1].

class Solution:
    def countPermutations(self, complexity):
        mod = 1000000007
        n = len(complexity)

        # If any element (except the first) is ≤ first element, no valid permutation
        for i in range(1, n):
            if complexity[i] <= complexity[0]:
                return 0

        ans = 1
        # Number of valid permutations is (n-1)! modulo mod
        for i in range(1, n):
            ans = (ans * i) % mod

        return ans
