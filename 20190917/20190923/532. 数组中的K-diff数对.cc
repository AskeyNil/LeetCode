/*
 * Description: 数组中的K-diff数对
 * Author: AskeyNil
 * CreateDate: 2019-09-23 08:22:29
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

/* class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        nums.sort()
        dic = {}
        left = None
        count = 0
        for num in nums:
            if left != None and left != num and (num - k) in dic:
                count += 1
            left = num
            if num in dic:
                dic[num] += 1
                if k == 0 and dic[num] == 2:
                    count += 1
            else:
                dic[num] = 1
        return count
 */

// 一次哈希表
class Solution {
  public:
    int findPairs(vector<int> &nums, int k) {
        map<int, int> dic;
        int count = 0, *left = nullptr;
        sort(nums.begin(), nums.end());
        for (auto &num : nums) {
            if (left != nullptr && *left != num && dic.count((num - k)) > 0) {
                count += 1;
            }
            left = &num;
            if (dic.count(num) > 0) {
                dic[num] += 1;
                if (k == 0 && dic[num] == 2) {
                    count += 1;
                }
            } else {
                dic[num] = 1;
            }
        }
        return count;
    }
};