/*
 * Description: 添加一个描述!!!
 * Author: AskeyNil
 * CreateDate: 2019-09-26 09:18:49
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

/* class Solution:
    def isMonotonic(self, A: [int]) -> bool:
        length = len(A)
        if length < 3:
            return True
        left = 0
        for index in range(length - 1):
            if left == 0:
                if A[index + 1] - A[index] > 0:
                    left = 1
                elif A[index + 1] - A[index] < 0:
                    left = -1
            elif left == 1:
                if A[index + 1] - A[index] < 0:
                    return False
            else:
                if A[index + 1] - A[index] > 0:
                    return False
        return True
*/
#include <iostream>
#include <string>
#include <vector>

using namespace std;

class Solution {
  public:
    bool isMonotonic(vector<int> &A) {
        int length = A.size();
        if (length < 3)
            return true;
        int tag = 0;
        for (int index = 0; index < length - 1; index++) {
            int diff = A[index + 1] - A[index];
            if (tag == 0) {
                if (diff > 0)
                    tag = 1;
                else if (diff < 0)
                    tag = -1;
            } else if (tag == 1) {
                if (diff < 0)
                    return false;
            } else {
                if (diff > 0)
                    return false;
            }
        }
        return true;
    }
};