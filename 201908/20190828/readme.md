# 9. 回文数
## [题目](https://leetcode-cn.com/problems/palindrome-number/)

判断一个整数是否是回文数。回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。

**示例 1**:

> **输入**: 121
>
> **输出**: true

**示例 2**:

> **输入**: -121
>
> **输出**: false
>
> **解释**: 从左向右读, 为 -121 。 从右向左读, 为 121- 。因此它不是一个回文数。

**示例 3**:

输入: 10

> **输出**: false
>
> **解释**: 从右向左读, 为 01 。因此它不是一个回文数。

**进阶**:

你能不将整数转为字符串来解决这个问题吗？

## [Python](./9.%20回文数.py)

```python
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        return str(x)[::-1] == str(x)
```



# 10. 正则表达式匹配

## [题目](https://leetcode-cn.com/problems/regular-expression-matching/)

给你一个字符串 s 和一个字符规律 p，请你来实现一个支持 '.' 和 '*' 的正则表达式匹配。

> '.' 匹配任意单个字符
>
> '*' 匹配零个或多个前面的那一个元素
>

所谓匹配，是要涵盖 整个 字符串 s的，而不是部分字符串。

**说明**:

- `s` 可能为空，且只包含从 `a-z` 的小写字母。
- `p` 可能为空，且只包含从 `a-z` 的小写字母，以及字符 `.` 和 `*`。

示例 1:

> **输入**:
>
> s = "aa"
>
> p = "a"
>
> **输出**: false
>
> **解释**: "a" 无法匹配 "aa" 整个字符串。

**示例 2**:

输入:

> s = "aa"
>
> p = "a\*"
>
> 输出: true
>
> 解释: 因为 '*' 代表可以匹配零个或多个前面的那一个元素, 在这里前面的元素就是 'a'。因此，字符串 "aa" 可被视为 'a' 重复了一次。

示例 3:

> **输入**:
> s = "ab"
>
> p = ".\*"
>
> **输出**: true
>
> **解释**: ".\*" 表示可匹配零个或多个（'*'）任意字符（'.'）。

示例 4:

输入:

> s = "aab"
>
> p = "c\*a\*b"
>
> **输出**: true
>
> **解释**: 因为 '*' 表示零个或多个，这里 'c' 为 0 个, 'a' 被重复一次。因此可以匹配字符串 "aab"。

示例 5:

> **输入**:
>
> s = "mississippi"
>
> p = "mis\*is\*p*."
>
> **输出**: false

## [Python](./10.%20正则表达式匹配.py)

``` python
class Solution(object):
    def isMatch(self, text, pattern):
        if not pattern:
            return not text
        first_match = bool(text) and pattern[0] in {text[0], '.'}
        if len(pattern) >= 2 and pattern[1] == '*':
            return (self.isMatch(text, pattern[2:]) or
                    first_match and self.isMatch(text[1:], pattern))
        else:
            return first_match and self.isMatch(text[1:], pattern[1:])
```

