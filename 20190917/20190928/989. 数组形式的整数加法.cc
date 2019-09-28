/*
 * Description: 数组形式的整数加法
 * Author: AskeyNil
 * CreateDate: 2019-09-28 18:52:57
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
    vector<int> addToArrayForm(vector<int> &A, int K) {
        int carry = 0;
        for (int i = A.size() - 1; i >= 0; i--) {
            A[i] += K % 10 + carry;
            carry = 0;
            if (A[i] >= 10) {
                A[i] %= 10;
                carry = 1;
            }
            K /= 10;
        }
        while (K > 0) {
            A.insert(A.begin(), K % 10 + carry);
            carry = 0;
            if (A[0] >= 10) {
                A[0] %= 10;
                carry = 1;
            }
            K /= 10;
        }
        if (carry == 1)
            A.insert(A.begin(), 1);
        return A;
    }
};