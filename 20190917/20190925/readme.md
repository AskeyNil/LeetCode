# 747. 至少是其他数字两倍的最大数

## [题目](https://leetcode-cn.com/problems/largest-number-at-least-twice-of-others/)

在一个给定的数组nums中，总是存在一个最大元素 。

查找数组中的最大元素是否至少是数组中每个其他数字的两倍。

如果是，则返回最大元素的索引，否则返回-1。

示例 1:

> 输入: nums = [3, 6, 1, 0]
>
> 输出: 1
>
> 解释: 6是最大的整数, 对于数组中的其他整数,
>
> 6大于数组中其他元素的两倍。6的索引是1, 所以我们返回1.


示例 2:

> 输入: nums = [1, 2, 3, 4]
>
> 输出: -1
>
> 解释: 4没有超过3的两倍大, 所以我们返回 -1.

**提示:**

1. `nums` 的长度范围在`[1, 50]`.
2. 每个 `nums[i]` 的整数范围在 `[0, 100]`.

## [Python](./747.%20至少是其他数字两倍的最大数.py)

```python
class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        i = -1
        max_number = None
        for index, num in enumerate(nums):
            if max_number == None:
                i = index
                max_number = num
            else:
                if max_number < num:
                    max_number = num
                    if max_number * 2 < num:
                        i = index
                    else:
                        i = -1
        return i
```



## [C++](./747.%20至少是其他数字两倍的最大数.cc)

```c++
class Solution {
  public:
    int dominantIndex(vector<int> &nums) {
        int i = -1, max_number = -2;
        for (int index = 0; index < nums.size(); index++) {
            if (max_number == -2) {
                i = index;
                max_number = nums[index];
            } else {
                if (max_number < nums[index]) {
                    if (max_number * 2 <= nums[index]) {
                        i = index;
                    } else {
                        i = -1;
                    }
                    max_number = nums[index];
                } else if (nums[index] * 2 > max_number) {
                    i = -1;
                }
            }
        }
        return i;
    }
};
```

# 766. 托普利茨矩阵

## [题目](https://leetcode-cn.com/problems/toeplitz-matrix/)

如果一个矩阵的每一方向由左上到右下的对角线上具有相同元素，那么这个矩阵是托普利茨矩阵。

给定一个 `M x N` 的矩阵，当且仅当它是*托普利茨矩阵*时返回 `True`。

示例 1:

```
输入: 
matrix = [
  [1,2,3,4],
  [5,1,2,3],
  [9,5,1,2]
]
输出: True
解释:
在上述矩阵中, 其对角线为:
"[9]", "[5, 5]", "[1, 1, 1]", "[2, 2, 2]", "[3, 3]", "[4]"。
各条对角线上的所有元素均相同, 因此答案是True。
```


示例 2:

```
输入:
matrix = [
  [1,2],
  [2,2]
]
输出: False
解释: 
对角线"[1, 2]"上的元素不同。
```

**说明:**

1. `matrix` 是一个包含整数的二维数组。
2. `matix` 的行数和列数均在 `[1, 20]` 范围内。
3. `matrix[i][j]` 包含的整数在 `[0, 99]` 范围内。

**进阶:**

1. 如果矩阵存储在磁盘上，并且磁盘内存是有限的，因此一次最多只能将一行矩阵加载到内存中，该怎么办？
2. 如果矩阵太大以至于只能一次将部分行加载到内存中，该怎么办？

## [Python](./766.%20托普利茨矩阵.py)

```python
class Solution:
    def isToeplitzMatrix(self, matrix: [[int]]) -> bool:
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if matrix[i][j] != matrix[i - 1][j - 1]:
                    return False
        return True
```



## [C++](./766.%20托普利茨矩阵.cc)

```c++
class Solution {
  public:
    bool isToeplitzMatrix(vector<vector<int>> &matrix) {
        int v = matrix.size(), h = matrix[0].size();
        for (int i = 1; i < v; i++) {
            for (int j = 1; j < h; j++) {
                if (matrix[i][j] != matrix[i - 1][j - 1])
                    return false;
            }
        }
        return true;
    }
};
```

# 830. 较大分组的位置

## [题目](https://leetcode-cn.com/problems/positions-of-large-groups/)

在一个由小写字母构成的字符串 S 中，包含由一些连续的相同字符所构成的分组。

例如，在字符串 `S = "abbxxxxzyy"` 中，就含有 `"a"`, `"bb"`, `"xxxx"`, `"z"` 和 `"yy"` 这样的一些分组。

我们称所有包含大于或等于三个连续字符的分组为较大分组。找到每一个较大分组的起始和终止位置。

最终结果按照字典顺序输出。

示例 1:

```
输入: "abbxxxxzzy"
输出: [[3,6]]
解释: "xxxx" 是一个起始于 3 且终止于 6 的较大分组。
```


示例 2:

```
输入: "abc"
输出: []
解释: "a","b" 和 "c" 均不是符合要求的较大分组。
```


示例 3:

```
输入: "abcdddeeeeaabbbcd"
输出: [[3,5],[6,9],[12,14]]
```

**说明:**  `1 <= S.length <= 1000`

## [Python](./830.%20较大分组的位置.py)

```python
class Solution:
    def largeGroupPositions(self, S: str) -> [[int]]:
        left = None
        leftIndex = -1
        arr = []
        for index, c in enumerate(S):
            if left == None:
                left = c
                leftIndex = index
            elif c != left:
                if index - leftIndex >= 3:
                    arr.append([leftIndex, index - 1])
                leftIndex = index
                left = c
        if len(S) - leftIndex >= 3:
            arr.append([leftIndex, len(S) - 1])
        return arr
```



## [C++](./830.%20较大分组的位置.cc)

```c++
class Solution {
  public:
    vector<vector<int>> largeGroupPositions(string S) {
        vector<vector<int>> vv;
        int leftIndex = 0;
        char left = S[0];
        for (int index = 1; index < S.size(); index++) {
            cout << left << endl;
            if (S[index] != left) {
                if (index - leftIndex >= 3)
                    vv.push_back({leftIndex, index - 1});
                leftIndex = index;
                left = S[index];
            }
        }
        if (S.size() - leftIndex >= 3)
            vv.push_back({leftIndex, int(S.size() - 1)});
        return vv;
    }
};
```



# 832. 翻转图像

## [题目](https://leetcode-cn.com/problems/flipping-an-image/)

## [Python](./832.%20翻转图像.py)

```python
class Solution:
    def flipAndInvertImage(self, A: [[int]]) -> [[int]]:
        arr = [[0 for _ in range(len(A))] for _ in range(len(A))]
        i = 0
        for N in A:
            j = 0
            for n in N[::-1]:
                if n == 0:
                    arr[i][j] = 1
                j += 1
            i += 1
        return arr
```



## [C++](./832.%20翻转图像.cc)

### 交换法

```c++
// 交换法
class Solution {
  public:
    vector<vector<int>> flipAndInvertImage(vector<vector<int>> &A) {
        int size = A.size();
        for (auto &v : A) {
            for (size_t i = 0; i < (size + 1) / 2; i++) {
                if (v[i] == v[size - i - 1]) {
                    v[i] = 1 ^ v[i];
                    v[size - i - 1] = v[i];
                }
            }
        }
        return A;
    }
};
```

## 分析

1. 判断每行要交换的元素是否相等
2. 如果不相等，则不要进行任何操作
3. 如果相等，元素取异或即可。