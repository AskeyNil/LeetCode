# 13. 罗马数字转整数
## [题目](https://leetcode-cn.com/problems/roman-to-integer/)

罗马数字包含以下七种字符： `I`， `V`， `X`， `L`，`C`，`D` 和 `M`。

```
字符          数值
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
```


例如， 罗马数字 2 写做 `II` ，即为两个并列的 1。12 `写做` `XII` ，即为 `X` + `II` 。 27 写做  `XXVII`, 即为 `XX` + `V` + `II` 。

通常情况下，罗马数字中小的数字在大的数字的右边。但也存在特例，例如 4 不写做 `IIII`，而是 `IV`。数字 1 在数字 5 的左边，所表示的数等于大数 5 减小数 1 得到的数值 4 。同样地，数字 9 表示为 `IX`。这个特殊的规则只适用于以下六种情况：

`I` 可以放在 `V` (5) 和 `X` (10) 的左边，来表示 4 和 9。
`X` 可以放在 `L` (50) 和 `C` (100) 的左边，来表示 40 和 90。 
`C` 可以放在 `D` (500) 和 `M` (1000) 的左边，来表示 400 和 900。
给定一个整数，将其转为罗马数字。输入确保在 1 到 3999 的范围内。

**示例 1**:

> **输入**: "III"
>
> **输出**: 3

**示例 2**:

> **输入**: "IV"
>
> **输出**: 4

**示例 3**:

> **输入**: "IX"
>
> **输出**: 9

**示例** 4:

> **输入**: "LVIII"
>
> **输出**: 58
>
> **解释**: L = 50, V= 5, III = 3.

**示例 5**:

> **输入**: "MCMXCIV"
>
> **输出**: 1994
>
> **解释**: M = 1000, CM = 900, XC = 90, IV = 4.



## [Python](./13.%20罗马数字转整数.py)

``` python
class Solution:
    def intToRoman(self, num: int) -> str:
        dic = [(1000, "M"),
               (900, "CM"),
               (500, "D"),
               (400, "CD"),
               (100, "C"),
               (90, "XC"),
               (50, "L"),
               (40, "XL"),
               (10, "X"),
               (9, "IX"),
               (5, "V"),
               (4, "IV"),
               (1, "I")]
        index = 0
        s = ""
        while True:
            print(index)
            if num >= dic[index][0]:
                num -= dic[index][0]
                s += dic[index][1]
            else:
                index += 1
            if num <= 0:
                return s
```



# 14. 最长公共前缀

## [题目](https://leetcode-cn.com/problems/longest-common-prefix/)

编写一个函数来查找字符串数组中的最长公共前缀。

如果不存在公共前缀，返回空字符串 ""。

**示例** 1:

> **输入**: ["flower","flow","flight"]
>
> **输出**: "fl"

**示例** 2:

> **输入**: ["dog","racecar","car"]
>
> **输出**: ""
>
> **解释**: 输入不存在公共前缀。

**说明**:

所有输入只包含小写字母 a-z 。

## [Python](./14.%20最长公共前缀.py)

``` python
class Solution:
    def longestCommonPrefix(self, strs) -> str:
        index = 0
        common = ""
        while True:
            temp_chars = map(lambda s: s[index:index+1], strs)
            temp_set = set(temp_chars)
            if len(temp_set) == 1:
                temp_str = temp_set.pop()
                if temp_str:
                    common += temp_str
                    index += 1
                    continue
            break
        return common
```

