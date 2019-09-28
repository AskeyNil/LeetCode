/*
 * Description: 有效的山脉数组
 * Author: AskeyNil
 * CreateDate: 2019-09-28 08:02:12
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
    bool validMountainArray(vector<int> &A) {
        if (A.size() < 3)
            return false;
        bool is_down = false;
        int left = A[0];
        for (int i = 1; i < A.size(); i++) {
            if (is_down) {
                if (left <= A[i]) {
                    return false;
                }
            } else {
                if (left > A[i]) {
                    if (i < 2) {
                        return false;
                    }
                    is_down = true;
                } else if (left == A[i]) {
                    return false;
                } else {
                    if (i == A.size() - 1) {
                        return false;
                    }
                }
            }
            left = A[i];
        }
        return true;
    }
};