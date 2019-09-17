'''
Description: 两数相加
Author: AskeyNil
CreateDate: 2019-08-25 20:25:15
LastEditors: AskeyNil

********************************
**                            **
**   It works on my machine   **
**                            **
********************************

'''

"""
'     给出两个 非空 的链表用来表示两个非负的整数。
' 其中，它们各自的位数是按照 逆序 的方式存储的，并
' 且它们的每个节点只能存储 一位 数字。如果，我们将
' 这两个数相加起来，则会返回一个新的链表来表示它们
' 的和。您可以假设除了数字 0 之外，这两个数都不会
' 以 0 开头。
'
' 示例：
' 输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
' 输出：7 -> 0 -> 8
' 原因：342 + 465 = 807
"""

# ! ######################   START   ##########################


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # 是否进位, 进位了就为 1 否则为 0
        carry = 0
        # 有数据就进来循环
        left_node = None
        first_node = None
        while l1 or l2:
            l1_val = 0
            l2_val = 0
            if l1:
                l1_val = l1.val
                l1 = l1.next
            if l2:
                l2_val = l2.val
                l2 = l2.next
            add_temp = l1_val + l2_val + carry
            # 判断是否要进位, 要进位的话置 carry 为 1,然后当前数取余
            if add_temp >= 10:
                add_temp %= 10
                carry = 1
            else:  # 不要进位,将 carry 设置为 0
                carry = 0
            # 创建一个 node, val 为 add_temp
            temp_node = ListNode(add_temp)
            if not first_node:
                first_node = temp_node
                left_node = temp_node
            else:
                left_node.next = temp_node
                left_node = temp_node
        if carry == 1:
            left_node.next = ListNode(carry)
        return first_node


def create_node(l):
    first_node = None
    left_node = None
    for i in l:
        temp_node = ListNode(i)
        if not first_node:
            first_node = temp_node
            left_node = temp_node
        else:
            left_node.next = temp_node
            left_node = temp_node
    return first_node


def print_node(node):
    while node:
        print(node.val)
        node = node.next


print_node(Solution().addTwoNumbers(
    create_node([2, 4, 3]), create_node([5, 6, 4])))
