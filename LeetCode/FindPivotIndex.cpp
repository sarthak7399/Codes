// https://leetcode.com/problems/find-pivot-index/description/?envType=study-plan-v2&envId=leetcode-75

// Input: nums = [1,7,3,6,5,6]
// Output: 3
// Explanation:
// The pivot index is 3.
// Left sum = nums[0] + nums[1] + nums[2] = 1 + 7 + 3 = 11
// Right sum = nums[4] + nums[5] = 5 + 6 = 11
// Otherwise 0


#include<bits/stdc++.h>
using namespace std;
class Solution {
public:
    int pivotIndex(vector<int>& nums) {
        int i=0,sum=0,suml=0;
        for (i=0; i<nums.size(); i++) sum+=nums[i];
        for (i=0; i<nums.size(); i++) {
            if(suml==(sum-nums.at(i)-suml)){
                return i;
            }
            suml+=nums.at(i);
        }
        return -1;
    }
};