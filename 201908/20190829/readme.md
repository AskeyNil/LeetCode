# 11. 盛最多水的容器
## [题目](https://leetcode-cn.com/problems/container-with-most-water/)

给定 n 个非负整数 a1，a2，...，an，每个数代表坐标中的一个点 (i, ai) 。在坐标内画 n 条垂直线，垂直线 i 的两个端点分别为 (i, ai) 和 (i, 0)。找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。

说明：你不能倾斜容器，且 n 的值至少为 2。



![](https://aliyun-lc-upload.oss-cn-hangzhou.aliyuncs.com/aliyun-lc-upload/uploads/2018/07/25/question_11.jpg)

图中垂直线代表输入数组 [1,8,6,2,5,4,8,3,7]。在此情况下，容器能够容纳水（表示为蓝色部分）的最大值为 49。

**示例**:

> **输入**: [1,8,6,2,5,4,8,3,7]
>
> **输出**: 49

## [Python](./11.%20盛最多水的容器.py)

``` python
class Solution:
    def maxArea(self, height) -> int:
        i = 0
        j = len(height) - 1
        max_area = 0
        while i != j:
            if height[i] > height[j]:
                temp = height[j] * (j - i)
                if temp > max_area:
                    max_area = temp
                j -= 1
            else:
                temp = height[i] * (j - i)
                if temp > max_area:
                    max_area = temp
                i += 1
        return max_area
```

