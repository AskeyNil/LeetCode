# 509. 斐波那契数

## [题目](https://leetcode-cn.com/problems/fibonacci-number/)

**斐波那契数**，通常用 `F(n)` 表示，形成的序列称为**斐波那契数列**。该数列由 `0` 和 `1` 开始，后面的每一项数字都是前面两项数字的和。也就是：

## [Python](./509.%20斐波那契数.py)

### 递归法

```python
class Solution:
    def fib(self, N: int) -> int:
        if N == 0:
            return 0
        elif N == 1:
            return 1
        else:
            return self.fib(N-1) + self.fib(N-2)

```



### 动态规划

```python
class Solution:
    def fib(self, N: int) -> int:
        if N == 0:
            return 0
        else if N == 1 or N == 2:
            return 1
        current = 1
        previous = 1
        for index in range(3, N+1):
            current = current + previous
            previous = current - previous
        return current
```



## [C++](./509.%20斐波那契数.cc)

### 动态规划

```c++
class Solution {
public:
  int fib(int N) {
    if (N == 0)
      return 0;
    if (N == 1 || N == 2)
      return 1;
    int current = 1, previous = 1;
    for (int i = 3; i <= N; i++) {
      current = current + previous;
      previous = current - previous;
    }
    return current;
  }
};	
```



# 532. 数组中的K-diff数对

## [题目](https://leetcode-cn.com/problems/k-diff-pairs-in-an-array/)

给定一个整数数组和一个整数 k, 你需要在数组里找到不同的 k-diff 数对。这里将 k-diff 数对定义为一个整数对 (i, j), 其中 i 和 j 都是数组中的数字，且两数之差的绝对值是 k.

**示例** 1:

> **输入**: [3, 1, 4, 1, 5], k = 2
>
> **输出**: 2
>
> **解释**: 数组中有两个 2-diff 数对, (1, 3) 和 (3, 5)。
>
> 尽管数组中有两个1，但我们只应返回不同的数对的数量。

**示例** 2:

> **输入**:[1, 2, 3, 4, 5], k = 1
>
> **输出**: 4
>
> **解释**: 数组中有四个 1-diff 数对, (1, 2), (2, 3), (3, 4) 和 (4, 5)。

**示例** 3:

> **输入**: [1, 3, 1, 5, 4], k = 0
>
> **输出**: 1
>
> **解释**: 数组中只有一个 0-diff 数对，(1, 1)。

**注意**:

1. 数对 (i, j) 和数对 (j, i) 被算作同一数对。
2. 数组的长度不超过10,000。
3. 所有输入的整数的范围在 [-1e7, 1e7]。

## [Python](./532.%20数组中的K-diff数对.py)

### 一张哈希表

```python
class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        nums.sort()
        dic = {}
        left = None
        count = 0
        for num in nums:
            if left != None and left != num and (num - k) in dic:
                count += 1
            left = num
            if num in dic:
                dic[num] += 1
                if k == 0 and dic[num] == 2:
                    count += 1
            else:
                dic[num] = 1
        return count
```

### 两张哈希表

```python
class Solution:
    def findPairs(self, nums: [int], k: int) -> int:
        dic = {}
        temp = set()
        for num in nums:
            # 分两种情况
            # 1. 假设 num >= prev
            prev = num - k
            if prev in dic:
                if num >= prev:
                    temp.add((num, prev))
                    continue
            # 2. 假设 num <= prev
            prev = k + num
            if prev in dic:
                if num <= prev:
                    temp.add((prev, num))
            dic[num] = 0
        return len(temp)
```



## [C++](./532.%20数组中的K-diff数对.cc)

### 一次哈希表

```c++
class Solution {
  public:
    int findPairs(vector<int> &nums, int k) {
        map<int, int> dic;
        int count = 0, *left = nullptr;
        sort(nums.begin(), nums.end());
        for (auto &num : nums) {
            if (left != nullptr && *left != num && dic.count((num - k)) > 0) {
                count += 1;
            }
            left = &num;
            if (dic.count(num) > 0) {
                dic[num] += 1;
                if (k == 0 && dic[num] == 2) {
                    count += 1;
                }
            } else {
                dic[num] = 1;
            }
        }
        return count;
    }
};
```



# 561. 数组拆分 I

## [题目](https://leetcode-cn.com/problems/array-partition-i/)

## [Python](./561.%20数组拆分%20I.py)

### 排序法

```python
class Solution:
    def arrayPairSum(self, nums: [int]) -> int:
        length = len(nums)
        nums.sort()
        sum_num = 0
        for index in range(0, length, 2):
            sum_num += nums[index]
        return sum_num
```



