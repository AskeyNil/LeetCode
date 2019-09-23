/*
 * Description: 最短无序连续子数组
 * Author: AskeyNil
 * CreateDate: 2019-09-23 10:25:56
 * LastEditors: AskeyNil
 *
 * *********************************
 * **                             **
 * **     　  你只有足够努力     　  **
 * **       才能看上去毫不费力       **
 * **                             **
 * *********************************
 *
 */

#include <iostream>
#include <vector>

using namespace std;

class Solution {
  public:
    int findUnsortedSubarray(vector<int> &nums) {
        vector<int> vv = nums;
        sort(vv.begin(), vv.end());
        int start = -1, end = -1;
        for (int i = 0; i < nums.size(); i++) {
            if (start == -1 && nums[i] != vv[i])
                start = i;
            else if (end == -1 && nums[i] == vv[i])
                end = i - 1;
            else if (end != -1 && nums[i] != vv[i])
                end = i;
        }
        if (end == -1)
            end = nums.size() - 1;
        if (start == -1)
            return 0;
        return end - start + 1;
    }
};