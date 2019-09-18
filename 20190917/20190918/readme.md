# 最大子序和
## [题目](https://leetcode-cn.com/problems/maximum-subarray/)

给定一个整数数组 `nums` ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。

**示例**:

> **输入**: [-2,1,-3,4,-1,2,1,-5,4],
>
> **输出**: 6
>
> **解释**: 连续子数组 [4,-1,2,1] 的和最大，为 6。

**进阶**:

如果你已经实现复杂度为 O(n) 的解法，尝试使用更为精妙的分治法求解。

## [Python](./53.%20最大子序和.py)
### 动态规划
``` python
class Solution:
    def maxSubArray(self, nums: [int]) -> int:
        length = len(nums)
        if length == 0:
            return 0
        max_num = nums[0]
        left_max = nums[0]
        for num in nums[1:]:
            if left_max + num < num:
                left_max = num
            else:
                left_max += num
            if left_max > max_num:
                max_num = left_max
        return max_num
```
### 分治法

## [C++](./53.%20最大子序和.cc)
### 动态规划
``` c++
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
```