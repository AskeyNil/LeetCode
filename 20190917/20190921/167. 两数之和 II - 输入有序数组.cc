/*
 * Description: 两数之和 II - 输入有序数组
 * Author: AskeyNil
 * CreateDate: 2019-09-21 20:13:26
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
    vector<int> twoSum(vector<int>& numbers, int target) {
        int pre = 0, tail = numbers.size() - 1;
        while (pre < tail) {
            if (numbers[pre] + numbers[tail] == target) {
                return {pre + 1, tail + 1};
            } else if (numbers[pre] + numbers[tail] > target) {
                tail -= 1;
            } else {
                pre += 1;
            }
        }
        return {};
    }
};

int main(int argc, char const* argv[]) {
    vector<int> numbers{5, 25, 75};
    Solution().twoSum(numbers, 100);
    return 0;
}
