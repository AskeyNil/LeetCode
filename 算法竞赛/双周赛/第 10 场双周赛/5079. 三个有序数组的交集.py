'''
Description: 三个有序数组的交集
Author: AskeyNil
CreateDate: 2019-10-05 22:32:22
LastEditors: AskeyNil

*********************************
**                             **
**     　  你只有足够努力     　  **
**       才能看上去毫不费力       **
**                             **
*********************************

'''


class Solution:
    def arraysIntersection(self, arr1: [int], arr2: [int], arr3: [int]) -> [int]:
        i, j, k = 0, 0, 0
        len_i, len_j, len_k = len(arr1), len(arr2), len(arr3)
        result = []
        while i < len_i and j < len_j and k < len_k:
            if arr1[i] == arr2[j] == arr3[k]:
                result.append(arr1[i])
                i += 1
                j += 1
                k += 1
            elif arr1[i] < arr2[j] and arr1[i] < arr3[k]:
                i += 1
            elif arr2[j] < arr1[i] and arr2[j] < arr3[k]:
                j += 1
            elif arr3[k] < arr1[i] and arr3[k] < arr2[j]:
                k += 1
            elif arr1[i] == arr2[j]:
                i += 1
                j += 1
            elif arr1[i] == arr3[k]:
                i += 1
                k += 1
            elif arr2[j] == arr3[k]:
                j += 1
                k += 1
        return result


print(Solution().arraysIntersection([1, 2, 3, 4, 5],
                                    [1, 2, 5, 7, 9],
                                    [1, 3, 4, 5, 8]))
