# https://leetcode.com/problems/the-k-th-lexicographical-string-of-all-happy-strings-of-length-n/

# Example 1:
# Input: n = 1, k = 3
# Output: "c"
# Explanation: The list ["a", "b", "c"] contains all happy strings of length 1. The third string is "c".

class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        # Recursive DFS to generate happy strings
        def dfs(prefix, n, k):
            if n == 0:  # Base case: when the string reaches length `n`
                return prefix

            for c in 'abc':  # Iterate over 'a', 'b', and 'c'
                if prefix and c == prefix[-1]:  # Ensure no consecutive same letters
                    continue
                
                cnt = 2 ** (n2 - len(prefix) - 1)  # Count possible strings from this point
                
                if cnt >= k:  # If `k` falls within this range, continue building the string
                    return dfs(prefix + c, n - 1, k)
                else:
                    k -= cnt  # Reduce `k` to skip these combinations

            return ""  # If `k` exceeds total possibilities, return an empty string
        
        n2 = n  # Store the original value of `n`
        return dfs("", n, k)  # Start the recursive DFS
