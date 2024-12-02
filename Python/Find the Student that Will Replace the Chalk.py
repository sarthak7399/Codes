# https://leetcode.com/problems/find-the-student-that-will-replace-the-chalk/

# Example 1:
# Input: chalk = [5,1,5], k = 22
# Output: 0
# Explanation: The students go in turns as follows:
# - Student number 0 uses 5 chalk, so k = 17.
# - Student number 1 uses 1 chalk, so k = 16.
# - Student number 2 uses 5 chalk, so k = 11.
# - Student number 0 uses 5 chalk, so k = 6.
# - Student number 1 uses 1 chalk, so k = 5.
# - Student number 2 uses 5 chalk, so k = 0.
# Student number 0 does not have enough chalk, so they will have to replace it.

from typing import List
class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        k=k%sum(chalk)
        l=len(chalk)
        for i in range(l):
            if(k<chalk[i]):
                return i
            k-=chalk[i]