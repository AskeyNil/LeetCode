'''
Description: 寻找两个有序数组的中位数
Author: AskeyNil
CreateDate: 2019-08-26 08:22:36
LastEditors: AskeyNil

********************************
**                            **
**   It works on my machine   **
**                            **
********************************

'''

"""
'     给定两个大小为 m 和 n 的有序数组 nums1 和 nums2。
' 请你找出这两个有序数组的中位数，并且要求算法的时间复杂度为
' O(log(m + n))。你可以假设 nums1 和 nums2 不会同时为空。
'
' 示例 1:
' nums1 = [1, 3]
' nums2 = [2]
' 则中位数是 2.0
'
' 示例 2:
' nums1 = [1, 2]
' nums2 = [3, 4]
' 则中位数是 (2 + 3)/2 = 2.5
"""

# ! ######################   START   ##########################
# !
# ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! !
# ! !         完成 但是时间复杂度不对应  O(log(m + n))          ! !
# ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! !
# !


class Solution:
    def findMedianSortedArrays(self, nums1: list, nums2: list):
        nums = nums1 + nums2
        nums.sort()
        count = len(nums)
        if count % 2 == 0:  # 偶数
            return (nums[count // 2] + nums[count // 2 - 1]) / 2
        else:
            return(nums[count // 2])
        pass


print(Solution().findMedianSortedArrays([1, 2], [3, 4]))
