# https://leetcode.com/problems/longest-balanced-substring-ii/

# Example 1:
# Input: s = "abbac"
# Output: 4
# Explanation:
# The longest balanced substring is "abba" because both distinct characters 'a' and 'b' each appear exactly 2 times.

class Solution:
    def longestBalanced(self, s: str) -> int:
        # We try multiple strategies:
        # 1. Substring containing only one character (a / b / c)
        # 2. Balanced substring between any two characters
        # 3. Balanced substring among all three characters
        
        results = [
            self._solve1(s, 'a'),
            self._solve1(s, 'b'),
            self._solve1(s, 'c'),
            self._solve2(s, 'a', 'b'),
            self._solve2(s, 'a', 'c'),
            self._solve2(s, 'b', 'c'),
            self._solve3(s),
        ]
        # Return maximum length found
        return max(results)

    # ---------------------------------------------------
    # CASE 1: Longest continuous block of SAME character
    # ---------------------------------------------------
    def _solve1(self, s: str, t: str) -> int:
        result = 0     # stores maximum length
        count = 0      # current consecutive count
        
        for c in s:
            if c == t:
                count += 1           # extend streak
                if count > result:
                    result = count
            else:
                count = 0            # reset streak
        
        return result

    # ---------------------------------------------------
    # CASE 2: Balanced substring between TWO characters
    # Example: equal number of 'a' and 'b'
    # ---------------------------------------------------
    def _solve2(self, s: str, t1: str, t2: str) -> int:
        result = 0
        
        counts0 = 0   # count of t1
        counts1 = 0   # count of t2
        
        # stores first index where a difference appeared
        previous = {}
        
        for i, c in enumerate(s):
            
            # if character is not part of this pair
            # reset everything
            if c != t1 and c != t2:
                previous.clear()
                counts0 = 0
                counts1 = 0
            else:
                # update counters
                if c == t1:
                    counts0 += 1
                else:
                    counts1 += 1
                
                # if counts equal → balanced substring
                if counts0 == counts1:
                    v = counts0 * 2
                    if v > result:
                        result = v
                else:
                    # difference between counts
                    diff = counts0 - counts1
                    
                    # if same diff seen before,
                    # substring between them is balanced
                    if diff in previous:
                        v = i - previous[diff]
                        if v > result:
                            result = v
                    else:
                        previous[diff] = i
        
        return result

    # ---------------------------------------------------
    # CASE 3: Balanced substring among ALL THREE
    # equal number of a, b, and c
    # ---------------------------------------------------
    def _solve3(self, s: str) -> int:
        result = 0
        
        # counts of characters
        ca = cb = cc = 0
        
        # map storing previously seen differences
        previous = {}
        
        for i, ch in enumerate(s):
            # update counts
            if ch == 'a':
                ca += 1
            elif ch == 'b':
                cb += 1
            else:
                cc += 1
            
            # if all counts equal → whole prefix balanced
            if ca == cb and cb == cc:
                result = i + 1
            else:
                # encode pair of differences into one number
                # (ca-cb, cb-cc)
                diff = (ca - cb) * 100001 + (cb - cc)
                
                # if same diff seen earlier,
                # substring between indices is balanced
                if diff in previous:
                    v = i - previous[diff]
                    if v > result:
                        result = v
                else:
                    previous[diff] = i
        
        return result
