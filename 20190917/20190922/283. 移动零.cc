/*
 * Description: 移动零
 * Author: AskeyNil
 * CreateDate: 2019-09-22 18:22:19
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

// 简单的做法
// class Solution {
// public:
//   void moveZeroes(vector<int> &nums) {
//     int index = 0, length = nums.size();
//     for (int i = 0; i < length; i++) {
//       if (nums[i] == 0) {
//         nums.erase(nums.begin() + i);
//         nums.push_back(0);
//         length -= 1;
//         i -= 1;
//       }
//     }
//   }
// };

// 双指针
class Solution {
public:
  void moveZeroes(vector<int> &nums) {
    int left = 0, right = 0, count = nums.size();
    while (left < count) {
      if (right < count) {
        if (nums[right] != 0) {
          nums[left++] = nums[right];
        }
        right += 1;
      } else {
        nums[left++] = 0;
      }
    }
  }
};