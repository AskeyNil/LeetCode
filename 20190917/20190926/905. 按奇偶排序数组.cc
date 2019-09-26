/*
 * Description: 按奇偶排序数组
 * Author: AskeyNil
 * CreateDate: 2019-09-26 09:48:38
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
    vector<int> sortArrayByParity(vector<int> &A) {
        int left = 0, right = A.size() - 1;
        while (left < right) {
            bool is_left = A[left] % 2 == 0;
            bool is_right = A[right] % 2 == 0;
            if (is_left && is_right) {
                left += 1;
            } else if (is_left && !is_right) {
                left += 1, right -= 1;
            } else if (!is_left && is_right) {
                A[left] = A[left] + A[right];
                A[right] = A[left] - A[right];
                A[left] = A[left] - A[right];
                left += 1, right -= 1;
            } else {
                right -= 1;
            }
        }
        return A;
    }
};