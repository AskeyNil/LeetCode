# 4. 寻找两个有序数组中的中位数
## [题目](https://leetcode-cn.com/problems/median-of-two-sorted-arrays/)

给定两个大小为 m 和 n 的有序数组 `nums1` 和 `nums2`。

请你找出这两个有序数组的中位数，并且要求算法的时间复杂度为 `O(log(m + n))`。

你可以假设 `nums1` 和 `nums2` 不会同时为空。

**示例 1:**

> nums1 = [1, 3]
>
> nums2 = [2]
>
> 则中位数是 2.0

**示例 2:**

> nums1 = [1, 2]
>
> nums2 = [3, 4]
>
> 则中位数是 (2 + 3)/2 = 2.5
>

## [Python](./4.%20寻找两个有序数组的中位数.py)

``` python
class Solution:
    def findMedianSortedArrays(self, nums1: list, nums2: list):
        nums = nums1 + nums2
        nums.sort()
        count = len(nums)
        if count % 2 == 0:  # 偶数
            return (nums[count // 2] + nums[count // 2 - 1]) / 2
        else:
            return(nums[count // 2])
        pass
```



# 5. 最长回文子串
## [题目](https://leetcode-cn.com/problems/longest-palindromic-substring/)

给定一个字符串 `s`，找到 `s` 中最长的回文子串。你可以假设 `s` 的最大长度为 1000。

**示例 1**：

> **输入**: "babad"
>
> **输出**: "bab"
>
> **注意**: "aba" 也是一个有效答案。

**示例 2**：

> **输入**: "cbbd"
>
> **输出**: "bb"

## [Python](./5.%20最长回文子串.py)

### 马拉车算法

``` python
class Solution:
    def longestPalindrome(self, s: str):
        # 1. 将 '#' 字符插入到字符串中, 任意一个不存在于字符串中的字符均可
        temp_s = ""
        for char in s:
            temp_s += "#" + char
        temp_s += "#"

        # 已查找出的最大回文子串的中心点坐标
        max_id = 0
        # 已查找出的最大回文子串的最右点坐标
        max_right = 0
        # 存储所有位置的回文数的扩散长度, 默认为 0
        p = [0 for _ in temp_s]

        # 字符串长度
        len_s = len(temp_s)

        # 记录之前最大的数据
        current_count = 1
        current_str = s[0:1]

        for index, char in enumerate(temp_s):
            # 先试试能不能直接使用 p 去获取当前的回文数值
            if max_right > index:
                p[index] = min(p[2 * max_id - index], max_right - index)
            else:
                if index > max_right:
                    raise "程序有问题"
                p[index] = 1

            # 中心匹配
            while index - p[index] >= 0 and index + p[index] < len_s and temp_s[index - p[index]] == temp_s[index + p[index]]:
                p[index] += 1

            if index + p[index] > max_right:
                max_right = index + p[index]
                max_id = index

            if p[index] - 1 > current_count:
                current_count = p[index] - 1
                current_str = temp_s[index - p[index] +
                                     1:index + p[index]].replace("#", "")

        return current_str
```

# 6. Z字形变换
## [题目](https://leetcode-cn.com/problems/zigzag-conversion/)

将一个给定字符串根据给定的行数，以从上往下、从左到右进行 Z 字形排列。

比如输入字符串为 `"LEETCODEISHIRING"` 行数为 3 时，排列如下：

``` python
L   C   I   R
E T O E S I I G
E   D   H   N
```


之后，你的输出需要从左往右逐行读取，产生出一个新的字符串，比如：`"LCIRETOESIIGEDHN"`。

请你实现这个将字符串进行指定行数变换的函数：

`string convert(string s, int numRows);`

示例 1:

> **输入**: s = "LEETCODEISHIRING", numRows = 3
>
> **输出**: "LCIRETOESIIGEDHN"

示例 2:

> **输入**: s = "LEETCODEISHIRING", numRows = 4
>
> **输出**: "LDREOEIIECIHNTSG"
>
> **解释**:
>
> ```
> L     D     R
> E   O E   I I
> E C   I H   N
> T     S     G
> ```

## [Python](./6.%20Z字形变换.py)

``` python
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        return_str = ""
        if numRows == 1:
            return s
        base_process = 2 * (numRows - 1)
        for index in range(numRows):
            if index == 0 or index == numRows - 1:
                return_str += s[index::2 * (numRows - 1)]
            else:
                return_str += self.process(s, index, base_process)
        return return_str

    def process(self, s, index, base_process):
        first = base_process - 2 * index
        second = 2 * index
        is_first = True
        return_str = ""
        while index < len(s):
            return_str += s[index]
            if is_first:
                index += first
            else:
                index += second
            is_first = not is_first
        return return_str
```

