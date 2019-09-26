/*
 * Description: 转置矩阵
 * Author: AskeyNil
 * CreateDate: 2019-09-26 08:11:15
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
    vector<vector<int>> transpose(vector<vector<int>> &A) {
        vector<vector<int>> vv;
        int line_count = A.size(), column_count = A[0].size();
        for (int i = 0; i < column_count; i++) {
            vector<int> v;
            for (int j = 0; j < line_count; j++) {
                v.push_back(A[j][i]);
            }
            vv.push_back(v);
        }
        return vv;
    }
};