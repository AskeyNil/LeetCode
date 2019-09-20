# 118. 杨辉三角
## [题目](https://leetcode-cn.com/problems/pascals-triangle/)

给定一个非负整数 *numRows，*生成杨辉三角的前 *numRows* 行。

![img](https://upload.wikimedia.org/wikipedia/commons/0/0d/PascalTriangleAnimated2.gif)

在杨辉三角中，每个数是它左上方和右上方的数的和。

示例:

> 输入: 5
>
> 输出:
>
> ```
> [
>      [1],
>     [1,1],
>    [1,2,1],
>   [1,3,3,1],
>  [1,4,6,4,1]
> ]
> ```

## [Python](./118.%20杨辉三角.py)
### 递归

``` python
class Solution:
    def generate(self, numRows: int) -> [[int]]:
        if numRows == 0:
            return []
        if numRows == 1:
            return [[1]]
        else:
            left = 0
            rows = self.generate(numRows - 1)
            rows.append([])
            for num in rows[-2]:
                rows[-1].append(num + left)
                left = num
            rows[-1].append(1)
            return rows
```
## [C++](./118.%20杨辉三角.cc)
### 递归
``` c++
class Solution {
   public:
    vector<vector<int>> generate(int numRows) {
        if (numRows == 0) {
            vector<vector<int>> vv;
            return vv;
        } else {
            vector<vector<int>> vv = this->generate(numRows - 1);
            vv.push_back(vector<int>());
            if (numRows != 1) {
                int left = 0;
                for (auto num : vv[numRows - 2]) {
                    vv[numRows - 1].push_back(left + num);
                    left = num;
                }
            }
            vv[numRows - 1].push_back(1);
            return vv;
        }
    }
};
```

# 119. 杨辉三角 II
## [题目](https://leetcode-cn.com/problems/pascals-triangle-ii/)
给定一个非负索引 k，其中 k ≤ 33，返回杨辉三角的第 k 行。

![img](https://upload.wikimedia.org/wikipedia/commons/0/0d/PascalTriangleAnimated2.gif)

> 在杨辉三角中，每个数是它左上方和右上方的数的和。
>
> 示例:
>
> 输入: 3
>
> 输出: [1,3,3,1]

进阶：

你可以优化你的算法到 O(k) 空间复杂度吗？
## [Python](./119.%20杨辉三角%20II.py)
### 递归
``` python
class Solution:
    def getRow(self, rowIndex: int) -> [int]:
        if rowIndex == 0:
            return [1]
        else:
            left = 0
            rows = self.getRow(rowIndex - 1)
            row = []
            for num in rows:
                row.append(num + left)
                left = num
            row.append(1)
            return row

```
### 公式法

``` python
class Solution:
    def getRow(self, rowIndex: int) -> [int]:
        rows = [1]
        if rowIndex == 1:
            return rows
        left_n = 1
        left_k = 1
        for index in range(rowIndex):
            left_n *= (rowIndex - index)
            left_k *= index + 1
            rows.append(left_n // left_k)
        return rows
```



## [C++](./119.%20杨辉三角%20II.cc)
### 递归
``` C++
class Solution {
   public:
    vector<int> getRow(int rowIndex) {
        if (rowIndex == 0) {
            vector<int> vv;
            vv.push_back(1);
            return vv;
        } else {
            vector<int> vv = this->getRow(rowIndex - 1);
            vector<int> vv1;
            int left = 0;
            for (auto num : vv) {
                vv1.push_back(left + num);
                left = num;
            }
            vv1.push_back(1);
            return vv1;
        }
    }
};
```
### 公式法
``` c++
class Solution {
   public:
    vector<int> getRow(int rowIndex) {
        vector<int> v{1};
        if (rowIndex == 0) return v;
        for (int i = 0; i < rowIndex; i++) {
            if (i >= rowIndex / 2.0) {
                v.push_back(v[rowIndex - i - 1]);
            } else {
                v.push_back(v[i] * ((long)rowIndex - i) / (i + 1));
            }
        }
        return v;
    }
};
```

### 分析
1. 注意溢出的问题
2. 先除然后乘可能会因为精度问题导致数字变小
3. 最重要的还是处理溢出问题
![img](https://pic.leetcode-cn.com/195de01eae91e09de14dd13daafbef986c42345f2bdef405153a1742175079f4.jpg)

公式法对应示意图
$$
C_n^k=C_n^{k−1}×(n−k+1)/k
$$
