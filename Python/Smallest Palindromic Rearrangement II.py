# https://leetcode.com/problems/smallest-palindromic-rearrangement-ii/

# Example 1:
# Input: s = "abba", k = 2
# Output: "baab"
# Explanation:
# The two distinct palindromic rearrangements of "abba" are "abba" and "baab".
# Lexicographically, "abba" comes before "baab". Since k = 2, the output is "baab".

class Solution:
    def smallestPalindrome(self, s: str, k: int) -> str:
        from collections import Counter
        import math

        # Count the frequency of every character
        freq = Counter(s)

        # half stores the number of each character
        # required in the first half of the palindrome
        half = {}

        # Stores the middle character for an odd-length palindrome
        mid = ""

        # Total length of the first half
        m = 0

        # Process characters in alphabetical order
        for char in "abcdefghijklmnopqrstuvwxyz":
            if freq[char] > 0:

                # A character with an odd frequency contributes
                # one occurrence to the middle of the palindrome
                if freq[char] % 2 != 0:
                    mid += char

                # Half of the remaining occurrences are placed
                # in the first half, while the other half is mirrored
                half[char] = freq[char] // 2
                m += half[char]

        def get_ways(f, target_k):
            # Calculate the number of distinct permutations
            # possible using the remaining characters
            ways = 1
            curr_len = 0

            for char in "abcdefghijklmnopqrstuvwxyz":
                count = f.get(char, 0)

                if count > 0:
                    # Add the current character count to the
                    # number of characters considered so far
                    curr_len += count

                    # Choose positions for the current character
                    ways *= math.comb(curr_len, count)

                    # Stop early when the count exceeds k,
                    # since an exact larger value is unnecessary
                    if ways > target_k:
                        return target_k + 1

            return ways

        # If fewer than k distinct palindromes are possible,
        # the k-th lexicographically smallest palindrome does not exist
        if get_ways(half, k) < k:
            return ""

        # Construct the first half of the k-th smallest palindrome
        first_half = []

        for _ in range(m):

            # Try each character in lexicographical order
            for char in "abcdefghijklmnopqrstuvwxyz":

                if half.get(char, 0) > 0:

                    # Temporarily place the character
                    half[char] -= 1

                    # Count the possible arrangements after
                    # fixing the current character
                    ways = get_ways(half, k)

                    # The k-th palindrome starts with this character
                    if ways >= k:
                        first_half.append(char)
                        break

                    else:
                        # Skip all arrangements beginning with
                        # this character and update k
                        k -= ways

                        # Restore the character and try the next one
                        half[char] += 1

        # Convert the constructed first half into a string
        first_str = "".join(first_half)

        # Mirror the first half around the middle character
        # to form the complete palindrome
        return first_str + mid + first_str[::-1]