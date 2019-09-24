/*
 * Description: 最长连续递增序列
 * Author: AskeyNil
 * CreateDate: 2019-09-24 09:13:37
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
    int findLengthOfLCIS(vector<int> &nums) {
        if (nums.empty())
            return 0;
        int max_count = 0, count = 1, *left = nullptr;
        for (int &num : nums) {
            if (left != nullptr) {
                if (num > *left)
                    count += 1;
                else {
                    if (max_count < count)
                        max_count = count;
                    count = 1;
                }
            }
            left = &num;
        }
        return max_count > count ? max_count : count;
    }
};