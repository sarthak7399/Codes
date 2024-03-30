# https://leetcode.com/problems/subarrays-with-k-different-integers/description/?envType=daily-question&envId=2024-03-29

# Example 1:
# Input: nums = [1,2,1,2,3], k = 2
# Output: 7
# Explanation: Subarrays formed with exactly 2 different integers: [1,2], [2,1], [1,2], [2,3], [1,2,1], [2,1,2], [1,2,1,2]

from typing import List
# Method 1 : Recursion - Time Complexity O(N), Space Complexity O(N)
class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        def atMostK(nums: List[int], k: int) -> int:    # Define a helper function to count subarrays with at most k distinct integers            
            count, left, ans = {}, 0, 0  # Initialize a dictionary to store count of each integer, left pointer, and answer
            for right in range(len(nums)):  # Iterate through the array using a sliding window approach
                count[nums[right]] = count.get(nums[right], 0) + 1  # Update the count of the current integer
                while len(count) > k:  # Adjust the window if the number of distinct integers exceeds k
                    count[nums[left]] -= 1  # Decrement count for the leftmost integer in the window
                    if count[nums[left]] == 0:  # If count becomes zero, remove the integer from the dictionary
                        del count[nums[left]]
                    left += 1  # Move the left pointer to the right to shrink the window
                ans += right - left + 1  # Update the answer by adding the number of valid subarrays in the current window
            return ans  # Return the total count of subarrays with at most k distinct integers
        
        # Calculate the result by subtracting count of subarrays with at most k - 1 distinct integers
        return atMostK(nums, k) - atMostK(nums, k - 1)

# # Method 2 : Iterative Dictionary - Time Complexity O(N), Space Complexity O(N)
# class Solution:
#     def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
#         counter = {}  # Initialize a dictionary to count the frequency of each integer
#         pre_cnt = 0  # Initialize a variable to count the number of subarrays with exactly k distinct integers
#         l = 0  # Initialize a left pointer
#         res = 0  # Initialize the result variable to store the count of good subarrays
#         for r in range(len(nums)):  # Iterate through the array using a sliding window approach
#             counter[nums[r]] = counter.get(nums[r], 0) + 1  # Update the count of the current integer
#             if len(counter) > k:  # If the number of distinct integers exceeds k
#                 counter.pop(nums[l])  # Remove the leftmost integer from the dictionary
#                 l += 1  # Move the left pointer to the right to shrink the window
#                 pre_cnt = 0  # Reset the pre_cnt variable as the count of subarrays with exactly k distinct integers
#             while counter[nums[l]] > 1:  # While the count of the leftmost integer is greater than 1
#                 counter[nums[l]] -= 1  # Decrement the count of the leftmost integer
#                 pre_cnt += 1  # Increment the pre_cnt variable
#                 l += 1  # Move the left pointer to the right
#             if len(counter) == k:  # If the number of distinct integers is exactly k
#                 res += pre_cnt + 1  # Add the count of subarrays with exactly k distinct integers to the result
#         return res  # Return the total count of good subarrays
