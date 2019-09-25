/*
 * Description: 翻转图像
 * Author: AskeyNil
 * CreateDate: 2019-09-25 09:25:40
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

// 交换法
class Solution {
  public:
    vector<vector<int>> flipAndInvertImage(vector<vector<int>> &A) {
        int size = A.size();
        for (auto &v : A) {
            for (size_t i = 0; i < (size + 1) / 2; i++) {
                if (v[i] == v[size - i - 1]) {
                    v[i] = 1 ^ v[i];
                    v[size - i - 1] = v[i];
                }
            }
        }
        return A;
    }
};
