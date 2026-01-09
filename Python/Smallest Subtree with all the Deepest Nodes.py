# https://leetcode.com/problems/smallest-subtree-with-all-the-deepest-nodes/

# Example 1:
# Input: root = [3,5,1,6,2,0,8,null,null,7,4]
# Output: [2,7,4]
# Explanation: We return the node with value 2, colored in yellow in the diagram.
# The nodes coloured in blue are the deepest nodes of the tree.
# Notice that nodes 5, 3 and 2 contain the deepest nodes in the tree but node 2 is the smallest subtree among them, so we return it.

class Solution:
    def subtreeWithAllDeepest(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        # dfs returns a tuple:
        # (height of subtree, node which is the answer for this subtree)
        def dfs(node):
            # Base case: if node is None, height is 0 and no subtree exists
            if not node:
                return 0, None

            # Recursively get left subtree height and answer node
            left_height, left_node = dfs(node.left)

            # Recursively get right subtree height and answer node
            right_height, right_node = dfs(node.right)

            # If left subtree is deeper, return its height and its answer node
            if left_height > right_height:
                return left_height + 1, left_node
            
            # If right subtree is deeper, return its height and its answer node
            elif right_height > left_height:
                return right_height + 1, right_node
            
            # If both sides have same depth, current node is the LCA of deepest nodes
            else:
                return left_height + 1, node
            
        # We only need the node part of the result
        return dfs(root)[1]
