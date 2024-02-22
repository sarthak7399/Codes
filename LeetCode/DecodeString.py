# https://leetcode.com/problems/decode-string/description/?envType=study-plan-v2&envId=leetcode-75

# Example 1:
# Input: s = "3[a]2[bc]"
# Output: "aaabcbc"

# Example 2:
# Input: s = "3[a2[c]]"
# Output: "accaccacc"

class Solution:
    def decodeString(self, s: str) -> str:
        st = []         
        for char in s:
            if char != ']':
                st.append(char)
            else:                       # When encountering ']', start decoding
                substr = ''
                while st and st[-1] != '[':
                    substr = st.pop() + substr   #substr conatins letters upto last '['
                st.pop()         # Pop '['

                count = ''
                while st and st[-1].isdigit():    # Extracting the repetition count
                    count = st.pop() + count     #count = pop + count because what if the number is more than single digit
                
                st.append(int(count) * substr)   # Repeat the substring

        return ''.join(st)
