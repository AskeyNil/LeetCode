'''
Description: 查找两棵二叉搜索树之和
Author: AskeyNil
CreateDate: 2019-10-05 22:43:43
LastEditors: AskeyNil

*********************************
**                             **
**     　  你只有足够努力     　  **
**       才能看上去毫不费力       **
**                             **
*********************************

'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def list_tree(self, root: TreeNode) -> [int]:
        result = []
        if root.left is not None:
            result += self.list_tree(root.left)
        result.append(root.val)
        if root.right is not None:
            result += self.list_tree(root.right)
        return result

    def twoSumBSTs(self, root1: TreeNode, root2: TreeNode, target: int) -> bool:
        # 左序遍历
        arr1 = self.list_tree(root1)
        arr2 = self.list_tree(root2)
        i, j = 0, len(arr2) - 1
        while i < len(arr1) and j >= 0:
            if arr1[i] + arr2[j] == target:
                return True
            elif arr1[i] + arr2[j] > target:
                j -= 1
            else:
                i += 1
        return False
