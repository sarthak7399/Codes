# https://leetcode.com/problems/angle-between-hands-of-a-clock/

# Example 1:
# Input: hour = 12, minutes = 30
# Output: 165

class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        # Each minute mark corresponds to 6 degrees
        # (360 / 60 = 6)
        minute_angle = 6.0 * minutes

        # Each hour mark corresponds to 30 degrees
        # (360 / 12 = 30)
        #
        # The hour hand also moves continuously:
        # 0.5 degrees per minute (30 / 60)
        hour_angle = 30.0 * (hour % 12) + 0.5 * minutes

        # Absolute angle between the two hands
        diff = abs(hour_angle - minute_angle)

        # Return the smaller angle between them
        return min(diff, 360.0 - diff)