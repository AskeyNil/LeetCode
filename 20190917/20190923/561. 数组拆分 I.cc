/*
 * Description: 数组拆分 I
 * Author: AskeyNil
 * CreateDate: 2019-09-23 09:35:03
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
    int arrayPairSum(vector<int> &nums) {
        sort(nums.begin(), nums.end());
        int sum = 0;
        for (auto i = nums.begin(); i < nums.end(); i += 2) {
            sum += *i;
        }
        return sum;
    }
};