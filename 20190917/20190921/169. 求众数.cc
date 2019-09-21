/*
 * Description: 求众数
 * Author: AskeyNil
 * CreateDate: 2019-09-21 21:04:36
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

// Boyer-Moore 投票算法
// class Solution {
//    public:
//     int majorityElement(vector<int>& nums) {
//         int count = 0, candidate = nums[0];
//         for (auto num : nums) {
//             if (count == 0) candidate = num;
//             count += num == candidate ? 1 : -1;
//         }
//         return candidate;
//     }
// };

// 哈希表
class Solution {
   public:
    int majorityElement(vector<int>& nums) {
        map<int, int> dic;
        int length = nums.size();
        for (auto num : nums) {
            if (dic.count(num) == 0) {
                dic[num] = 1;
            } else {
                dic[num] += 1;
            }
            if (dic[num] > length / 2.0) return num;
        }
        return nums[0];
    }
};
