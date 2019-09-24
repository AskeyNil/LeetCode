/*
 * Description: 使用最小花费爬楼梯
 * Author: AskeyNil
 * CreateDate: 2019-09-24 12:05:55
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
    int minCostClimbingStairs(vector<int> &cost) {
        vector<int> dp{cost[0], cost[1]};
        for (int i = 2; i < cost.size(); i++) {
            dp.push_back(min(dp[i - 2], dp[i - 1]) + cost[i]);
        }
        return min(dp[dp.size() - 1], dp[dp.size() - 2]);
    }
};
