/*
 * Description: 有序数组的平方
 * Author: AskeyNil
 * CreateDate: 2019-09-28 08:31:06
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

#include <cmath>
#include <iostream>
#include <string>
#include <vector>

using namespace std;

// 双指针法
class Solution {
  public:
    vector<int> sortedSquares(vector<int> &A) {
        int left = 0, right = A.size() - 1;
        vector<int> B(A.size());
        for (int i = A.size() - 1; i >= 0; i--) {
            int leftValue = pow(A[left], 2), rightValue = pow(A[right], 2);
            if (leftValue < rightValue) {
                B[i] = rightValue;
                if (right != 0)
                    right -= 1;
            } else {
                B[i] = leftValue;
                if (left + 1 != A.size())
                    left += 1;
            }
        }
        return B;
    }
};