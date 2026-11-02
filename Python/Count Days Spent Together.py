# https://leetcode.com/problems/count-days-spent-together/

# Example 1:
# Input: arriveAlice = "08-15", leaveAlice = "08-18", arriveBob = "08-16", leaveBob = "08-19"
# Output: 3
# Explanation: Alice will be in Rome from August 15 to August 18. Bob will be in Rome from August 16 to August 19. They are both in Rome together on August 16th, 17th, and 18th, so the answer is 3.

class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        # Find the later arrival date and the earlier departure date.
        # These dates define the possible overlapping period.
        # Convert both dates to day numbers and calculate the overlap.
        # Add 1 because both the arrival and departure days are inclusive.
        # Return 0 if there is no overlap.
        return max(0, self.getDate(min(leaveAlice, leaveBob)) - self.getDate(max(arriveAlice, arriveBob)) + 1)

    def getDate(self, date):
        # Number of days in each month (assuming a non-leap year).
        monthList = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        # Extract the month and day from the MM-DD date string.
        month = int(date[:2])
        days = int(date[3:])

        # Add the days in all previous months to get the day number of the year.
        return sum(monthList[: month - 1]) + days