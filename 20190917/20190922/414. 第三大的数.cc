/*
 * Description: 第三大的数
 * Author: AskeyNil
 * CreateDate: 2019-09-22 18:49:06
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
#include <set>
#include <string>
#include <vector>
using namespace std;

// 借助 set 去重复
//! 效率太低
// class Solution {
// public:
//   int thirdMax(vector<int> &nums) {
//     set<int> s(nums.begin(), nums.end());
//     nums.assign(s.begin(), s.end());
//     sort(nums.begin(), nums.end());
//     if (nums.size() >= 3) {
//       return nums[nums.size() - 3];
//     } else {
//       return nums[nums.size() - 1];
//     }
//   }
// };

// 有三个指针分别表示第一大,第二大,第三大
class Solution {
public:
  int thirdMax(vector<int> &nums) {
    int *max_number = nullptr;
    int *second_number = nullptr;
    int *third_number = nullptr;
    for (auto &num : nums) {
      if (max_number == nullptr) {
        max_number = &num;
      } else if (num == *max_number) {
        continue;
      } else if (num > *max_number) {
        third_number = second_number;
        second_number = max_number;
        max_number = &num;
      } else if (second_number == nullptr) {
        second_number = &num;
      } else if (num == *second_number) {
        continue;
      } else if (num > *second_number) {
        third_number = second_number;
        second_number = &num;
      } else if (third_number == nullptr) {
        third_number = &num;
      } else if (num > *third_number) {
        third_number = &num;
      }
    }
    return third_number != nullptr ? *third_number : *max_number;
  }
};

int main(int argc, char const *argv[]) {
  vector<int> v{9998, 9991, 9991, 9989, 9986, 9985};
  cout << Solution().thirdMax(v) << endl;
  return 0;
}
