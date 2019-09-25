/*
 * Description: 托普利茨矩阵
 * Author: AskeyNil
 * CreateDate: 2019-09-25 08:20:31
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
    bool isToeplitzMatrix(vector<vector<int>> &matrix) {
        int v = matrix.size(), h = matrix[0].size();
        for (int i = 1; i < v; i++) {
            for (int j = 1; j < h; j++) {
                if (matrix[i][j] != matrix[i - 1][j - 1])
                    return false;
            }
        }
        return true;
    }
};