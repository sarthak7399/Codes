# https://leetcode.com/problems/destroying-asteroids/

# Example 1:
# Input: mass = 10, asteroids = [3,9,19,5,21]
# Output: true
# Explanation: One way to order the asteroids is [9,19,5,3,21]:
# - The planet collides with the asteroid with a mass of 9. New planet mass: 10 + 9 = 19
# - The planet collides with the asteroid with a mass of 19. New planet mass: 19 + 19 = 38
# - The planet collides with the asteroid with a mass of 5. New planet mass: 38 + 5 = 43
# - The planet collides with the asteroid with a mass of 3. New planet mass: 43 + 3 = 46
# - The planet collides with the asteroid with a mass of 21. New planet mass: 46 + 21 = 67
# All asteroids are destroyed.

from typing import List

class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
        # Process asteroids in increasing order of size
        asteroids.sort()

        # Current mass of the planet
        curr_mass = mass

        # Try to destroy each asteroid
        for asteroid in asteroids:

            # Cannot destroy asteroid if it is larger than current mass
            if curr_mass < asteroid:
                return False

            # Destroy asteroid and gain its mass
            curr_mass += asteroid

        # Successfully destroyed all asteroids
        return True