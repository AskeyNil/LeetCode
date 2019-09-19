# 88. 合并两个有序数组
## [题目](https://leetcode-cn.com/problems/merge-sorted-array/)
给定两个有序整数数组 nums1 和 nums2，将 nums2 合并到 nums1 中，使得 num1 成为一个有序数组。

**说明**:

- 初始化 nums1 和 nums2 的元素数量分别为 m 和 n。
- 你可以假设 nums1 有足够的空间（空间大小大于或等于 m + n）来保存 nums2 中的元素。

**示例**:

> 输入:
>
> nums1 = [1,2,3,0,0,0], m = 3
>
> nums2 = [2,5,6],       n = 3
>
>
> 输出: [1,2,2,3,5,6]


## Python
### 暴力合并排序法
``` python
class Solution:
    def merge(self, nums1: [int], m: int, nums2: [int], n: int) -> None:
        nums1[:] = sorted(nums1[:m] + nums2)
```

1. 双指针法(用 C++ 实现)
2. Python 实现参考[官方题解](https://leetcode-cn.com/problems/merge-sorted-array/solution/he-bing-liang-ge-you-xu-shu-zu-by-leetcode/)

## C++
### 双指针法(从前往后)
``` C++
class Solution {
   public:
    void merge(vector<int>& nums1, int m, vector<int>& nums2, int n) {
        if (n == 0) return;
        vector<int> nums1_copy = nums1;
        int index1 = 0, index2 = 0;
        for (auto& number : nums1) {
            std::cout << nums1_copy[index1] << std::endl;
            if (index2 == n ||
                index1 != m && nums1_copy[index1] < nums2[index2]) {
                number = nums1_copy[index1];
                index1 += 1;
            } else {
                number = nums2[index2];
                index2 += 1;
            }
        }
    }
};
```
> 时间复杂度o(m+n) 空间复杂度o(m+n)
### 双指针法(从后往前)
``` C++
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
```
> 时间复杂度o(m+n) 空间复杂度o(1)
