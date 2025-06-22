# https://leetcode.com/problems/divide-a-string-into-groups-of-size-k/

# Example 1:
# Input: s = "abcdefghi", k = 3, fill = "x"
# Output: ["abc","def","ghi"]
# Explanation:
# The first 3 characters "abc" form the first group.
# The next 3 characters "def" form the second group.
# The last 3 characters "ghi" form the third group.
# Since all groups can be completely filled by characters from the string, we do not need to use fill.
# Thus, the groups formed are "abc", "def", and "ghi".

class Solution:
    def divideString(self, s: str, k: int, fill: str) -> list[str]:
        # Step 1: Initialize result list
        result = []  
        i = 0

        # Step 2: Loop through the string
        while i < len(s):
            # Step 3: Extract k characters
            chunk = s[i:i+k]

            # Step 4: Pad with fill if needed
            if len(chunk) < k:
                chunk += fill * (k - len(chunk))

            # Step 5: Add to result
            result.append(chunk)
            i += k

        # Step 6: Return final list
        return result