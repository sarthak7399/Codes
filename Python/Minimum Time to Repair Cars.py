# https://leetcode.com/problems/minimum-time-to-repair-cars/

# Example 1:
# Input: ranks = [4,2,3,1], cars = 10
# Output: 16
# Explanation: 
# - The first mechanic will repair two cars. The time required is 4 * 2 * 2 = 16 minutes.
# - The second mechanic will repair two cars. The time required is 2 * 2 * 2 = 8 minutes.
# - The third mechanic will repair two cars. The time required is 3 * 2 * 2 = 12 minutes.
# - The fourth mechanic will repair four cars. The time required is 1 * 4 * 4 = 16 minutes.
# It can be proved that the cars cannot be repaired in less than 16 minutes.​​​​​

from typing import List

class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        left = 1  # Minimum possible time
        right = min(ranks) * cars * cars  # Maximum possible time
        
        # Function to check if all cars can be repaired within 'time'
        def can_repair_all(time):
            total_cars_repaired = 0
            for rank in ranks:
                cars_repaired = int((time / rank) ** 0.5)  # Cars repaired by this mechanic
                total_cars_repaired += cars_repaired
                if total_cars_repaired >= cars:  # If enough cars are repaired
                    return True
            return False
        
        # Binary search for the minimum required time
        while left < right:
            mid = (left + right) // 2
            if can_repair_all(mid):
                right = mid  # Try a smaller time
            else:
                left = mid + 1  # Increase time
        
        return left  # Minimum time required to repair all cars
