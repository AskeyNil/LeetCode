'''
Description: 杨辉三角
Author: AskeyNil
CreateDate: 2019-09-20 07:45:07
LastEditors: AskeyNil

*********************************
**                             **
**     　  你只有足够努力     　  **
**       才能看上去毫不费力       **
**                             **
*********************************

'''


class Solution:
    def generate(self, numRows: int) -> [[int]]:
        if numRows == 0:
            return [[]
        if numRows == 1:
            return [[1]]
        else:
            left = 0
            rows = self.generate(numRows - 1)
            rows.append([])
            for num in rows[-2]:
                rows[-1].append(num + left)
                left = num
            rows[-1].append(1)
            return rows


print(Solution().generate(100))
