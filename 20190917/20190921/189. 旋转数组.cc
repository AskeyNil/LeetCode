/*
 * Description: 旋转数组
 * Author: AskeyNil
 * CreateDate: 2019-09-21 21:43:34
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

// 插入法
// class Solution {
//    public:
//     void rotate(vector<int>& nums, int k) {
//         k %= nums.size();
//         for (int i = 0; i < k; i++) {
//             int temp = nums[nums.size() - 1];
//             nums.pop_back();
//             nums.insert(nums.begin(), temp);
//         }
//     }
// };

// 三次翻转
class Solution {
   public:
    void rotate(vector<int>& nums, int k) {
        k %= nums.size();
        // 全部翻转
        reverse(nums.begin(), nums.end());
        // 翻转前 k 个
        reverse(nums.begin(), nums.begin() + k);
        // 翻转剩余的
        reverse(nums.begin() + k, nums.end());
    }
};