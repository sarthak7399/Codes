# https://leetcode.com/problems/crawler-log-folder/

# Example 1:
# Input: logs = ["d1/","d2/","../","d21/","./"]
# Output: 2
# Explanation: Use this change folder operation "../" 2 times and go back to the main folder.

class Solution:
    def minOperations(self, logs: list[str]) -> int:
        res: int = 0

        for log in logs:
            if log == "../":
                res -= 1 if res > 0 else 0
            elif log != "./":
                res += 1

        return res