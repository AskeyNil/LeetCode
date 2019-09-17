'''
Description: 两两交换链表中的节点
Author: AskeyNil
CreateDate: 2019-09-12 08:23:48
LastEditors: AskeyNil

*********************************
**                             **
**     　  你只有足够努力     　  **
**       才能看上去毫不费力       **
**                             **
*********************************

'''

"""
'     给定一个链表，两两交换其中相邻的节点，并返回交换后的链表。
' 你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。
'
' 示例:
' 给定 1->2->3->4, 你应该返回 2->1->4->3.
"""


# ! ######################   START   ##########################
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


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
