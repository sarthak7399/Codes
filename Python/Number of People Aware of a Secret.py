# https://leetcode.com/problems/number-of-people-aware-of-a-secret/

# Example 1:
# Input: n = 6, delay = 2, forget = 4
# Output: 5
# Explanation:
# Day 1: Suppose the first person is named A. (1 person)
# Day 2: A is the only person who knows the secret. (1 person)
# Day 3: A shares the secret with a new person, B. (2 people)
# Day 4: A shares the secret with a new person, C. (3 people)
# Day 5: A forgets the secret, and B shares the secret with a new person, D. (3 people)
# Day 6: B shares the secret with E, and C shares the secret with F. (5 people)

class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        # aware[i] = number of people who first learn the secret on day i
        aware = [0] * n
        spread = 0  # number of people currently able to share the secret
        total = 1   # total people aware of the secret
        aware[0] = 1  # on day 0, one person knows the secret

        for day in range(1, n):
            # After 'delay' days, people can start spreading the secret
            if day >= delay:
                spread += aware[day - delay]
            
            # After 'forget' days, people completely forget the secret
            if day >= forget:
                forgot = aware[day - forget]
                total -= forgot   # remove them from total aware count
                spread -= forgot  # they also stop spreading
            
            # People who become aware today = all spreaders from today
            aware[day] = spread
            total += spread  # update total aware count
        
        # Return result modulo 1e9+7 (to avoid overflow)
        return total % (10 ** 9 + 7)
