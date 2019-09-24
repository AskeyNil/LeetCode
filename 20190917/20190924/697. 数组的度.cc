/*
 * Description: 数组的度
 * Author: AskeyNil
 * CreateDate: 2019-09-24 09:38:15
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

class Solution {
  public:
    int findShortestSubArray(vector<int> &nums) {
        if (nums.empty())
            return 0;
        map<int, vector<int>> dic;
        for (int i = 0; i < nums.size(); i++) {
            if (dic.count(nums[i]) == 0)
                dic[nums[i]] = vector<int>{1, i, i};
            else
                dic[nums[i]][0] += 1, dic[nums[i]][2] = i;
        }

        int re_count = 0, *max_number = nullptr;
        for (auto v : dic) {
            if (max_number == nullptr) {
                max_number = new int(v.second[0]);
                re_count = v.second[2] - v.second[1] + 1;
            } else {
                if (v.second[0] > *max_number) {
                    *max_number = v.second[0];
                    re_count = v.second[2] - v.second[1] + 1;
                } else if (v.second[0] == *max_number) {
                    int count = v.second[2] - v.second[1] + 1;
                    if (count < re_count) {
                        re_count = count;
                    }
                }
            }
        }
        return re_count;
    }
};