# 24. 两两交换链表中的节点

## [题目](https://leetcode-cn.com/problems/swap-nodes-in-pairs/)

给定一个链表，两两交换其中相邻的节点，并返回交换后的链表。

**你不能只是单纯的改变节点内部的值**，而是需要实际的进行节点交换。

**示例**:

> 给定 1->2->3->4, 你应该返回 2->1->4->3.
>

## [Python](./24.%20两两交换链表中的节点.py)

``` python
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        first = head
        is_first = True
        while head:
            if head.next is None:
                break
            headNext = head.next
            headNext.next, head.next = head, headNext.next
            if is_first:
                is_first = False
                first = headNext
            else:
                before.next = headNext
            before = head
            head = head.next
        return first
```

