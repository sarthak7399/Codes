# https://leetcode.com/problems/find-elements-in-a-contaminated-binary-tree/

# Example 1:
# Input
# ["FindElements","find","find"]
# [[[-1,null,-1]],[1],[2]]
# Output
# [null,false,true]
# Explanation
# FindElements findElements = new FindElements([-1,null,-1]); 
# findElements.find(1); // return False 
# findElements.find(2); // return True 

class FindElements:
    def __init__(self, root):
        self.recoveredValues = set()  # Store recovered values
        root.val = 0  # Root value is always 0
        self.recoverTree(root)  # Restore tree structure

    def recoverTree(self, root):
        if not root:
            return
        self.recoveredValues.add(root.val)  # Add current node to set
        if root.left:
            root.left.val = 2 * root.val + 1  # Compute left child value
            self.recoverTree(root.left)
        if root.right:
            root.right.val = 2 * root.val + 2  # Compute right child value
            self.recoverTree(root.right)

    def find(self, target):
        return target in self.recoveredValues  # Check if target exists
