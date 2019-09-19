'''
Description: 加一
Author: AskeyNil
CreateDate: 2019-09-18 21:54:25
LastEditors: AskeyNil

*********************************
**                             **
**     　  你只有足够努力     　  **
**       才能看上去毫不费力       **
**                             **
*********************************

'''


class Solution:
    def plusOne(self, digits: [int]) -> [int]:
        length = len(digits) - 1
        for index in range(length, -1, -1):
            sum = digits[index] + 1
            if sum < 10:
                digits[index] = sum
                break
            else:
                digits[index] = 0
            if index == 0:
                digits.insert(0, 1)
        return digits


print(Solution().plusOne([9, 9, 9, 9]))
