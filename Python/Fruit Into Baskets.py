# https://leetcode.com/problems/fruit-into-baskets/

# Example 1:
# Input: fruits = [1,2,1]
# Output: 3
# Explanation: We can pick from all 3 trees.

from collections import defaultdict

class Solution:
    def totalFruit(self, fruits: list[int]) -> int:
        start = 0                          # Start of the sliding window
        max_len = 0                        # To track the maximum length of valid subarray
        fruit_count = defaultdict(int)    # To count the number of each type of fruit in the window

        # Expand the sliding window using 'end' pointer
        for end in range(len(fruits)):
            fruit_count[fruits[end]] += 1  # Include current fruit in the count

            # If more than 2 types of fruits, shrink the window from the start
            while len(fruit_count) > 2:
                fruit_count[fruits[start]] -= 1  # Remove one fruit from start
                if fruit_count[fruits[start]] == 0:
                    del fruit_count[fruits[start]]  # Remove fruit type if count becomes 0
                start += 1  # Move start pointer forward to make window valid

            # Update max_len if current window is longer
            max_len = max(max_len, end - start + 1)

        return max_len  # Return the maximum number of fruits that can be picked
