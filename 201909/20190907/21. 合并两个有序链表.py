'''
Description: 合并两个有序链表
Author: AskeyNil
CreateDate: 2019-09-07 21:53:02
LastEditors: AskeyNil

********************************
**                            **
**   It works on my machine   **
**                            **
********************************

'''


"""
'     将两个有序链表合并为一个新的有序链表并返回。新链表是通过拼接给
' 定的两个链表的所有节点组成的。 
'
' 示例：
' 输入：1->2->4, 1->3->4
' 输出：1->1->2->3->4->4
'
"""


# ! ######################   START   ##########################

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


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
