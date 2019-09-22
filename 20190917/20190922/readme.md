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



# 414. 第三大的数

## [题目](https://leetcode-cn.com/problems/third-maximum-number/)

给定一个非空数组，返回此数组中第三大的数。如果不存在，则返回数组中最大的数。要求算法时间复杂度必须是O(n)。

**示例** 1:

> **输入**: [3, 2, 1]
>
> **输出**: 1
>
> **解释**: 第三大的数是 1.

**示例** 2:

> **输入**: [1, 2]
>
> **输出**: 2
>
> **解释**: 第三大的数不存在, 所以返回最大的数 2 .

**示例** 3:

> **输入**: [2, 2, 3, 1]
>
> **输出**: 1
>
> **解释**: 注意，要求返回第三大的数，是指第三大且唯一出现的数。
>
> 存在两个值为2的数，它们都排第二。

## [Python](./414.%20第三大的数.py)

```python
class Solution:
    def thirdMax(self, nums: [int]) -> int:
        nums = list(set(nums))
        nums.sort()
        if len(nums) >= 3:
            return nums[-3]
        else:
            return nums[-1]
```

## [C++](./414.%20第三大的数.cc)

```c++
// 有三个指针分别表示第一大,第二大,第三大
class Solution {
public:
  int thirdMax(vector<int> &nums) {
    int *max_number = nullptr;
    int *second_number = nullptr;
    int *third_number = nullptr;
    for (auto &num : nums) {
      if (max_number == nullptr) {
        max_number = &num;
      } else if (num == *max_number) {
        continue;
      } else if (num > *max_number) {
        third_number = second_number;
        second_number = max_number;
        max_number = &num;
      } else if (second_number == nullptr) {
        second_number = &num;
      } else if (num == *second_number) {
        continue;
      } else if (num > *second_number) {
        third_number = second_number;
        second_number = &num;
      } else if (third_number == nullptr) {
        third_number = &num;
      } else if (num > *third_number) {
        third_number = &num;
      }
    }
    return third_number != nullptr ? *third_number : *max_number;
  }
};
```



# 448. 找到所有数组中消失的数字

## [题目](https://leetcode-cn.com/problems/find-all-numbers-disappeared-in-an-array/)

给定一个范围在  1 ≤ a[i] ≤ n ( n = 数组大小 ) 的 整型数组，数组中的元素一些出现了两次，另一些只出现一次。

找到所有在 [1, n] 范围之间没有出现在数组中的数字。

您能在不使用额外空间且时间复杂度为O(n)的情况下完成这个任务吗? 你可以假定返回的数组不算在额外空间内。

**示例**:

> **输入**:
>
> [4,3,2,7,8,2,3,1]
>
> **输出**:
>
> [5,6]



## [Python](./448.%20找到所有数组中消失的数字.py)

```python
class Solution:
    def findDisappearedNumbers(self, nums: [int]) -> [int]:
        rel = []
        count = len(nums)
        for index, num in enumerate(nums):
            nums[(num - 1) % count] += count
        for index, num in enumerate(nums):
            if num <= count:
                rel.append(index+1)

```



## [C++](./448.%20找到所有数组中消失的数字.cc)

```c++
class Solution {
public:
  vector<int> findDisappearedNumbers(vector<int> &nums) {
    vector<int> v;
    for (auto num : nums) {
      nums[(num - 1) % nums.size()] += nums.size();
    }
    for (size_t i = 0; i < nums.size(); i++) {
      if (nums[i] <= nums.size()) {
        v.push_back(i + 1);
      }
    }
    return v;
  }
};
```

## 总结

该题采用两次遍历

1. 第一次给所有数据应该出现在的位子做一个特定的标记
2. 第二次遍历到查找没有标记的位子，该位置就是就是消失的数字