# https://leetcode.com/problems/defuse-the-bomb/

# Example 1:
# Input: code = [5,7,1,4], k = 3
# Output: [12,10,16,13]
# Explanation: Each number is replaced by the sum of the next 3 numbers. The decrypted code is [7+1+4, 1+4+5, 4+5+7, 5+7+1]. Notice that the numbers wrap around.

from typing import List
class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n = len(code)  # O(1): Length of the list.
        
        if k == 0:
            return [0] * n  # O(n): Return a list of zeros if k is 0.

        result = [0] * n  # O(n): Initialize the result list.
        
        # Determine the direction of the sliding window.
        start, end, step = (1, k + 1, 1) if k > 0 else (k, 0, 1)
        window_sum = sum(code[i % n] for i in range(start, end))  # O(k): Initialize the first window sum.

        for i in range(n):  # O(n): Slide the window across all positions.
            result[i] = window_sum  # Store the current window sum in the result.
            # Slide the window: Remove the outgoing element and add the incoming one.
            window_sum -= code[(i + start) % n]  # O(1): Remove outgoing element.
            window_sum += code[(i + end) % n]    # O(1): Add incoming element.
        
        return result  # O(1): Return the result list.