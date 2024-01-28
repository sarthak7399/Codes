// https://leetcode.com/problems/merge-strings-alternately/description/?envType=study-plan-v2&envId=leetcode-75

// Input: word1 = "ab", word2 = "pqrs"
// Output: "apbqrs"
// Explanation: Notice that as word2 is longer, "rs" is appended to the end.
// word1:  a   b 
// word2:    p   q   r   s
// merged: a p b q   r   s


#include<bits/stdc++.h>
using namespace std;
class Solution {
public:
    string mergeAlternately(string word1, string word2){
        string result = "";
        int i = 0;
        while (i < word1.length() || i < word2.length()) {
            if (i < word1.length()) {
                result += word1[i];
            }
            if (i < word2.length()) {
                result += word2[i];
            }
            i++;
        }
        return result;
    }
};




// IN PYTHON

// class Solution:
//     def mergeAlternately(self, word1: str, word2: str) -> str:
//         result=""
//         i=0
//         while(i<len(word1) or i<len(word2)):
//             if (i < len(word1)):
//                 result += word1[i]
//             if (i < len(word2)):
//                 result += word2[i]
//             i+=1
//         return result