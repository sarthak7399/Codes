# https://leetcode.com/problems/delete-duplicate-folders-in-system/

# Example 1:
# Input: paths = [["a"],["c"],["d"],["a","b"],["c","b"],["d","a"]]
# Output: [["d"],["d","a"]]
# Explanation: The file structure is as shown.
# Folders "/a" and "/c" (and their subfolders) are marked for deletion because they both contain an empty
# folder named "b".

from collections import defaultdict

class Node:
    def __init__(self, name):
        self.name = name                  # Name of the folder
        self.children = {}                # Child folders (name -> Node)
        self.signature = ""               # Unique signature representing subtree structure

class Solution:
    def deleteDuplicateFolder(self, paths):
        root = Node("")  # Root node representing the filesystem root

        # Step 1: Build the folder tree from the list of paths
        for path in paths:
            node = root
            for folder in path:
                if folder not in node.children:
                    node.children[folder] = Node(folder)
                node = node.children[folder]

        signature_count = defaultdict(int)  # Count how many times each subtree signature appears

        # Step 2: DFS traversal to compute a unique signature for each subtree
        def dfs(node):
            if not node.children:
                node.signature = ""  # Leaf node: empty signature
                return ""
            child_signatures = []
            # Process children in sorted order to keep signature consistent
            for name, child in sorted(node.children.items()):
                child_signature = dfs(child)  # Recursively compute signature
                child_signatures.append(f"{name}({child_signature})")
            node.signature = "".join(child_signatures)
            signature_count[node.signature] += 1  # Track how many times this signature appears
            return node.signature

        dfs(root)  # Populate signatures and counts

        result = []           # To store paths that are not part of duplicate subtrees
        current_path = []     # Helper to track current traversal path

        # Step 3: DFS traversal to build the final result, skipping duplicate subtrees
        def dfs2(node):
            # If this subtree is duplicated, skip it entirely
            if node.children and signature_count[node.signature] >= 2:
                return
            current_path.append(node.name)  # Add current folder to path
            result.append(current_path.copy())  # Record current valid path
            for name, child in sorted(node.children.items()):
                dfs2(child)
            current_path.pop()  # Backtrack

        # Start traversal from each child of root (since root itself is virtual)
        for name, child in sorted(root.children.items()):
            dfs2(child)

        return result
