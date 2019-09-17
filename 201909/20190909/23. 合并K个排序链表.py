'''
Description: 合并K个排序链表
Author: AskeyNil
CreateDate: 2019-09-08 22:20:02
LastEditors: AskeyNil

*********************************
**                             **
**     　  你只有足够努力     　  **
**       才能看上去毫不费力       **
**                             **
*********************************

'''

"""
'     合并 k 个排序链表，返回合并后的排序链表。
' 请分析和描述算法的复杂度。
'
' 示例:
' 输入:
'         [
'           1->4->5,
'           1->3->4,
'           2->6
'         ]
' 输出: 1->1->2->3->4->4->5->6
"""


# ! ######################   START   ##########################
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeKLists(self, lists: [ListNode]) -> ListNode:
        # 最简单的方法  暴力法
        # 把所有的 val 取出来 放在一个数组里
        nums = []
        for l in lists:
            while l:
                nums.append(l.val)
                l = l.next
        nums.sort()

        for index, num in enumerate(nums):
            if index == 0:
                first = ListNode(num)
                left = first
            else:
                left.next = ListNode(num)
                left = left.next
        return first
