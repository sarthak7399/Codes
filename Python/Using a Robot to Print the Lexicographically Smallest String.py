

# Example 1:
# Input: s = "zza"
# Output: "azz"
# Explanation: Let p denote the written string.
# Initially p="", s="zza", t="".
# Perform first operation three times p="", s="", t="zza".
# Perform second operation three times p="azz", s="", t="".

class Solution:
    def robotWithString(self, s: str) -> str:
        from collections import Counter

        ans = []  # Final answer string as a list of characters
        t = []    # Stack to temporarily hold characters
        freq = Counter(s)  # Count frequency of each character in the string
        sml = 'a'  # Smallest character we are looking to push directly to result

        for c in s:
            if c == sml:
                # If current character is the smallest available, push directly to result
                ans.append(c)
            else:
                # Otherwise, push it to the temporary stack `t`
                t.append(c)

            # Decrease the frequency of current character
            freq[c] -= 1
            if freq[c] == 0:
                del freq[c]  # Remove from counter when no more occurrences left

            # Update `sml` to be the smallest character still available in `freq`
            while sml <= 'z' and sml not in freq:
                sml = chr(ord(sml) + 1)

            # Check top of stack `t`, and if its value is ≤ smallest available character,
            # pop and push to result (ensures lexicographically smallest result)
            while t and t[-1] <= sml:
                ans.append(t.pop())

        # Append remaining characters from stack `t` if any
        while t:
            ans.append(t.pop())

        return ''.join(ans)
