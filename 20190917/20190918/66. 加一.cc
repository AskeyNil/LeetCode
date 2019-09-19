/*
 * Description: 添加一个描述!!!
 * Author: AskeyNil
 * CreateDate: 2019-09-18 22:11:16
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
    vector<int> plusOne(vector<int>& digits) {
        int sum = 0;
        for (auto i = digits.end() - 1; i > digits.begin() - 1; i--) {
            sum = *i + 1;
            if (sum < 10) {
                *i = sum;
                break;
            } else {
                *i = 0;
            }
            if (i == digits.begin()) {
                digits.insert(digits.begin(), 1);
            }
        }
        return digits;
    }
};

int main(int argc, char const* argv[]) {
    vector<int> v{9, 9, 9, 9};
    auto v1 = Solution().plusOne(v);
    for (auto i : v1) {
        std::cout << i << std::endl;
    }
    return 0;
}
