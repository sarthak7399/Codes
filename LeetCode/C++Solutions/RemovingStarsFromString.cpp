// https://leetcode.com/problems/removing-stars-from-a-string/description/?envType=study-plan-v2&envId=leetcode-75

// Example 1:
// Input: s = "leet**cod*e"
// Output: "lecoe"
// Explanation: Performing the removals from left to right:
// - The closest character to the 1st star is 't' in "leet**cod*e". s becomes "lee*cod*e".
// - The closest character to the 2nd star is 'e' in "lee*cod*e". s becomes "lecod*e".
// - The closest character to the 3rd star is 'd' in "lecod*e". s becomes "lecoe".
// There are no more stars, so we return "lecoe".

// Example 2:
// Input: s = "erase*****"
// Output: ""
// Explanation: The entire string is removed, so we return an empty string.


#include<bits/stdc++.h>
using namespace std;
class Solution {
public:
    string removeStars(string s) {
        stack<char> st;
        int i=0;
        while(i<s.size()){
            if(char(s[i])=='*' && i>0){
                st.pop();
            }
            if(char(s[i])!='*')
                st.push(s[i]);
            i+=1;
        }
        
        string ans="";
        while (!st.empty()) {
            ans+=st.top();
            st.pop();
        }
        
        reverse(ans.begin(), ans.end());
        return ans;
    }
};