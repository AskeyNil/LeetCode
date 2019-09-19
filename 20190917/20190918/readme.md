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

# 加一
## [题目](https://leetcode-cn.com/problems/plus-one/)
给定一个由整数组成的非空数组所表示的非负整数，在该数的基础上加一。

最高位数字存放在数组的首位， 数组中每个元素只存储单个数字。

你可以假设除了整数 0 之外，这个整数不会以零开头。

示例 1:

> 输入: [1,2,3]
>
> 输出: [1,2,4]
>
> 解释: 输入数组表示数字 123。

示例 2:

> 输入: [4,3,2,1]
>
> 输出: [4,3,2,2]
>
> 解释: 输入数组表示数字 4321。


## [Python](./66.%20加一.py)
``` python
class Solution:
    def plusOne(self, digits: [int]) -> [int]:
        length = len(digits) - 1
        for index in range(length, -1, -1):
            sum = digits[index] + 1
            if sum < 10:
                digits[index] = sum
                break
            else:
                digits[index] = 0
            if index == 0:
                digits.insert(0, 1)
        return digits
```

## [C++](./66.%20加一.cc)
``` c++
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

```