/*
 * Description: 最大连续1的个数
 * Author: AskeyNil
 * CreateDate: 2019-09-22 20:20:14
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
  int findMaxConsecutiveOnes(vector<int> &nums) {
    int max = 0, current = 0;
    for (int num : nums) {
      if (num) {
        current += 1;
      } else {
        if (current > max)
          max = current;
        current = 0;
      }
    }
    return max > current ? max : current;
  }
};