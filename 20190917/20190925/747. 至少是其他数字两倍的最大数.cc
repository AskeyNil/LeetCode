/*
 * Description: 至少是其他数字两倍的最大数
 * Author: AskeyNil
 * CreateDate: 2019-09-25 07:45:22
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
    int dominantIndex(vector<int> &nums) {
        int i = -1, max_number = -2;
        for (int index = 0; index < nums.size(); index++) {
            if (max_number == -2) {
                i = index;
                max_number = nums[index];
            } else {
                if (max_number < nums[index]) {
                    if (max_number * 2 <= nums[index]) {
                        i = index;
                    } else {
                        i = -1;
                    }
                    max_number = nums[index];
                } else if (nums[index] * 2 > max_number) {
                    i = -1;
                }
            }
        }
        return i;
    }
};