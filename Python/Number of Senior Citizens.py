# https://leetcode.com/problems/number-of-senior-citizens/

# Example 1:
# Input: details = ["7868190130M7522","5303914400F9211","9273338290F4010"]
# Output: 2
# Explanation: The passengers at indices 0, 1, and 2 have ages 75, 92, and 40. Thus, there are 2 people who are over 60 years old.

from typing import List
class Solution:
    def countSeniors(self, details: List[str]) -> int:
        count = 0
        age = 0
        for detail in details:
            age = detail[11] + detail[12]
            if int(age) > 60:
                count += 1
        return count