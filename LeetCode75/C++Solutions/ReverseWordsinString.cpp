// https://leetcode.com/problems/reverse-words-in-a-string/description/?envType=study-plan-v2&envId=leetcode-75

// Input: s = "a good   example"
// Output: "example good a"
// Explanation: You need to reduce multiple spaces between two words to a single space in the reversed string.


#include<bits/stdc++.h>
using namespace std;
class Solution {
public:
    string reverseWords(string s) {
        vector<string>v;
        istringstream in(s); 
        string word;
        while(in>>word){
            v.push_back(word);
        }
        string ans;
        for(int i=v.size()-1;i>=0;i--){
            if (i != v.size() - 1) ans += " ";
            ans += v[i];
        }
        return ans;
    }
};

