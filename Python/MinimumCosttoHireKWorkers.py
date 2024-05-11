# https://leetcode.com/problems/minimum-cost-to-hire-k-workers/

# Example 1:
# Input: quality = [10,20,5], wage = [70,50,30], k = 2
# Output: 105.00000
# Explanation: We pay 70 to 0th worker and 35 to 2nd worker.

from typing import List
class Solution:
    def mincostToHireWorkers(
        self, quality: List[int], wage: List[int], k: int ) -> float:
        
        # Calculate the wage-to-quality ratio for each worker and sort them
        wage_quality_ratio = sorted([(w / q, q) for w, q in zip(wage, quality)])
        
        # Initialize a max heap to track the highest quality workers
        max_heap = []
        
        # Initialize variables to track total quality and maximum ratio
        total_quality = 0
        max_ratio = 0.0
        
        # Select the first k workers with the lowest wage-to-quality ratios
        for i in range(k):
            max_ratio = max(max_ratio, wage_quality_ratio[i][0])
            total_quality += wage_quality_ratio[i][1]
            heapq.heappush(max_heap, -wage_quality_ratio[i][1])
        
        # Initialize the result with the cost of hiring the first k workers
        result = max_ratio * total_quality
        
        # Iterate through the remaining workers
        for i in range(k, len(quality)):
            max_ratio = max(max_ratio, wage_quality_ratio[i][0])
            total_quality += wage_quality_ratio[i][1] + heapq.heappop(max_heap)
            heapq.heappush(max_heap, -wage_quality_ratio[i][1])
            result = min(result, max_ratio * total_quality)
        
        return result
