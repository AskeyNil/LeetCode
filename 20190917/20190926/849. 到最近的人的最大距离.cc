/*
 * Description: 到最近的人的最大距离
 * Author: AskeyNil
 * CreateDate: 2019-09-26 07:35:07
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
    int maxDistToClosest(vector<int> &seats) {
        vector<int> v{-1};
        for (int i = 0; i < seats.size(); i++) {
            if (seats[i] == 1)
                v.push_back(i);
        }
        v.push_back(seats.size());
        int max_index = 0, length = v.size();
        for (int i = 0; i < length - 1; i++) {
            int temp_index = (v[i + 1] - v[i]) / 2;
            if (i == 0 || i == length - 2)
                temp_index = v[i + 1] - v[i] - 1;
            if (temp_index > max_index)
                max_index = temp_index;
        }
        return max_index;
    }
};