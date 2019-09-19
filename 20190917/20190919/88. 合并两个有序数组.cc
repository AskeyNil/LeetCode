/*
 * Description: 合并两个有序数组
 * Author: AskeyNil
 * CreateDate: 2019-09-19 21:42:51
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

// 双指针法 从左往右
// class Solution {
//    public:
//     void merge(vector<int>& nums1, int m, vector<int>& nums2, int n) {
//         if (n == 0) return;
//         vector<int> nums1_copy = nums1;
//         int index1 = 0, index2 = 0;
//         for (auto& number : nums1) {
//             std::cout << nums1_copy[index1] << std::endl;
//             if (index2 == n ||
//                 index1 != m && nums1_copy[index1] < nums2[index2]) {
//                 number = nums1_copy[index1];
//                 index1 += 1;
//             } else {
//                 number = nums2[index2];
//                 index2 += 1;
//             }
//         }
//     }
// };

//  双指针法 从右往左
class Solution {
   public:
    void merge(vector<int>& nums1, int m, vector<int>& nums2, int n) {
        if (n == 0) return;
        int index1 = m - 1, index2 = n - 1;
        for (int index = m + n - 1; index >= 0; index--) {
            if (index1 == -1 || index2 != -1 && nums1[index1] < nums2[index2]) {
                nums1[index] = nums2[index1];
                index1 -= 1;
            } else {
                nums1[index] = nums1[index2];
                index2 -= 1;
            }
        }
    }
};
int main(int argc, char const* argv[]) { return 0; }
