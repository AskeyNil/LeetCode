# 674. 最长连续递增序列

## [题目](https://leetcode-cn.com/problems/longest-continuous-increasing-subsequence/)

给定一个未经排序的整数数组，找到最长且连续的的递增序列。

示例 1:

> 输入: [1,3,5,4,7]
>
> 输出: 3
>
> 解释: 最长连续递增序列是 [1,3,5], 长度为3。
>
> 尽管 [1,3,5,7] 也是升序的子序列, 但它不是连续的，因为5和7在原数组里被4隔开。 

示例 2:

> 输入: [2,2,2,2,2]
>
> 输出: 1
>
> 解释: 最长连续递增序列是 [2], 长度为1。

**注意**：数组长度不会超过10000。



## [Python](./674.%20最长连续递增序列.py)

```python
class Solution:
    def findLengthOfLCIS(self, nums: [int]) -> int:
        if len(nums) == 0:
            return 0
        max_count = 0
        count = 1
        left = None
        for num in nums:
            if left != None:
                if num > left:
                    count += 1
                else:
                    if max_count < count:
                        max_count = count
                    count = 1
            left = num
        return max(max_count, count)
```



## [C++](./674.%20最长连续递增序列.cc)

```c++
class Solution {
  public:
    int findLengthOfLCIS(vector<int> &nums) {
        if (nums.empty())
            return 0;
        int max_count = 0, count = 1, *left = nullptr;
        for (int &num : nums) {
            if (left != nullptr) {
                if (num > *left)
                    count += 1;
                else {
                    if (max_count < count)
                        max_count = count;
                    count = 1;
                }
            }
            left = &num;
        }
        return max_count > count ? max_count : count;
    }
};
```

# 697. 数组的度

## [题目](https://leetcode-cn.com/problems/degree-of-an-array/)

## [Python](./697.%20数组的度.py)

```python
class Solution:
    def findShortestSubArray(self, nums: [int]) -> int:
        if len(nums) == 0:
            return 0
        dic = {}
        for index, num in enumerate(nums):
            if num in dic:
                dic[num][0] += 1
                dic[num][2] = index
            else:
                dic[num] = [1, index, index]
        re_count = 0
        max_number = None
        for number, start, end in dic.values():
            if max_number == None:
                max_number = number
                re_count = end - start + 1
            else:
                if number > max_number:
                    max_number = number
                    re_count = end - start + 1
                if number == max_number:
                    count = end - start + 1
                    if count < re_count:
                        re_count = count
        return re_count
```



## [C++](./697.%20数组的度.cc)

```c++
class Solution {
  public:
    int findShortestSubArray(vector<int> &nums) {
        if (nums.empty())
            return 0;
        map<int, vector<int>> dic;
        for (int i = 0; i < nums.size(); i++) {
            if (dic.count(nums[i]) == 0)
                dic[nums[i]] = vector<int>{1, i, i};
            else
                dic[nums[i]][0] += 1, dic[nums[i]][2] = i;
        }

        int re_count = 0, *max_number = nullptr;
        for (auto v : dic) {
            if (max_number == nullptr) {
                max_number = new int(v.second[0]);
                re_count = v.second[2] - v.second[1] + 1;
            } else {
                if (v.second[0] > *max_number) {
                    *max_number = v.second[0];
                    re_count = v.second[2] - v.second[1] + 1;
                } else if (v.second[0] == *max_number) {
                    int count = v.second[2] - v.second[1] + 1;
                    if (count < re_count) {
                        re_count = count;
                    }
                }
            }
        }
        return re_count;
    }
};
```

# 717. 1比特与2比特字符

## [题目](https://leetcode-cn.com/problems/1-bit-and-2-bit-characters/)

有两种特殊字符。第一种字符可以用一比特0来表示。第二种字符可以用两比特(10 或 11)来表示。

现给一个由若干比特组成的字符串。问最后一个字符是否必定为一个一比特字符。给定的字符串总是由0结束。

示例 1:

输入: 

> bits = [1, 0, 0]
>
> 输出: True
>
> 解释: 
>
> 唯一的编码方式是一个两比特字符和一个一比特字符。所以最后一个字符是一比特字符。

示例 2:

> 输入: 
>
> bits = [1, 1, 1, 0]
>
> 输出: False
>
> 解释: 
>
> 唯一的编码方式是两比特字符和两比特字符。所以最后一个字符不是一比特字符。

**注意:**

- `1 <= len(bits) <= 1000`.
- `bits[i]` 总是`0` 或 `1`.

## [Python](./717.%201比特与2比特字符.py)

```python
class Solution:
    def isOneBitCharacter(self, bits: [int]) -> bool:
        length = len(bits)
        while index < length - 1:
            if bits[index] == 1:
                index += 2
            else:
                index += 1
        return index == 0
```



## [C++](./717.%201比特与2比特字符.cc)

```c++
class Solution {
  public:
    bool isOneBitCharacter(vector<int> &bits) {
        int size = bits.size(), index = 0;
        while (index < size - 1) {
            if (bits[index] == 1)
                index += 2;
            else
                index += 1;
        }
        return index == size - 1;
    }
};
```

## 总结

不要想的过于复杂，直接正面扫描，很简单的一题。

# 724. 寻找数组的中心索引

## [题目](https://leetcode-cn.com/problems/find-pivot-index/)

给定一个整数类型的数组 `nums`，请编写一个能够返回数组“**中心索引**”的方法。

我们是这样定义数组中心索引的：数组中心索引的左侧所有元素相加的和等于右侧所有元素相加的和。

如果数组不存在中心索引，那么我们应该返回 -1。如果数组有多个中心索引，那么我们应该返回最靠近左边的那一个。

示例 1:

> 输入: 
>
> nums = [1, 7, 3, 6, 5, 6]
>
> 输出: 3
>
> 解释: 
>
> 索引3 (nums[3] = 6) 的左侧数之和(1 + 7 + 3 = 11)，与右侧数之和(5 + 6 = 11)相等。
>
> 同时, 3 也是第一个符合要求的中心索引。

示例 2:

> 输入: 
>
> nums = [1, 2, 3]
>
> 输出: -1
>
> 解释: 
>
> 数组中不存在满足此条件的中心索引。

说明:**

- `nums` 的长度范围为 `[0, 10000]`。
- 任何一个 `nums[i]` 将会是一个范围在 `[-1000, 1000]`的整数。

## [Python](./724.%20寻找数组的中心索引.py)

```python
class Solution:
    def pivotIndex(self, nums: [int]) -> int:
        length = len(nums)
        left = None
        right = None
        for index in range(length):
            if left == None:
                left = sum(nums[0:index])
                right = sum(nums[index+1:])
            else:
                left += nums[index-1]
                right -= nums[index]
            if left == right:
                return index + 1
        return -1
```



## [C++](./724.%20寻找数组的中心索引.cc)

```c++
class Solution {
  public:
    int pivotIndex(vector<int> &nums) {
        int length = nums.size(), *left = nullptr, *right = nullptr;
        int cur_index = -1;
        for (int index = 0; index < length; index++) {
            if (left == nullptr) {
                left = new int(0);
                right = new int(accumulate(nums.begin() + 1, nums.end(), 0));
            } else {
                *left += nums[index - 1];
                *right -= nums[index];
            }
            if (*left == *right) {
                cur_index = index;
                break;
            }
        }
        delete left, delete right;
        return cur_index;
    }
};
```

