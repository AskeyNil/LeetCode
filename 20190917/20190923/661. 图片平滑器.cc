/*
 * Description: 图片平滑器
 * Author: AskeyNil
 * CreateDate: 2019-09-23 14:22:17
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
    vector<vector<int>> imageSmoother(vector<vector<int>> &M) {
        int m_h = M.size(), m_v = M[0].size();
        int direction[9][2] = {{-1, -1}, {0, -1}, {1, -1}, {-1, 0}, {0, 0},
                               {1, 0},   {-1, 1}, {0, 1},  {1, 1}};
        vector<vector<int>> vv;
        for (size_t i = 0; i < m_h; i++) {
            vector<int> v;
            for (size_t j = 0; j < m_v; j++) {
                int sum = 0, count = 0;
                for (auto index : direction) {
                    int h1 = i + index[0], v1 = j + index[1];
                    if (h1 < 0 or h1 >= m_h or v1 < 0 or v1 >= m_v)
                        continue;
                    sum += M[h1][v1];
                    count += 1;
                }
                v.push_back(sum / count);
            }
            vv.push_back(v);
        }
        return vv;
    }
};