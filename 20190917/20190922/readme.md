# 268.缺失数字

## [题目](https://leetcode-cn.com/problems/missing-number/)

给定一个包含 `0, 1, 2, ..., n` 中 n 个数的序列，找出 0 .. n 中没有出现在序列中的那个数。

**示例** 1:

> **输入**: [3,0,1]
>
> **输出**: 2

**示例** 2:

> **输入**: [9,6,4,2,3,5,7,0,1]
>
> **输出**: 8

**说明**:

你的算法应具有线性时间复杂度。你能否仅使用额外常数空间来实现?

## [Python](./268.%20缺失数字.py)

### 排序法

```python
class Solution:
    def missingNumber(self, nums: [int]) -> int:
        nums.sort()
        for index, num in enumerate(nums):
            if index != num:
                return index
        return len(nums)
```

### 求和法

```python
class Solution:
    def missingNumber(self, nums: [int]) -> int:
        sum_number = sum(nums)
        length = len(nums)
        sum_number1 = (length + 1) * length // 2
        return sum_number1 - sum_number
```



## [C++](./268.%20缺失数字.cc)

### 排序法

```c++
class Solution {
   public:
    int missingNumber(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        for (auto i = 0; i < nums.size(); i++) {
            if (nums[i] != i) {
                return i;
            }
        }
        return nums.size();
    }
};
```

### 位运算

```C++
class Solution {
   public:
    int missingNumber(vector<int>& nums) {
        int number = nums.size();
        for (int i = 0; i < nums.size(); i++) {
            number ^= i ^ nums[i];
        }
        return number;
    }
};
```

## 总结

### 求和法

按照数学公式（高斯求和公式），$\sum_{i=0}^{n}i=\frac{n(n+1)}{2}$ 计算出 n 的总长度，然后减去数组中各元素的值，即可得到缺失的值

### 位运算

根据异或的特性，结合率，0 与任何数异或都是任何数，两次与同一个数异或变回本身。可以计算出缺失值，与求和法类似。



# 283. 移动零

## [题目](https://leetcode-cn.com/problems/move-zeroes/)

给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。

**示例**:

> 输入: `[0,1,0,3,12]`
>
> 输出: `[1,3,12,0,0]`

**说明**:

1. 必须在原数组上操作，不能拷贝额外的数组。

2. 尽量减少操作次数。

## [Python](./283.%20移动零.py)

```python
class Solution:
    def moveZeroes(self, nums: [int]):
        left = 0
        right = 0
        length = len(nums)
        while right < length:
            if nums[right] != 0:
                nums[left] = nums[right]
                left += 1
            right += 1
        nums[left:right] = [0 for _ in range(right - left)]

```



## [C++](./283.%20移动零.cc)

### 双指针

```c++
class Solution {
public:
  void moveZeroes(vector<int> &nums) {
    int left = 0, right = 0, count = nums.size();
    while (left < count) {
      if (right < count) {
        if (nums[right] != 0) {
          nums[left++] = nums[right];
        }
        right += 1;
      } else {
        nums[left++] = 0;
      }
    }
  }
};
```

