# https://leetcode.com/problems/shifting-letters-ii/

# Example 1:
# Input: s = "abc", shifts = [[0,1,0],[1,2,1],[0,2,1]]
# Output: "ace"
# Explanation: Firstly, shift the characters from index 0 to index 1 backward. Now s = "zac".
# Secondly, shift the characters from index 1 to index 2 forward. Now s = "zbd".
# Finally, shift the characters from index 0 to index 2 forward. Now s = "ace".

class Solution:
    def shiftingLetters(self, s: str, shifts: list[list[int]]) -> str:
        arr = [0] * len(s)
        
        # Step 1: Populate the difference array
        for start, end, direction in shifts:
            if direction == 1:
                arr[start] += 1
                if end + 1 < len(s):
                    arr[end + 1] -= 1
            else:
                arr[start] -= 1
                if end + 1 < len(s):
                    arr[end + 1] += 1

        # Step 2: Convert to prefix sum
        for i in range(1, len(arr)):
            arr[i] += arr[i - 1]

        # Step 3: Transform the string
        result = []
        for i, char in enumerate(s):
            shift = arr[i] % 26  # Normalize shift
            new_char = chr((ord(char) - ord('a') + shift + 26) % 26 + ord('a'))
            result.append(new_char)

        return ''.join(result)