/*
 * Description: 买卖股票的最佳时机 II
 * Author: AskeyNil
 * CreateDate: 2019-09-21 19:48:59
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
    int maxProfit(vector<int>& prices) {
        int length = prices.size();
        if (length <= 1) return 0;
        int sum = 0, left = prices[0];
        for (auto i = 1; i < length; i++) {
            if (prices[i] > left) sum += prices[i] - left;
            left = prices[i];
        }
        return sum;
    }
};
