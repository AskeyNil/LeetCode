/*
 * Description: 缺失数字
 * Author: AskeyNil
 * CreateDate: 2019-09-22 07:44:01
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

// 排序法
// class Solution {
//    public:
//     int missingNumber(vector<int>& nums) {
//         sort(nums.begin(), nums.end());
//         for (auto i = 0; i < nums.size(); i++) {
//             if (nums[i] != i) {
//                 return i;
//             }
//         }
//         return nums.size();
//     }
// };

// 位运算
class Solution {
   public:
    int missingNumber(vector<int>& nums) {
        int number = nums.size();
        for (int i = 0; i < nums.size(); i++) {
            number ^= i ^ nums[i];
        }
        return number;
    }
};