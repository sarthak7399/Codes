# https://leetcode.com/problems/construct-string-with-repeat-limit/

# Example 1:
# Input: s = "cczazcc", repeatLimit = 3
# Output: "zzcccac"
# Explanation: We use all of the characters from s to construct the repeatLimitedString "zzcccac".
# The letter 'a' appears at most 1 time in a row.
# The letter 'c' appears at most 3 times in a row.
# The letter 'z' appears at most 2 times in a row.
# Hence, no letter appears more than repeatLimit times in a row and the string is a valid repeatLimitedString.
# The string is the lexicographically largest repeatLimitedString possible so we return "zzcccac".
# Note that the string "zzcccca" is lexicographically larger but the letter 'c' appears more than 3 times in a row, so it is not a valid repeatLimitedString.

from heapq import heappush, heappop
class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        # Count frequency of each character
        alphabets = {}
        for letter in s:
            alphabets[letter] = alphabets.get(letter, 0) + 1
        
        # Create a max-heap with negative ASCII values for descending order
        max_heap = []
        for key, value in alphabets.items():
            heappush(max_heap, (-ord(key), key, value))  # Push (-ASCII, char, freq)

        answer = []
        while max_heap:
            _, char, freq = heappop(max_heap)
            # Add as many of the current character as allowed by the repeat limit
            add_count = min(freq, repeatLimit)
            answer.append(char * add_count)
            
            remaining = freq - add_count
            
            if remaining > 0:
                # If there are remaining characters, we need to add another character
                if max_heap:
                    # Pop the next largest character
                    _, next_char, next_freq = heappop(max_heap)
                    answer.append(next_char)
                    # Push back the remaining frequency of the next character
                    if next_freq > 1:
                        heappush(max_heap, (-ord(next_char), next_char, next_freq - 1))
                    
                    # Push back the current character with its remaining frequency
                    heappush(max_heap, (-ord(char), char, remaining))
                else:
                    # If no other characters are available, break
                    break

        return ''.join(answer)
