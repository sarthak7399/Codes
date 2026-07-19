# https://leetcode.com/problems/number-of-zigzag-arrays-ii/

# Example 1:
# Input: n = 3, l = 4, r = 5
# Output: 2
# Explanation:
# There are only 2 valid ZigZag arrays of length n = 3 using values in the range [4, 5]:
# [4, 5, 4]
# [5, 4, 5]

class Solution:
    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        MOD = 10**9 + 7

        # Number of distinct values available in the range [l, r]
        m = r - l + 1

        # Base vector:
        # up[i] = number of valid zig-zag arrays of length 2
        # ending at rank i
        up = list(range(m))

        # Transition matrix
        # T[i][k] = 1 if a transition from state k to state i is valid
        T = [[0] * m for _ in range(m)]

        for i in range(1, m):
            for k in range(m - i, m):
                T[i][k] = 1

        # Matrix multiplication
        def matmul(A, B):
            sz = len(A)

            C = [[0] * sz for _ in range(sz)]

            for i in range(sz):
                for k in range(sz):

                    # Skip useless computations
                    if not A[i][k]:
                        continue

                    for j in range(sz):
                        C[i][j] = (
                            C[i][j] + A[i][k] * B[k][j]
                        ) % MOD

            return C

        # Fast matrix exponentiation
        def matpow(M, p):
            sz = len(M)

            # Identity matrix
            res = [[int(i == j) for j in range(sz)]
                   for i in range(sz)]

            while p:

                # Multiply result when current bit is set
                if p & 1:
                    res = matmul(res, M)

                # Square the matrix
                M = matmul(M, M)

                p >>= 1

            return res

        # Raise transition matrix to power (n - 2)
        # because the base vector already represents length 2
        Tn = matpow(T, n - 2)

        # Multiply T^(n-2) with base vector
        # to obtain counts for length n
        ans = 0

        for i in range(m):
            for j in range(m):
                ans = (
                    ans + Tn[i][j] * up[j]
                ) % MOD

        # Multiply by 2 to account for both zig-zag patterns:
        # 1. Up-Down-Up-Down...
        # 2. Down-Up-Down-Up...
        return ans * 2 % MOD