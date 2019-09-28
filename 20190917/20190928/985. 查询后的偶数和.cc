/*
 * Description: 查询后的偶数和
 * Author: AskeyNil
 * CreateDate: 2019-09-28 14:00:54
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
    vector<int> sumEvenAfterQueries(vector<int> &A,
                                    vector<vector<int>> &queries) {
        int sum = 0;
        for (auto num : A) {
            if (num % 2 == 0)
                sum += num;
        }
        vector<int> v;
        for (auto q : queries) {
            int val = q[0], index = q[1];
            if (A[index] % 2 == 0)
                sum -= A[index];
            A[index] += val;
            if (A[index] % 2 == 0)
                sum += A[index];
            v.push_back(sum);
        }
        return v;
    }
};