/*
 * Description: 存在重复元素
 * Author: AskeyNil
 * CreateDate: 2019-09-21 22:21:14
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
#include <map>
#include <vector>

using namespace std;

// 哈希表
// class Solution {
//    public:
//     bool containsDuplicate(vector<int>& nums) {
//         map<int, int> dic;
//         for (int num : nums) {
//             if (dic.count(num) == 0)
//                 dic[num] = 0;
//             else
//                 return true;
//         }
//         return false;
//     }
// };

// 排序法
class Solution {
   public:
    bool containsDuplicate(vector<int>& nums) {
        if (nums.empty()) return false;
        sort(nums.begin(), nums.end());
        for (auto i = 0; i < nums.size() - 1; i++) {
            if (nums[i] == nums[i + 1]) return true;
        }
        return false;
    }
};