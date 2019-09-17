# 1. 两数之和
## [题目](https://leetcode-cn.com/problems/two-sum/)

给定一个整数数组 `nums` 和一个目标值 `target`，请你在该数组中找出和为目标值的那 **两个** 整数，并返回他们的数组下标。

你可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素。

示例:

> 给定 nums = [2, 7, 11, 15], target = 9
>
> 因为 nums[0] + nums[1] = 2 + 7 = 9
>
> 所以返回 [0, 1]

## [Python](./1.%20两数之和.py)

``` python
class Solution:
    def twoSum(self, nums: list, target: int) -> list:
        dic = {}
        for index, num in enumerate(nums):
            if target - num in dic:
                return [dic[target - num], index]
            else:
                dic[num] = index
```



# 2. 两数相加

## [题目](https://leetcode-cn.com/problems/add-two-numbers/)

给出两个 **非空** 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 **逆序** 的方式存储的，并且它们的每个节点只能存储 一位 数字。

如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。

您可以假设除了数字 0 之外，这两个数都不会以 0 开头。

**示例**：

> **输入**：(2 -> 4 -> 3) + (5 -> 6 -> 4)
>
> **输出**：7 -> 0 -> 8
>
> **原因**：342 + 465 = 807

## [Python](./2.%20两数相加.py)

``` python
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
```



# 3. 无重复字符的最长子串
## [题目](https://leetcode-cn.com/problems/longest-substring-without-repeating-characters/)

给定一个字符串，请你找出其中不含有重复字符的 **最长子串** 的长度。

示例 1:

> **输入**: "abcabcbb"
>
> **输出**: 3 
>
> **解释**: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。

示例 2:

> **输入**: "bbbbb"
>
> **输出**: 1
>
> **解释**: 因为无重复字符的最长子串是 "b"，所以其长度为 1。

示例 3:

> **输入**: "pwwkew"
>
> **输出**: 3
>
> **解释**: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
>      请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。

## [Python](./3.%20无重复字符的最长子串.py)

``` python
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        temp_str = ""
        max_number = 0
        for index, char in enumerate(s):
            if char in temp_str:
                i = temp_str.index(char)
                max_number = max(len(temp_str), max_number)
                temp_str = temp_str[i+1:]
            temp_str += char
        max_number = max(len(temp_str), max_number)
        return max_number
```

