/*
 * Description: 非递减数列
 * Author: AskeyNil
 * CreateDate: 2019-09-23 15:24:06
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
    bool checkPossibility(vector<int> &nums) {
        int p = -1;
        for (size_t i = 0; i < nums.size() - 1; i++) {
            if (nums[i] > nums[i + 1]) {
                if (p != -1)
                    return false;
                p = i;
            }
        }
        return (p == -1 || p == 0 || p == nums.size() - 2 ||
                nums[p - 1] <= nums[p + 1] || nums[p] <= nums[p + 2]);
    }
};