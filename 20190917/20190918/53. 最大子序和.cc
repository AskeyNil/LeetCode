/*
 * Description: 最大子序和
 * Author: AskeyNil
 * CreateDate: 2019-09-18 08:09:48
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
    int maxSubArray(vector<int>& nums) {
        if (nums.empty()) return 0;
        int left_max = nums[0];
        int max_sum = nums[0];
        for (auto i = nums.begin() + 1; i < nums.end(); i++) {
            if (left_max + *i < *i) {
                left_max = *i;
            } else {
                left_max += *i;
            }
            if (max_sum < left_max) max_sum = left_max;
        }
        return max_sum;
    }
};

int main(int argc, const char** argv) {
    vector<int> nums{-2, 1, -3, 4, -1, 2, 1, -5, 4};
    std::cout << Solution().maxSubArray(nums) << std::endl;
    return 0;
}
