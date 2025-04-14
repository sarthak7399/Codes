# https://leetcode.com/problems/recover-a-tree-from-preorder-traversal/

# Example 1:
# Input: traversal = "1-2--3--4-5--6--7"
# Output: [1,2,5,3,4,6,7]

import re
from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def recoverFromPreorder(self, S: str) -> TreeNode:
        dash_map = {}
        dash_cnt = 0
        first_num = ""
        for ch in S:
            if ch == '-': break
            first_num += ch
        dash_map[0] = TreeNode(int(first_num))
        s = re.findall(r'(-+)(\d+)', S)
        for dash, num in s:
            dash_num = len(dash)
            num = int(num)
            n = TreeNode(num)
            fa = dash_map[dash_num - 1]
            if not fa.left:
                fa.left = n
            elif not fa.right:
                fa.right = n
            dash_map[dash_num] = n
        return dash_map[0]