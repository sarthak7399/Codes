# https://leetcode.com/problems/divide-an-array-into-subarrays-with-minimum-cost-ii/

# Example 2:
# Input: nums = [10,1,2,2,2,1], k = 4, dist = 3
# Output: 15
# Explanation: The best possible way to divide nums into 4 subarrays is: [10], [1], [2], and [2,2,1]. This choice is valid because ik-1 - i1 is 3 - 1 = 2 which is less than dist. The total cost is nums[0] + nums[1] + nums[2] + nums[3] which is 10 + 1 + 2 + 2 = 15.
# The division [10], [1], [2,2,2], and [1] is not valid, because the difference between ik-1 and i1 is 5 - 1 = 4, which is greater than dist.
# It can be shown that there is no possible way to divide nums into 4 subarrays at a cost lower than 15.

class Solution:
    def minimumCost(self, nums: List[int], k: int, dist: int) -> int:

        # Move the largest element from left_set to right_set
        def move_from_left_to_right():
            nonlocal current_sum
            element = left_set.pop()     # remove largest from left_set
            current_sum -= element
            right_set.add(element)

        # Move the smallest element from right_set to left_set
        def move_from_right_to_left():
            nonlocal current_sum
            element = right_set.pop(0)  # remove smallest from right_set
            left_set.add(element)
            current_sum += element

        k -= 1  # first element nums[0] is always included

        # Initial window sum includes nums[0] and next dist+1 elements
        current_sum = sum(nums[:dist + 2])

        # left_set holds k smallest elements contributing to the cost
        left_set = SortedList(nums[1:dist + 2])

        # right_set holds remaining elements in the window
        right_set = SortedList()

        # Balance left_set to contain exactly k elements
        while len(left_set) > k:
            move_from_left_to_right()

        min_cost = current_sum

        # Slide the window across the array
        for i in range(dist + 2, len(nums)):

            # Remove outgoing element
            outgoing_element = nums[i - dist - 1]
            if outgoing_element in left_set:
                left_set.remove(outgoing_element)
                current_sum -= outgoing_element
            else:
                right_set.remove(outgoing_element)

            # Add incoming element
            incoming_element = nums[i]
            if left_set and incoming_element < left_set[-1]:
                left_set.add(incoming_element)
                current_sum += incoming_element
            else:
                right_set.add(incoming_element)

            # Rebalance sets to maintain k elements in left_set
            while len(left_set) < k:
                move_from_right_to_left()
            while len(left_set) > k:
                move_from_left_to_right()

            # Update minimum cost
            min_cost = min(min_cost, current_sum)

        return min_cost
