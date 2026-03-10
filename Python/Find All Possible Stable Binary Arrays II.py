# https://leetcode.com/problems/find-all-possible-stable-binary-arrays-ii/

# Example 1:
# Input: zero = 1, one = 1, limit = 2
# Output: 2
# Explanation:
# The two possible stable binary arrays are [1,0] and [0,1].

# Modulo constant to keep numbers within limits
MOD = 1_000_000_007

# Maximum size for factorial precomputation
MAXN = 1000

# Arrays to store factorials and inverse factorials
fact = [0] * (MAXN + 1)
invfact = [0] * (MAXN + 1)


def init():
    # Precompute factorials: fact[i] = i!
    fact[0] = 1
    for i in range(1, MAXN + 1):
        fact[i] = (fact[i - 1] * i) % MOD

    # Compute inverse factorial of MAXN using Fermat's Little Theorem
    invfact[MAXN] = pow(fact[MAXN], MOD - 2, MOD)

    # Fill remaining inverse factorials
    # invfact[i] = modular inverse of fact[i]
    for i in range(MAXN, 0, -1):
        invfact[i - 1] = (invfact[i] * i) % MOD


# Initialize factorial tables once
init()


class Solution:
    def numberOfStableArrays(self, zero: int, one: int, limit: int) -> int:

        # Ensure zero <= one (symmetry optimization)
        if zero > one:
            zero, one = one, zero

        # Special case when limit = 1
        # Means no two same elements can be adjacent
        # So array must strictly alternate
        if limit == 1:
            if zero == one: 
                return 2        # start with 0 or start with 1
            if zero + 1 == one: 
                return 1        # must start with 1
            return 0            # impossible otherwise

        # Function to compute nCr using precomputed factorials
        def ncr(n: int, r: int) -> int:
            return fact[n] * invfact[r] * invfact[n - r]

        # Count number of ways to divide n elements into k groups
        # such that each group size ≤ limit
        # Uses inclusion–exclusion principle
        def ways(n: int, k: int):

            # If every group has exactly 1 element
            if n == k: 
                return 1

            j, total, flag = 0, 0, True

            # Inclusion–exclusion loop
            while j <= k <= n:
                # Choose j groups that violate limit
                # and distribute remaining elements
                term = ncr(k, j) * ncr(n - 1, k - 1)

                # Alternate adding/subtracting terms
                total = total + term if flag else total - term

                # Reduce n by limit for next violation case
                n -= limit
                j += 1
                flag = not flag

            return total

        result = 0

        # Minimum zero segments required
        start = (zero + limit - 1) // limit

        # Precompute ways for ones
        prv, cur, nxt = 0, ways(one, start), ways(one, start + 1)

        # Iterate over possible number of zero segments
        for k in range(start, zero + 1):

            # Combine zero segment arrangements with one segment arrangements
            result += (prv + 2 * cur + nxt) * ways(zero, k)

            # Slide window for ones segment counts
            prv, cur, nxt = cur, nxt, ways(one, k + 2)

        # Return answer modulo MOD
        return result % MOD