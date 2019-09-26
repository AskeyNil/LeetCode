/*
 * Description: 公平的糖果交换
 * Author: AskeyNil
 * CreateDate: 2019-09-26 08:46:07
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

/*
class Solution:
    def fairCandySwap(self, A: [int], B: [int]) -> [int]:
        sum_A = sum(A)
        sum_B = sum(B)
        A.sort()
        B.sort()
        diff = sum_A - sum_B
        index = 0
        for num in A:
            temp = A - diff
            while True:
                if temp > B[index]:
                    index += 1
                    continue
                elif temp == B[index]:
                    return [num, temp]
                else:
                    break
        return [0, 0]
*/

#include <iostream>
#include <numeric>
#include <vector>

using namespace std;

class Solution {
  public:
    vector<int> fairCandySwap(vector<int> &A, vector<int> &B) {
        int sum_a = accumulate(A.begin(), A.end(), 0);
        int sum_b = accumulate(B.begin(), B.end(), 0);
        sort(A.begin(), A.end());
        sort(B.begin(), B.end());
        int diff = sum_a - sum_b;
        int index = 0;
        for (auto num : A) {
            int temp = num - diff / 2;
            while (true) {
                if (temp > B[index]) {
                    index += 1;
                    continue;
                } else if (temp == B[index])
                    return {num, temp};
                else
                    break;
            }
        }
        throw "";
    }
};

int main(int argc, char const *argv[]) {
    /* code */
    return 0;
}
