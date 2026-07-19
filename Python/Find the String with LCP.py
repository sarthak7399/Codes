# https://leetcode.com/problems/find-the-string-with-lcp/

# Example 1:
# Input: lcp = [[4,0,2,0],[0,3,0,1],[2,0,2,0],[0,1,0,1]]
# Output: "abab"
# Explanation: lcp corresponds to any 4 letter string with two alternating letters. The lexicographically smallest of them is "abab".

class Solution:

    # -------- Disjoint Set Union (Union-Find) --------
    class DSU:
        def __init__(self, n):
            # Parent array (initially each node is its own parent)
            self.parent = list(range(n))
            
            # Rank array for union by rank optimization
            self.rank = [0] * n

        def findPar(self, x):
            # Find representative (root) with path compression
            if self.parent[x] != x:
                self.parent[x] = self.findPar(self.parent[x])
            return self.parent[x]

        def unite(self, x, y):
            # Union two sets
            px = self.findPar(x)
            py = self.findPar(y)

            # Already in same set
            if px == py:
                return

            # Union by rank
            if self.rank[px] < self.rank[py]:
                self.parent[px] = py
            elif self.rank[px] > self.rank[py]:
                self.parent[py] = px
            else:
                self.parent[px] = py
                self.rank[py] += 1

    # -------- Compute LCP matrix from constructed word --------
    def compute(self, word, dp):
        n = len(word)

        # Fill dp from bottom-right to top-left
        for i in range(n - 1, -1, -1):
            for j in range(n - 1, -1, -1):

                # If characters match
                if word[i] == word[j]:
                    if i + 1 < n and j + 1 < n:
                        # Extend LCP from next positions
                        dp[i][j] = 1 + dp[i + 1][j + 1]
                    else:
                        # Last character match
                        dp[i][j] = 1
                else:
                    # No match
                    dp[i][j] = 0

    # -------- Main function --------
    def findTheString(self, lcp):
        n = len(lcp)

        # Initialize DSU
        dsu = self.DSU(n)

        # -------- Step 1: Validate diagonal --------
        # lcp[i][i] should be length of suffix starting at i → n-i
        for i in range(n):
            if lcp[i][i] != n - i:
                return ""

        # -------- Step 2: Group indices using DSU --------
        # If lcp[i][j] > 0 → characters at i and j must be same
        for i in range(n):
            for j in range(i + 1, n):
                if lcp[i][j] > 0:
                    dsu.unite(i, j)

        # -------- Step 3: Assign characters to groups --------
        grp = [''] * n   # group → assigned character
        word = ['?'] * n # final string (as list)

        # Start assigning characters from 'a'
        c = ord('a')

        for i in range(n):
            p = dsu.findPar(i)

            # If this group has no character yet
            if grp[p] == '':
                if c > ord('z'):  # only 26 lowercase letters allowed
                    return ""
                grp[p] = chr(c)
                c += 1

            # Assign character to position i
            word[i] = grp[p]

        # -------- Step 4: Validate zero LCP constraints --------
        # If lcp[i][j] == 0 → characters must differ
        for i in range(n):
            for j in range(n):
                if lcp[i][j] == 0 and word[i] == word[j]:
                    return ""

        # -------- Step 5: Recompute LCP from constructed word --------
        dp = [[0] * n for _ in range(n)]
        self.compute(word, dp)

        # If computed LCP matches given LCP → valid string
        if dp == lcp:
            return "".join(word)

        # Otherwise invalid
        return ""