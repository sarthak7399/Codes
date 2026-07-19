# https://leetcode.com/problems/total-waviness-of-numbers-in-range-ii/

# Example 1:
# Input: num1 = 120, num2 = 130
# Output: 3
# Explanation:
# In the range [120, 130]:
# 120: middle digit 2 is a peak, waviness = 1.
# 121: middle digit 2 is a peak, waviness = 1.
# 130: middle digit 3 is a peak, waviness = 1.
# All other numbers in the range have a waviness of 0.
# Thus, total waviness is 1 + 1 + 1 = 3.

class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:

        from functools import lru_cache

        # Returns total waviness of all numbers in range [0, n]
        def solve(n: int) -> int:

            if n < 0:
                return 0

            s = str(n)

            @lru_cache(None)
            def dfs(pos, started, last, second_last, tight):
                """
                pos         -> current digit position
                started     -> whether a non-leading-zero digit has appeared
                last        -> previous digit
                second_last -> digit before previous digit
                tight       -> whether current prefix matches n exactly

                Returns:
                    (count_of_numbers, total_waviness)
                """

                # Reached end of number
                if pos == len(s):
                    return (1, 0)

                # Maximum digit allowed at this position
                limit = int(s[pos]) if tight else 9

                total_cnt = 0
                total_wav = 0

                # Try every possible digit
                for d in range(limit + 1):

                    ntight = tight and d == limit

                    # Still in leading zeros
                    if not started and d == 0:

                        cnt, wav = dfs(
                            pos + 1,
                            False,
                            10,      # sentinel value
                            10,      # sentinel value
                            ntight
                        )

                        total_cnt += cnt
                        total_wav += wav

                    else:

                        # Additional waviness contributed by the
                        # current 3-digit window
                        add = 0

                        # We need at least 3 digits to form a wave
                        if started and second_last != 10:

                            # Check if the middle digit (last)
                            # forms a peak or valley
                            if (
                                (last > second_last and last > d)
                                or
                                (last < second_last and last < d)
                            ):
                                add = 1

                        # Shift digit history:
                        # second_last <- last
                        # last <- current digit
                        n_second_last = last if started else 10

                        cnt, wav = dfs(
                            pos + 1,
                            True,
                            d,
                            n_second_last,
                            ntight
                        )

                        total_cnt += cnt

                        # Add:
                        # 1. waviness from suffix numbers
                        # 2. waviness formed at current position
                        total_wav += wav + add * cnt

                return (total_cnt, total_wav)

            # Return total waviness from 0 to n
            return dfs(0, False, 10, 10, True)[1]

        # Total waviness in range [num1, num2]
        return solve(num2) - solve(num1 - 1)