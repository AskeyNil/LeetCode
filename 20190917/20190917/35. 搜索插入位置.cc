/*
 * Description: 搜索插入位置
 * Author: AskeyNil
 * CreateDate: 2019-09-17 21:59:43
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
    int searchInsert(vector<int> &nums, int target) {
        int length = nums.size();
        if (length == 0) return 0;
        int left = 0, right = length;
        while (left < right) {
            int mid = left + (right - left) / 2;
            if (nums[mid] < target) {
                left = mid + 1;
            } else {
                right = mid;
            }
        }
        return left;
    }
};

int main(int argc, char const *argv[]) {
    vector<int> a{1, 3, 5, 6};
    std::cout << Solution().searchInsert(a, 0) << std::endl;
    return 0;
}
