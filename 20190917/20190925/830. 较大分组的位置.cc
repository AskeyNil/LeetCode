/*
 * Description: 较大分组的位置
 * Author: AskeyNil
 * CreateDate: 2019-09-25 08:56:00
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
    vector<vector<int>> largeGroupPositions(string S) {
        vector<vector<int>> vv;
        int leftIndex = 0;
        char left = S[0];
        for (int index = 1; index < S.size(); index++) {
            cout << left << endl;
            if (S[index] != left) {
                if (index - leftIndex >= 3)
                    vv.push_back({leftIndex, index - 1});
                leftIndex = index;
                left = S[index];
            }
        }
        if (S.size() - leftIndex >= 3)
            vv.push_back({leftIndex, int(S.size() - 1)});
        return vv;
    }
};

int main(int argc, char const *argv[]) {
    cout << Solution().largeGroupPositions("aaa")[0][1] << endl;
    return 0;
}
