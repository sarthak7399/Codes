# https://leetcode.com/problems/brace-expansion-ii/

# Example 2:
# Input: expression = "{{a,z},a{b,c},{ab,z}}"
# Output: ["a","ab","ac","z"]
# Explanation: Each distinct word is written only once in the final answer.

class Solution:
    def braceExpansionII(self, expression):
        # Set is used to store unique expanded strings.
        ans = set()

        def dfs(s):
            # Find the first closing brace.
            r = s.find('}')

            # No braces are left, so the expression is fully expanded.
            if r == -1:
                ans.add(s)
                return

            # Find the matching opening brace for this closing brace.
            l = s.rfind('{', 0, r)

            # Parts before and after the current braces.
            left = s[:l]
            right = s[r + 1:]

            # Get the content inside the braces.
            inside = s[l + 1:r]

            # Try each comma-separated option inside the braces.
            for part in inside.split(','):
                # Replace the current { ... } with the selected part
                # and recursively expand any remaining braces.
                dfs(left + part + right)

        # Start the recursive expansion.
        dfs(expression)

        # Return all unique results in lexicographical order.
        return sorted(ans)