/*
 * Description: 三个数的最大乘积
 * Author: AskeyNil
 * CreateDate: 2019-09-23 11:57:40
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
    int maximumProduct(vector<int> &nums) {
        sort(nums.begin(), nums.end());
        int max_number = nums[nums.size() - 1] * nums[nums.size() - 2] *
                         nums[nums.size() - 3];
        int min_number = nums[nums.size() - 1] * nums[0] * nums[1];
        return max_number > min_number ? max_number : min_number;
    }
};