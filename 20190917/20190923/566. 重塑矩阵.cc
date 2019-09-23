/*
 * Description: 重塑矩阵
 * Author: AskeyNil
 * CreateDate: 2019-09-23 09:53:54
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
    vector<vector<int>> matrixReshape(vector<vector<int>> &nums, int r, int c) {
        int current_r = nums.size();
        if (current_r == 0)
            return nums;
        int current_c = nums[0].size();
        if (current_c == 0)
            return nums;
        if (current_c * current_r != r * c)
            return nums;
        vector<vector<int>> vv;
        for (size_t i = 0; i < r; i++) {
            vector<int> v;
            for (size_t j = 0; j < c; j++) {
                v.push_back(
                    nums[((i * c) + j) / current_c][((i * c) + j) % current_c]);
            }
            vv.push_back(v);
        }
        return vv;
    }
};

int main(int argc, char const *argv[]) {
    /* code */
    return 0;
}
