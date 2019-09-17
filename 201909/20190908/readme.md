# 22. 括号生成

## [题目](https://leetcode-cn.com/problems/generate-parentheses/)

给出 n 代表生成括号的对数，请你写出一个函数，使其能够生成所有可能的并且**有效的**括号组合。

例如，给出 n = 3，生成结果为：

```
[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
```

## [Python](./22.%20括号生成.py)

``` python
class Solution:
    def generateParenthesis(self, n: int) -> [str]:
        if n == 1:
            return ["()"]
        p = []
        for item in self.generateParenthesis(n - 1):
            for index, char in enumerate(item):
                c = list(item)
                c.insert(index + 1, "()")
                p.append("".join(c))
        return list(set(p))
```

