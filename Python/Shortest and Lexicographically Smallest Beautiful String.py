# https://leetcode.com/problems/shortest-and-lexicographically-smallest-beautiful-string/

# Example 1:
# Input: s = "100011001", k = 3
# Output: "11001"
# Explanation: There are 7 beautiful substrings in this example:
# 1. The substring "100011001".
# 2. The substring "100011001".
# 3. The substring "100011001".
# 4. The substring "100011001".
# 5. The substring "100011001".
# 6. The substring "100011001".
# 7. The substring "100011001".
# The length of the shortest beautiful substring is 5.
# The lexicographically smallest beautiful substring with length 5 is the substring "11001".

class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        # Store the best beautiful substring found so far.
        ans = ""

        # Length of the input string.
        n = len(s)

        # Try every possible starting index.
        for i in range(n):

            # Count the number of '1's in the current substring.
            oneCnt = 0

            # Build the substring starting from index i.
            cur = ""

            # Extend the substring one character at a time.
            for j in range(i, n):

                # Add the current character to the substring.
                cur += s[j]

                # Increase the count if the current character is '1'.
                if s[j] == '1':
                    oneCnt += 1

                # Once the substring contains more than k '1's,
                # extending it further can never make it valid again.
                if oneCnt > k:
                    break

                # A beautiful substring must contain exactly k '1's.
                if oneCnt == k:

                    # Update the answer if:
                    # 1. No answer has been found yet,
                    # 2. The current substring is shorter, or
                    # 3. Both have the same length but the current one
                    #    is lexicographically smaller.
                    if (
                        ans == ""
                        or len(cur) < len(ans)
                        or (len(cur) == len(ans) and cur < ans)
                    ):
                        ans = cur

        # Return the shortest lexicographically smallest valid substring.
        return ans