## [C++](./561.%20数组拆分%20I.cc)

### 排序法

```c++
class Solution {
  public:
    int arrayPairSum(vector<int> &nums) {
        sort(nums.begin(), nums.end());
        int sum = 0;
        for (auto i = nums.begin(); i < nums.end(); i += 2) {
            sum += *i;
        }
        return sum;
    }
};
```



# 566. 重塑矩阵

## [题目](https://leetcode-cn.com/problems/reshape-the-matrix/)

在MATLAB中，有一个非常有用的函数 `reshape`，它可以将一个矩阵重塑为另一个大小不同的新矩阵，但保留其原始数据。

给出一个由二维数组表示的矩阵，以及两个正整数`r`和`c`，分别表示想要的重构的矩阵的行数和列数。

重构后的矩阵需要将原始矩阵的所有元素以相同的**行遍历顺序**填充。

如果具有给定参数的`reshape`操作是可行且合理的，则输出新的重塑矩阵；否则，输出原始矩阵。

示例 1:

```
输入: 
nums = 
[[1,2],
 [3,4]]
r = 1, c = 4
输出: 
[[1,2,3,4]]
解释:
行遍历nums的结果是 [1,2,3,4]。新的矩阵是 1 * 4 矩阵, 用之前的元素值一行一行填充新矩阵。
```


示例 2:

```
输入: 
nums = 
[[1,2],
 [3,4]]
r = 2, c = 4
输出: 
[[1,2],
 [3,4]]
解释:
没有办法将 2 * 2 矩阵转化为 2 * 4 矩阵。 所以输出原矩阵。
```

**注意**：

1. 给定矩阵的宽和高范围在 [1, 100]。
2. 给定的 r 和 c 都是正数。

## [Python](./566.%20重塑矩阵.py)

```python
class Solution:
    def matrixReshape(self, nums: [[int]], r: int, c: int) -> [[int]]:
        # 限制条件 特判
        current_r = len(nums)
        if current_r == 0:
            return nums
        current_c = len(nums[0])
        if current_c == 0:
            return nums
        if current_c * current_r != r * c:
            return nums
        return [[nums[((x*c)+y) // current_c][((x*c)+y) % current_c] for y in range(c)] for x in range(r)]
```



## [C++](./566.%20重塑矩阵.cc)

```c++
class Solution {
  public:
    vector<vector<int>> matrixReshape(vector<vector<int>> &nums, int r, int c) {
        int current_r = nums.size();
        if (current_r == 0)
            return nums;
        int current_c = nums[0].size();
        if (current_c == 0)
            return nums;
        if (current_c * current_r != r * c)
            return nums;
        vector<vector<int>> vv;
        for (size_t i = 0; i < r; i++) {
            vector<int> v;
            for (size_t j = 0; j < c; j++) {
                v.push_back(
                    nums[((i * c) + j) / current_c][((i * c) + j) % current_c]);
            }
            vv.push_back(v);
        }
        return vv;
    }
};
```

# 581. 最短无序连续子数组

## [题目](https://leetcode-cn.com/problems/shortest-unsorted-continuous-subarray/)

给定一个整数数组，你需要寻找一个**连续的子数组**，如果对这个子数组进行升序排序，那么整个数组都会变为升序排序。

你找到的子数组应是**最短**的，请输出它的长度。

**示例 1:**

> 输入: [2, 6, 4, 8, 10, 9, 15]
>
> 输出: 5
>
> 解释: 你只需要对 [6, 4, 8, 10, 9] 进行升序排序，那么整个表都会变为升序排序。

**说明 :**

1. 输入的数组长度范围在 [1, 10,000]。
2. 输入的数组可能包含**重复**元素 ，所以**升序**的意思是**<=。**

## [Python](./581.%20最短无序连续子数组.py)

```python
class Solution:
    def findUnsortedSubarray(self, nums: [int]) -> int:
        sorted_nums = sorted(nums)
        start = None
        end = None
        for index, num in enumerate(nums):
            if start == None and num != sorted_nums[index]:
                start = index
            elif end == None and num == sorted_nums[index]:
                end = index
            elif end != None and num != sorted_nums[index]:
                end = index
        if end == None:
            end = len(nums) - 1
        return end - start + 1
```



## [C++](./581.%20最短无序连续子数组.cc)

