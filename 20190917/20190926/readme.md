# 849. 到最近的人的最大距离

## [题目](https://leetcode-cn.com/problems/maximize-distance-to-closest-person/)

在一排座位（ `seats`）中，`1` 代表有人坐在座位上，`0` 代表座位上是空的。

至少有一个空座位，且至少有一人坐在座位上。

亚历克斯希望坐在一个能够使他与离他最近的人之间的距离达到最大化的座位上。

返回他到离他最近的人的最大距离。

示例 1：

```
输入：[1,0,0,0,1,0,1]
输出：2
解释：
如果亚历克斯坐在第二个空位（seats[2]）上，他到离他最近的人的距离为 2 。
如果亚历克斯坐在其它任何一个空位上，他到离他最近的人的距离为 1 。
因此，他到离他最近的人的最大距离是 2 。 
```


示例 2：

```
输入：[1,0,0,0]
输出：3
解释： 
如果亚历克斯坐在最后一个座位上，他离最近的人有 3 个座位远。
这是可能的最大距离，所以答案是 3 。
```

**提示：**

1. `1 <= seats.length <= 20000`
2. `seats` 中只含有 0 和 1，至少有一个 `0`，且至少有一个 `1`。

## [Python](./849.%20到最近的人的最大距离.py)

```python
class Solution:
    def maxDistToClosest(self, seats: [int]) -> int:
        indeies = [-1]
        for index, seat in enumerate(seats):
            if seat == 1:
                indeies.append(index)
        indeies.append(len(seats))
        max_index = 0
        length = len(indeies)
        for index in range(length - 1):
            tempIndex = (indeies[index + 1] - indeies[index]) // 2
            if index == 0 or index == length - 2:
                tempIndex = indeies[index + 1] - indeies[index] - 1
            if indeies[index + 1] - indeies[index] > max_index:
                max_index = tempIndex
        return max_index
```



## [C++](./849.%20到最近的人的最大距离.cc)

```c++
class Solution {
  public:
    int maxDistToClosest(vector<int> &seats) {
        vector<int> v{-1};
        for (int i = 0; i < seats.size(); i++) {
            if (seats[i] == 1)
                v.push_back(i);
        }
        v.push_back(seats.size());
        int max_index = 0, length = v.size();
        for (int i = 0; i < length - 1; i++) {
            int temp_index = (v[i + 1] - v[i]) / 2;
            if (i == 0 || i == length - 2)
                temp_index = v[i + 1] - v[i] - 1;
            if (temp_index > max_index)
                max_index = temp_index;
        }
        return max_index;
    }
};
```

# 867. 转置矩阵

## [题目](https://leetcode-cn.com/problems/transpose-matrix/)

给定一个矩阵 A， 返回 A 的转置矩阵。

矩阵的转置是指将矩阵的主对角线翻转，交换矩阵的行索引与列索引。 

示例 1：

```
输入：[[1,2,3],[4,5,6],[7,8,9]]
输出：[[1,4,7],[2,5,8],[3,6,9]]
```


示例 2：

```
输入：[[1,2,3],[4,5,6]]
输出：[[1,4],[2,5],[3,6]]
```

**提示：**

1. `1 <= A.length <= 1000`
2. `1 <= A[0].length <= 1000`

## [Python](./867.%20转置矩阵.py)

```python
class Solution:
    def transpose(self, A: [[int]]) -> [[int]]:
        line_number = len(A)
        column_number = len(A[0])
        re_result = [[0 for _ in range(line_number)]
                     for _ in range(column_number)]
        for x, line in enumerate(re_result):
            for y, item in enumerate(line):
                re_result[x][y] = A[y][x]
        return re_result
```



## [C++](./867.%20转置矩阵.cc)

```c++
class Solution {
  public:
    vector<vector<int>> transpose(vector<vector<int>> &A) {
        vector<vector<int>> vv;
        int line_count = A.size(), column_count = A[0].size();
        for (int i = 0; i < column_count; i++) {
            vector<int> v;
            for (int j = 0; j < line_count; j++) {
                v.push_back(A[j][i]);
            }
            vv.push_back(v);
        }
        return vv;
    }
};
```

# 896. 单调数列

## [题目](https://leetcode-cn.com/problems/monotonic-array/)

如果数组是单调递增或单调递减的，那么它是单调的。

如果对于所有 `i <= j`，`A[i] <= A[j]`，那么数组 A 是单调递增的。 如果对于所有 `i <= j`，`A[i]> = A[j]`，那么数组 A 是单调递减的。

当给定的数组 A 是单调数组时返回 `true`，否则返回 `fale`。

示例 1：

```
输入：[1,2,2,3]
输出：true
```


示例 2：

```
输入：[6,5,4,4]
输出：true
```


示例 3：

```
输入：[1,3,2]
输出：false
```


示例 4：

```
输入：[1,2,4,5]
输出：true
```


示例 5：

```
输入：[1,1,1]
输出：true
```

**提示：**

1. `1 <= A.length <= 50000`
2. `-100000 <= A[i] <= 100000`

## [Python](./896.%20单调数列.py)

```python
class Solution:
    def isMonotonic(self, A: [int]) -> bool:
        length = len(A)
        if length < 3:
            return True
        left = 0
        for index in range(length - 1):
            if left == 0:
                if A[index + 1] - A[index] > 0:
                    left = 1
                elif A[index + 1] - A[index] < 0:
                    left = -1
            elif left == 1:
                if A[index + 1] - A[index] < 0:
                    return False
            else:
                if A[index + 1] - A[index] > 0:
                    return False
        return True
```



## [C++](./896.%20单调数列.cc)

```c++
class Solution {
  public:
    bool isMonotonic(vector<int> &A) {
        int length = A.size();
        if (length < 3)
            return true;
        int tag = 0;
        for (int index = 0; index < length - 1; index++) {
            int diff = A[index + 1] - A[index];
            if (tag == 0) {
                if (diff > 0)
                    tag = 1;
                else if (diff < 0)
                    tag = -1;
            } else if (tag == 1) {
                if (diff < 0)
                    return false;
            } else {
                if (diff > 0)
                    return false;
            }
        }
        return true;
    }
};
```

