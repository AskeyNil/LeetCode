/*
 * Description: 找到所有数组中消失的数字
 * Author: AskeyNil
 * CreateDate: 2019-09-22 20:02:25
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
  vector<int> findDisappearedNumbers(vector<int> &nums) {
    vector<int> v;
    for (auto num : nums) {
      nums[(num - 1) % nums.size()] += nums.size();
    }
    for (size_t i = 0; i < nums.size(); i++) {
      if (nums[i] <= nums.size()) {
        v.push_back(i + 1);
      }
    }
    return v;
  }
};