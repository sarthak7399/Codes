# https://leetcode.com/problems/find-all-possible-stable-binary-arrays-i/

# Example 1:
# Input: zero = 1, one = 1, limit = 2
# Output: 2
# Explanation:
# The two possible stable binary arrays are [1,0] and [0,1], as both arrays have a single 0 and a single 1, and no subarray has a length greater than 2.

class Solution:
    def numberOfStableArrays(self, zero: int, one: int, limit: int) -> int:
        # Modulo constant (required because answer can be very large)
        MOD = 1000000007
        
        # Maximum total length of array
        maxN = zero + one
        
        # Precompute factorials and inverse factorials for combinations
        fact = [0] * (maxN + 1)
        invFact = [0] * (maxN + 1)
        
        fact[0] = 1
        invFact[0] = 1
        
        # Compute factorial values: n!
        for i in range(1, maxN + 1):
            fact[i] = (fact[i - 1] * i) % MOD
        
        # Compute inverse factorial using Fermat's little theorem
        invFact[maxN] = pow(fact[maxN], MOD - 2, MOD)
        
        # Fill remaining inverse factorial values
        for i in range(maxN - 1, 0, -1):
            invFact[i] = (invFact[i + 1] * (i + 1)) % MOD
        
        # Function to compute nCk (binomial coefficient)
        def C(n, k):
            if k < 0 or k > n:
                return 0
            return fact[n] * invFact[k] % MOD * invFact[n - k] % MOD

        # Count number of ways to distribute N elements into K groups
        # such that no group size exceeds limit L
        # Uses inclusion–exclusion principle
        def F(N, K, L):
            if K <= 0 or K > N:
                return 0
            
            ans = 0
            
            # Maximum number of groups that violate the limit
            maxJ = (N - K) // L
            
            for j in range(maxJ + 1):
                # Number of ways to choose j groups that exceed the limit
                # and distribute remaining elements
                term = C(K, j) * C(N - j * L - 1, K - 1) % MOD
                
                # Inclusion-exclusion: alternate signs
                if j & 1:
                    ans = (ans - term + MOD) % MOD
                else:
                    ans = (ans + term) % MOD
            
            return ans

        # Maximum number of zero segments possible
        maxK = min(zero, one + 1)

        # Precompute valid arrangements for ones
        fOne = [0] * (maxK + 2)
        for k in range(1, maxK + 2):
            fOne[k] = F(one, k, limit)
        
        ans = 0
        
        # Iterate over possible number of zero segments
        for k in range(1, maxK + 1):
            # Ways to arrange zeros in k segments
            fz = F(zero, k, limit)
            
            if fz == 0:
                continue
            
            # Ones can appear in three ways relative to zero segments:
            # (k-1), k, or (k+1) segments
            fo = (fOne[k - 1] + 2 * fOne[k] + fOne[k + 1]) % MOD
            
            # Multiply zero arrangements with one arrangements
            ans = (ans + fz * fo) % MOD
        
        return ans