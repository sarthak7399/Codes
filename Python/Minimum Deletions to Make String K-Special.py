# https://leetcode.com/problems/minimum-deletions-to-make-string-k-special/

# Example 1:
# Input: word = "aabcaba", k = 0
# Output: 3
# Explanation: We can make word 0-special by deleting 2 occurrences of "a" and 1 occurrence of "c". Therefore, word becomes equal to "baba" where freq('a') == freq('b') == 2.

class Solution(object):
    def minimumDeletions(self, word, k):
        # Step 1: Count frequency of each character in the word
        freq = [0] * 26
        for ch in word:
            freq[ord(ch) - ord('a')] += 1

        # Step 2: Filter out characters that appear at least once
        freq_list = [f for f in freq if f > 0]

        # Sort the frequency list to facilitate sliding window approach
        freq_list.sort()

        n = len(freq_list)
        total = len(word)  # Total characters in the word
        removed_left = 0   # Cumulative sum of frequencies removed from the left
        window_sum = 0     # Sum of current sliding window (valid frequencies)
        result = total     # Initialize result to maximum deletions (worst case)
        r = 0              # Right pointer for the sliding window

        # Try every frequency as a base to normalize all other frequencies to (within k)
        for l in range(n):
            base = freq_list[l]
            limit = base + k  # Max allowed frequency in the window

            # Expand the window to the right where all frequencies ≤ limit
            while r < n and freq_list[r] <= limit:
                window_sum += freq_list[r]
                r += 1

            # Calculate how many characters to delete from the right side of the window
            right_count = n - r                  # Number of frequencies greater than limit
            right_sum = total - window_sum       # Total characters in the right part
            del_right = right_sum - right_count * limit  # Deletions needed to reduce them to `limit`

            # Total deletions = left-side removals + right-side deletions
            curr = removed_left + del_right
            result = min(result, curr)  # Track minimum deletions

            # Slide the window to the right: remove current left frequency from totals
            total -= base
            removed_left += base
            window_sum -= base

        return result
