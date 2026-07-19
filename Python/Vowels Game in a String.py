# https://leetcode.com/problems/vowels-game-in-a-string/

# Example 1:
# Input: s = "leetcoder"
# Output: true
# Explanation:
# Alice can win the game as follows:
# Alice plays first, she can delete the underlined substring in s = "leetcoder" which contains 3 vowels. The resulting string is s = "der".
# Bob plays second, he can delete the underlined substring in s = "der" which contains 0 vowels. The resulting string is s = "er".
# Alice plays third, she can delete the whole string s = "er" which contains 1 vowel.
# Bob plays fourth, since the string is empty, there is no valid play for Bob. So Alice wins the game.

# Method 1 : 
class Solution:
    def doesAliceWin(self, s: str) -> bool:
        vowels = set('aeiou')   # Set of vowels for quick lookup

        # Counters for number of prefixes with even and odd parity
        even = 1   # empty prefix counts as "even parity"
        odd = 0
        parity = 0 # 0 = even, 1 = odd (number of vowels so far)

        for ch in s:
            if ch in vowels:
                # Flip parity when encountering a vowel
                parity ^= 1

            # Count prefix by parity
            if parity == 0:
                even += 1
            else:
                odd += 1

        # Alice wins if there exists at least one even-parity prefix
        # and at least one odd-parity prefix
        return even * odd > 0


# Method 2 : 
class Solution:
    def doesAliceWin(self, s: str) -> bool:
        # Count how many vowels are in the string
        count = s.count("a") + s.count("e") + s.count("i") + s.count("o") + s.count("u")

        if count == 0:
            return False   # No vowels -> Alice cannot win

        if count % 2 != 0:
            return True    # Odd number of vowels -> Alice wins

        if count % 2 == 0:
            return True    # Even number of vowels -> Alice also wins
