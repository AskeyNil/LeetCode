# 20. 有效的括号

## [题目](https://leetcode-cn.com/problems/valid-parentheses/)

给定一个只包括 `'('`，`')'`，`'{'`，`'}'`，`'['`，`']'` 的字符串，判断字符串是否有效。

有效字符串需满足：

左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。
注意空字符串可被认为是有效字符串。

示例 1:

> 输入: "()"
>
> 输出: true

示例 2:

> 输入: "()[]{}"
>
> 输出: true

示例 3:

> 输入: "(]"
>
> 输出: false

示例 4:

> 输入: "([)]"
>
> 输出: false

示例 5:

> 输入: "{[]}"
>
> 输出: true

## [Python](./20.%20有效的括号.py)

``` python
class Solution:
    def isValid(self, s: str) -> bool:
        dic = {")": "(",
               "]": "[",
               "}": "{"}
        line = []
        for char in s:
            if char in dic:
                if not line or line.pop() != dic[char]:
                    return False
            else:
                line.append(char)
        return not line
```

# 21. 合并两个有序链表

## [题目](https://leetcode-cn.com/problems/merge-two-sorted-lists/)

将两个有序链表合并为一个新的有序链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。 

**示例**：

> **输入**：1->2->4, 1->3->4
>
> **输出**：1->1->2->3->4->4

## [Python](./21.%20合并两个有序链表.py)

``` python
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1 or not l2:
            return l1 if l1 else l2
        if l1.val <= l2.val:
            first = l1
            head = l1
            second = l2
        else:
            first = l2
            head = l2
            second = l1
        while head:
            # 碰到大于等于的数 才要插入到前面
            if head.val > second.val:
                head.val, second.val = second.val, head.val
                temp = head.next
                head.next = second
                second = second.next
                head.next.next = temp
                # second, head.next, second.next = second.next, second, head.next
            if head.next is None:
                head.next = second
                break
            head = head.next
            if second is None:
                break
        return first
```



