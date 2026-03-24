# https://leetcode.com/problems/construct-product-matrix/

# Example 1:
# Input: grid = [[1,2],[3,4]]
# Output: [[24,12],[8,6]]
# Explanation: p[0][0] = grid[0][1] * grid[1][0] * grid[1][1] = 2 * 3 * 4 = 24
# p[0][1] = grid[0][0] * grid[1][0] * grid[1][1] = 1 * 3 * 4 = 12
# p[1][0] = grid[0][0] * grid[0][1] * grid[1][1] = 1 * 2 * 4 = 8
# p[1][1] = grid[0][0] * grid[0][1] * grid[1][0] = 1 * 2 * 3 = 6
# So the answer is [[24,12],[8,6]].

class Solution:
    def constructProductMatrix(self, grid):
        
        # Given modulo
        MOD = 12345
        
        # Dimensions of grid
        n, m = len(grid), len(grid[0])

        # -------- Step 1: Flatten the grid --------
        # Convert 2D grid into 1D array for easier processing
        arr = []
        for row in grid:
            for x in row:
                arr.append(x % MOD)   # take modulo early to avoid overflow

        N = len(arr)

        # -------- Step 2: Prefix and Suffix arrays --------
        # prefix[i] → product of all elements before index i
        # suffix[i] → product of all elements after index i
        prefix = [1] * N
        suffix = [1] * N

        # Build prefix array
        for i in range(1, N):
            # prefix[i] = arr[0] * arr[1] * ... * arr[i-1]
            prefix[i] = (prefix[i - 1] * arr[i - 1]) % MOD

        # Build suffix array
        for i in range(N - 2, -1, -1):
            # suffix[i] = arr[i+1] * arr[i+2] * ... * arr[N-1]
            suffix[i] = (suffix[i + 1] * arr[i + 1]) % MOD

        # -------- Step 3: Construct result matrix --------
        res = [[0] * m for _ in range(n)]
        idx = 0  # pointer to traverse flattened array

        for i in range(n):
            for j in range(m):
                
                # Product of all elements except current index
                # = prefix[idx] * suffix[idx]
                res[i][j] = (prefix[idx] * suffix[idx]) % MOD
                
                idx += 1

        return res