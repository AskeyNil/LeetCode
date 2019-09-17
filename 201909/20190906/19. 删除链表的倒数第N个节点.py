'''
Description: 删除链表的倒数第N个节点
Author: AskeyNil
CreateDate: 2019-09-06 21:13:20
LastEditors: AskeyNil

********************************
**                            **
**   It works on my machine   **
**                            **
********************************

'''

"""
'     给定一个链表，删除链表的倒数第 n 个节点，并且返回链表的头结点。
'
' 示例：
' 给定一个链表: 1->2->3->4->5, 和 n = 2.
'
' 当删除了倒数第二个节点后，链表变为 1->2->3->5.
' 说明：
' 给定的 n 保证是有效的。
' 进阶：
' 你能尝试使用一趟扫描实现吗？
"""


# ! ######################   START   ##########################


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        # 双指针
        left, right = 0, 0
        firstNode = head
        deleteNode = None
        while head:
            if right >= left + n:
                left += 1
                if deleteNode is None:
                    deleteNode = firstNode
                else:
                    deleteNode = deleteNode.next
            head = head.next
            right += 1
        if deleteNode is None:
            # 删除第一个元素
            firstNode = firstNode.next
        else:
            deleteNode.next = deleteNode.next.next
        return firstNode
