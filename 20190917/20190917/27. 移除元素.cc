/*
 * Description: 移除元素
 * Author: AskeyNil
 * CreateDate: 2019-09-17 20:21:21
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
using std::vector;

class Solution {
   public:
    int removeElement(vector<int> &nums, int val) {
        auto j = 0;
        for (auto i = 0; i < nums.size(); i++) {
            if (nums[i] != val) {
                nums[j] = nums[i];
                j++;
            }
        }
        return j;
    }
};

int main(int argc, char const *argv[]) {
    vector<int> nums{0, 1, 2, 2, 3, 0, 4, 2};
    std::cout << Solution().removeElement(nums, 2) << std::endl;
    for (auto i : nums) {
        std::cout << i << std::endl;
    }
    return 0;
}