```c++
class Solution {
  public:
    int findUnsortedSubarray(vector<int> &nums) {
        vector<int> vv = nums;
        sort(vv.begin(), vv.end());
        int start = -1, end = -1;
        for (int i = 0; i < nums.size(); i++) {
            if (start == -1 && nums[i] != vv[i])
                start = i;
            else if (end == -1 && nums[i] == vv[i])
                end = i - 1;
            else if (end != -1 && nums[i] != vv[i])
                end = i;
        }
        if (end == -1)
            end = nums.size() - 1;
        if (start == -1)
            return 0;
        return end - start + 1;
    }
};
```



# 605. 种花问题

## [题目](https://leetcode-cn.com/problems/can-place-flowers/)

假设你有一个很长的花坛，一部分地块种植了花，另一部分却没有。可是，花卉不能种植在相邻的地块上，它们会争夺水源，两者都会死去。

给定一个花坛（表示为一个数组包含0和1，其中0表示没种植花，1表示种植了花），和一个数 n 。能否在不打破种植规则的情况下种入 n 朵花？能则返回True，不能则返回False。

示例 1:

> 输入: flowerbed = [1,0,0,0,1], n = 1
>
> 输出: True

示例 2:

> 输入: flowerbed = [1,0,0,0,1], n = 2
>
> 输出: False

注意:

1. 数组内已种好的花不会违反种植规则。
2. 输入的数组长度范围为 [1, 20000]。
3. n 是非负整数，且不会超过输入数组的大小。



## [Python](./605.%20种花问题.py)

```python
class Solution:
    def canPlaceFlowers(self, flowerbed: [int], n: int) -> bool:
        reset = 1
        for bed in flowerbed:
            if bed == 1:
                reset = 0
            else:
                if reset == 2:
                    n -= 1
                    reset = 1
                else:
                    reset += 1
        if reset == 2:
            n -= 1
        return n <= 0
```



## [C++](./605.%20种花问题.cc)

```c++
class Solution {
  public:
    bool canPlaceFlowers(vector<int> &flowerbed, int n) {
        int reset = 1;
        for (auto bed : flowerbed) {
            if (bed == 1)
                reset = 0;
            else {
                if (reset == 2) {
                    n -= 1;
                    reset = 1;
                } else {
                    reset += 1;
                }
            }
        }
        if (reset == 2) {
            n -= 1;
        }
        return n <= 0;
    }
};
```



# 628. 三个数的最大乘积

## [题目](https://leetcode-cn.com/problems/maximum-product-of-three-numbers/)

## [Python](./628.%20三个数的最大乘积.py)

```python
class Solution:
    def maximumProduct(self, nums: [int]) -> int:
        # 排序 取最后三个相乘
        nums.sort()
        max_number = nums[-1] * nums[-2] * nums[-3]
        min_number = nums[0] * nums[1] * nums[-1]
        return max_number if max_number > min_number else min_number
```



## [C++](./628.%20三个数的最大乘积.cc)

```c++
class Solution {
  public:
    int maximumProduct(vector<int> &nums) {
        sort(nums.begin(), nums.end());
        int max_number = nums[nums.size() - 1] * nums[nums.size() - 2] *
                         nums[nums.size() - 3];
        int min_number = nums[nums.size() - 1] * nums[0] * nums[1];
        return max_number > min_number ? max_number : min_number;
    }
};
```



# 643. 子数组最大平均数 I

## [题目](https://leetcode-cn.com/problems/maximum-average-subarray-i/)

## [Python](./643.%20子数组最大平均数%20I.py)

```python
class Solution:
    def findMaxAverage(self, nums: [int], k: int) -> float:
        max_aver = None
        left = None
        for index in range(len(nums) - k + 1):
            if max_aver != None:
                aver = aver - left + nums[index + k - 1]
                if max_aver < aver:
                    max_aver = aver
            else:
                aver = sum(nums[index: index + k])
                max_aver = aver
            left = nums[index]
        return max_aver / k
```



## [C++](./643.%20子数组最大平均数%20I.cc)

```c++
class Solution {
  public:
    double findMaxAverage(vector<int> &nums, int k) {
        int max_aver = INT_MIN, left = INT_MIN, aver = 0;
        for (int i = 0; i < nums.size() - k + 1; i++) {
            if (max_aver != INT_MIN) {
                aver = aver - left + nums[i + k - 1];
                if (max_aver < aver)
                    max_aver = aver;
            } else {
                for (int j = i; j < i + k; j++) {
                    aver += nums[j];
                }
                max_aver = aver;
            }
            left = nums[i];
        }
        return double(max_aver) / k;
    }
};
```

