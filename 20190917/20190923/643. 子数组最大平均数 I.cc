/*
 * Description: 子数组最大平均数 I
 * Author: AskeyNil
 * CreateDate: 2019-09-23 13:11:47
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
#include <string>
#include <vector>

using namespace std;

class Solution {
  public:
    double findMaxAverage(vector<int> &nums, int k) {
        int max_aver = INT_MIN, left = INT_MIN, aver = 0;
        for (int i = 0; i < nums.size() - k + 1; i++) {
            if (max_aver != INT_MIN) {
                aver = aver - left + nums[i + k - 1];
                if (max_aver < aver)
                    max_aver = aver;
            } else {
                for (int j = i; j < i + k; j++) {
                    aver += nums[j];
                }
                max_aver = aver;
            }
            left = nums[i];
        }
        return double(max_aver) / k;
    }
};