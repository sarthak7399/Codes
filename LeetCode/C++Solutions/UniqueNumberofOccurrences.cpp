// https://leetcode.com/problems/unique-number-of-occurrences/?envType=study-plan-v2&envId=leetcode-75

// Example 1:
// Input: arr = [1,2,2,1,1,3]
// Output: true
// Explanation: The value 1 has 3 occurrences, 2 has 2 and 3 has 1. No two values have the same number of occurrences.

// Example 2:
// Input: arr = [1,2]
// Output: false



#include<bits/stdc++.h>
using namespace std;
class Solution {
public:
    bool uniqueOccurrences(vector<int>& arr) {
        unordered_map<int,int> temp;
        for (int i = 0; i < arr.size(); i++) 
            temp[(arr[i])]++;

        vector<int> v;
        for (auto x : temp){
            // cout << x.first << " " << x.second << endl;
            v.push_back(x.second);
        }
        std::sort(v.begin(), v.end());
        
        for (int i = 0; i < v.size()-1; i++) {
            if(v[i]==v[i+1]){return 0;}
        }

        return 1;
    }
};