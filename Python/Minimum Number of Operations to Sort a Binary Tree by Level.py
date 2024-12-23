# https://leetcode.com/problems/minimum-number-of-operations-to-sort-a-binary-tree-by-level/

# Example 2:
# Input: root = [1,3,2,7,6,5,4]
# Output: 3
# Explanation:
# - Swap 3 and 2. The 2nd level becomes [2,3].
# - Swap 7 and 4. The 3rd level becomes [4,6,5,7].
# - Swap 6 and 5. The 3rd level becomes [4,5,6,7].
# We used 3 operations so return 3.
# It can be proven that 3 is the minimum number of operations needed.

from collections import deque
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        
        q = deque()
        q.append(root)
        ans = 0
        d = {}

        # Perform level order traversal of the Tree
        while q:
            level = []
            for i in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                level.append(node.val)
            final = sorted(level)
            d.clear()

            # make a map that stores the right position of each value
            for i in range(len(level)):
                d[final[i]] = i

            # Swap until the position i has the correct value
            for i in range(len(level)):
                if i == d[level[i]]: continue

                while i != d[level[i]]:
                    temp = level[d[level[i]]]
                    level[d[level[i]]] = level[i]
                    level[i] = temp
                    ans+=1
        return ans