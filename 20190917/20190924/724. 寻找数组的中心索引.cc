/*
 * Description: 寻找数组的中心索引
 * Author: AskeyNil
 * CreateDate: 2019-09-24 11:32:28
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
#include <numeric>
#include <vector>

using namespace std;

class Solution {
  public:
    int pivotIndex(vector<int> &nums) {
        int length = nums.size(), *left = nullptr, *right = nullptr;
        int cur_index = -1;
        for (int index = 0; index < length; index++) {
            if (left == nullptr) {
                left = new int(0);
                right = new int(accumulate(nums.begin() + 1, nums.end(), 0));
            } else {
                *left += nums[index - 1];
                *right -= nums[index];
            }
            if (left == right) {
                cur_index = index;
                break;
            }
        }
        delete left, delete right;
        return cur_index;
    }
};
