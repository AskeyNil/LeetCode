'''
Description: 种花问题
Author: AskeyNil
CreateDate: 2019-09-23 11:44:27
LastEditors: AskeyNil

*********************************
**                             **
**     　  你只有足够努力     　  **
**       才能看上去毫不费力       **
**                             **
*********************************

'''


class Solution:
    def canPlaceFlowers(self, flowerbed: [int], n: int) -> bool:
        reset = 1
        for bed in flowerbed:
            if bed == 1:
                reset = 0
            else:
                if reset == 2:
                    n -= 1
                    reset = 1
                else:
                    reset += 1
        if reset == 2:
            n -= 1
        return n == 0
