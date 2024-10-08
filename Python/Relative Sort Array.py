# https://leetcode.com/problems/relative-sort-array/

# Example 2:
# Input: arr1 = [28,6,22,8,44,17], arr2 = [22,28,8,6]
# Output: [22,28,8,6,17,44]

# Counting Sort , T: O(m+n+k) , S: O(k)
class Solution:
    def relativeSortArray(self, arr1, arr2):
        from collections import defaultdict

        count_map = defaultdict(int)
        remaining = []
        result = []

        # Initialize count map with relative order elements
        for num in arr2:
            count_map[num] = 0

        # Count occurrences of elements in target array
        for num in arr1:
            if num in count_map:
                count_map[num] += 1
            else:
                remaining.append(num)

        # Sort the remaining elements
        remaining.sort()

        # Add elements as per relative order
        for num in arr2:
            result.extend([num] * count_map[num])

        # Add remaining elements
        result.extend(remaining)

        return result