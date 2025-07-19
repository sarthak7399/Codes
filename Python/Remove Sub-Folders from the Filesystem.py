# https://leetcode.com/problems/remove-sub-folders-from-the-filesystem/

# Example 1:
# Input: folder = ["/a","/a/b","/c/d","/c/d/e","/c/f"]
# Output: ["/a","/c/d","/c/f"]
# Explanation: Folders "/a/b" is a subfolder of "/a" and "/c/d/e" is inside of folder "/c/d" in our filesystem.

from typing import List
class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        # Sort the folders lexicographically so parent folders come before their subfolders
        folder.sort()
        
        # Initialize result list with the first folder
        ans = [folder[0]]
        
        # Iterate through remaining folders starting from index 1
        for i in range(1, len(folder)):
            # Get the last added folder path and add a trailing slash
            last_folder = ans[-1] + '/'
            
            # Check if current folder starts with last_folder
            # If it doesn't start with last_folder, then it's not a subfolder
            if not folder[i].startswith(last_folder):
                ans.append(folder[i])
        
        # Return the result
        return ans