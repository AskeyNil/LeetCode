/*
 * Description: 杨辉三角
 * Author: AskeyNil
 * CreateDate: 2019-09-20 08:04:44
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
    vector<vector<int>> generate(int numRows) {
        if (numRows == 0) {
            vector<vector<int>> vv;
            return vv;
        } else {
            vector<vector<int>> vv = this->generate(numRows - 1);
            vv.push_back(vector<int>());
            if (numRows != 1) {
                int left = 0;
                for (auto num : vv[numRows - 2]) {
                    vv[numRows - 1].push_back(left + num);
                    left = num;
                }
            }
            vv[numRows - 1].push_back(1);
            return vv;
        }
    }
};