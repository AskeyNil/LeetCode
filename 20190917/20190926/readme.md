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

