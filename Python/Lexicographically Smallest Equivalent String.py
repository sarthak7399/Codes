# https://leetcode.com/problems/lexicographically-smallest-equivalent-string/

# Example 1:
# Input: s1 = "parker", s2 = "morris", baseStr = "parser"
# Output: "makkek"
# Explanation: Based on the equivalency information in s1 and s2, we can group their characters as [m,p], [a,o], [k,r,s], [e,i].
# The characters in each group are equivalent and sorted in lexicographical order.
# So the answer is "makkek".

# Union-Find (Disjoint Set Union) structure to manage equivalence of characters
class UnionFind:
    def __init__(self, N):
        # Initialize root array where each node is its own parent initially
        self.root = list(range(N))

    def Find(self, x):
        # Path compression: make each node in the path point directly to the root
        if self.root[x] != x:
            self.root[x] = self.Find(self.root[x])
        return self.root[x]

    def Union(self, x, y):
        # Find the root of both x and y
        x = self.Find(x)
        y = self.Find(y)

        if x == y:
            return  # Already in the same set

        # Always attach the larger index to the smaller index to ensure lexicographically smallest representative
        if y > x:
            self.root[y] = x
        else:
            self.root[x] = y

class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        G = UnionFind(26)  # There are 26 lowercase English letters (indexed 0 to 25)

        n, m = len(s1), len(baseStr)

        # Union corresponding characters from s1 and s2
        for i in range(n):
            G.Union(ord(s1[i]) - 97, ord(s2[i]) - 97)  # Convert char to index (a=0, ..., z=25)

        ans = ""
        # For each character in baseStr, find its lexicographically smallest equivalent character
        for x in baseStr:
            smallest_index = G.Find(ord(x) - 97)  # Get root representative index
            ans += chr(smallest_index + 97)       # Convert index back to character

        return ans
