# 27. 移动元素
## [题目](https://leetcode-cn.com/problems/remove-element/)

给定一个数组 nums 和一个值 val，你需要原地移除所有数值等于 val 的元素，返回移除后数组的新长度。

不要使用额外的数组空间，你必须在**原地修改输入数组**并在使用 O(1) 额外空间的条件下完成。

元素的顺序可以改变。你不需要考虑数组中超出新长度后面的元素。

**示例 1**:

> 给定 nums = [3,2,2,3], val = 3,
>
> 函数应该返回新的长度 2, 并且 nums 中的前两个元素均为 2。
>
> 你不需要考虑数组中超出新长度后面的元素。

**示例 2**:

> 给定 nums = [0,1,2,2,3,0,4,2], val = 2,
>
> 函数应该返回新的长度 5, 并且 nums 中的前五个元素为 0, 1, 3, 0, 4。
>
> 注意这五个元素可为任意顺序。
>
>你不需要考虑数组中超出新长度后面的元素。

**说明**:

为什么返回数值是整数，但输出的答案是数组呢?

请注意，输入数组是以“引用”方式传递的，这意味着在函数里修改输入数组对于调用者是可见的。

你可以想象内部操作如下:
``` c++
// nums 是以“引用”方式传递的。也就是说，不对实参作任何拷贝
int len = removeElement(nums, val);

// 在函数里修改输入数组对于调用者是可见的。
// 根据你的函数返回的长度, 它会打印出数组中该长度范围内的所有元素。
for (int i = 0; i < len; i++) {
    print(nums[i]);
}
```

## [Python](./27.%20移除元素.py)
``` python
class Solution:
    def removeElement(self, nums: [int], val: int) -> int:
        i = 0
        for (index, num) in enumerate(nums):
            if nums[index] != val:
                nums[i] = nums[index]
                i += 1
        return i
```

## [C++](./27.%20移除元素.cc)
``` c++
class Solution
{
public:
    int removeElement(vector<int> &nums, int val)
    {
        auto j = 0;
        for (auto i = 0; i < nums.size(); i++)
        {
            if (nums[i] != val)
            {
                nums[j] = nums[i];
                j++;
            }
        }
        return j;
    }
};
```

# 35. 搜索插入位置
# [题目](https://leetcode-cn.com/problems/search-insert-position/)
给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。

你可以假设数组中无重复元素。

示例 1:

> 输入: [1,3,5,6], 5
>
> 输出: 2

示例 2:

> 输入: [1,3,5,6], 2
>
> 输出: 1

示例 3:

>输入: [1,3,5,6], 7
>
> 输出: 4

示例 4:

>输入: [1,3,5,6], 0
>输出: 0

## [Python](./35.%20搜索插入位置.py)

### 暴力解决
``` python
class Solution:
    def searchInsert(self, nums: [int], target: int) -> int:
        for index, num in enumerate(nums):
            if num >= target:
                return index
        return len(nums)
```

### 二分查找法
``` python
class Solution:
    def searchInsert(self, nums: [int], target: int) -> int:
        length = len(nums)
        if length == 0:
            return 0
        left = 0
        right = length
        while left < right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid
        return left
```

## C++

### 二分查找法
``` c++
class Solution
{
public:
    int searchInsert(vector<int> &nums, int target)
    {
        int length = nums.size();
        if (length == 0)
            return 0;
        int left = 0, right = length;
        while (left < right)
        {
            int mid = left + (right - left) / 2;
            if (nums[mid] < target)
            {
                left = mid + 1;
            }
            else
            {
                right = mid;
            }
        }
        return left;
    }
};
```

## 算法总结
二分法学习来源:[十分好用的二分查找法模板](https://leetcode-cn.com/problems/search-insert-position/solution/te-bie-hao-yong-de-er-fen-cha-fa-fa-mo-ban-python-/)
### 二分法取中位数索引的问题
1. `(left + right) / 2`

> 如果 left 和 right 很大，相加可能就会出现溢出的情况，即索引就取不到准确的值

2. `left + (right - left) / 2`

> 如果 left 是负数，right 很大，也可能出现溢出的情况，但是在数组查找中，left 为正数，right 为正数，所以也就不存在这种情况。

3. `(left + right) >>> 1`

> 这行代码是 `Java` 的写法，代表的是相加然后右移一位，在位运算中，右移一位相当于是除以 2，左移一位相当于是乘以 2。`>>>`代表无符号右移，在 C 中没有这种运算符，需要将数字转化为无符号类型然后使用`>>`即可。

但是在二分查找中，不会出现负数的情况，使用第二种方式其实可以满足情况

