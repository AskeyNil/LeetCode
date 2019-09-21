/*
 * Description: 买卖股票的最佳时机
 * Author: AskeyNil
 * CreateDate: 2019-09-21 09:06:06
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

// 从左往右推
class Solution {
   public:
    int maxProfit(vector<int>& prices) {
        int length = prices.size();
        if (length == 0 || length == 1) {
            return 0;
        }
        int diff = 0, mini = prices[0];
        for (int i = 0; i < length; i++) {
            int temp = prices[i] - mini;
            if (temp > diff)
                diff = temp;
            else if (temp < 0)
                mini = prices[i];
        }
        return diff;
    }
};