# https://leetcode.com/problems/minimize-hamming-distance-after-swap-operations/

# Example 1:
# Input: source = [1,2,3,4], target = [2,1,4,5], allowedSwaps = [[0,1],[2,3]]
# Output: 1
# Explanation: source can be transformed the following way:
# - Swap indices 0 and 1: source = [2,1,3,4]
# - Swap indices 2 and 3: source = [2,1,4,3]
# The Hamming distance of source and target is 1 as they differ in 1 position: index 3.

import collections

class UnionFind:
  def __init__(self, n: int):
    # Initialize parent array (each node is its own parent initially)
    self.id = list(range(n))
    
    # Rank array to keep tree shallow (used in union by rank)
    self.rank = [0] * n

  def unionByRank(self, u: int, v: int) -> None:
    # Find roots of both nodes
    i = self.find(u)
    j = self.find(v)

    # If already in same set, do nothing
    if i == j:
      return

    # Attach smaller rank tree under larger rank tree
    if self.rank[i] < self.rank[j]:
      self.id[i] = j
    elif self.rank[i] > self.rank[j]:
      self.id[j] = i
    else:
      # If ranks are equal, choose one as root and increase its rank
      self.id[i] = j
      self.rank[j] += 1

  def find(self, u: int) -> int:
    # Path compression: make all nodes point directly to root
    if self.id[u] != u:
      self.id[u] = self.find(self.id[u])
    return self.id[u]


class Solution:
  def minimumHammingDistance(
      self,
      source: list[int],
      target: list[int],
      allowedSwaps: list[list[int]],
  ) -> int:
    n = len(source)
    ans = 0

    # Initialize Union-Find structure
    uf = UnionFind(n)

    # Each group will maintain a frequency map of values from 'source'
    groupIdToCount = [collections.Counter() for _ in range(n)]

    # Build connected components using allowed swaps
    for a, b in allowedSwaps:
      uf.unionByRank(a, b)

    # Count frequencies of source values in each connected component
    for i in range(n):
      root = uf.find(i)
      groupIdToCount[root][source[i]] += 1

    # Compare with target array
    for i in range(n):
      groupId = uf.find(i)
      count = groupIdToCount[groupId]

      # If target value not available in this group → mismatch
      if target[i] not in count:
        ans += 1
      else:
        # Use one occurrence of this value
        count[target[i]] -= 1

        # Remove key if count becomes zero (cleanup)
        if count[target[i]] == 0:
          del count[target[i]]

    return ans  # Minimum Hamming distance