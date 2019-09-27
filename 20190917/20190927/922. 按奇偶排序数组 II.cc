/*
 * Description: 按奇偶排序数组 II
 * Author: AskeyNil
 * CreateDate: 2019-09-27 18:19:10
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

/*
# # 沙雕思路
# class Solution:
#     def sortArrayByParityII(self, A: [int]) -> [int]:
#         left = []
#         for index, num in enumerate(A):
#             if (num - index) % 2 != 0:
#                 if not left:
#                     left.append(index)
#                 else:
#                     if (num - A[left[-1]]) % 2 == 0:
#                         left.append(index)
#                     else:
#                         A[index], A[left[-1]] = A[left[-1]], A[index]
#                         left.pop()
#         return A
*/

class Solution {
  public:
    vector<int> sortArrayByParityII(vector<int> &A) {
        vector<int> v;
        for (int i = 0; i < A.size(); i++) {
            if ((A[i] - i) % 2 != 0) {
                if (v.size() == 0) {
                    v.push_back(i);
                } else {
                    if ((A[i] - A[v[0]]) % 2 == 0) {
                        v.push_back(i);
                    } else {
                        cout << A[i] << " " << A[v[0]] << endl;
                        A[i] = A[i] + A[v[0]];
                        A[v[0]] = A[i] - A[v[0]];
                        A[i] = A[i] - A[v[0]];
                        cout << A[i] << " " << A[v[0]] << endl;
                        cout << endl;
                        v.erase(v.begin());
                    }
                }
            }
        }
        return A;
    }
};
