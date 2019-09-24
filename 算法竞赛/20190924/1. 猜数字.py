'''
Description: 添加一个描述!!!
Author: AskeyNil
CreateDate: 2019-09-24 22:08:33
LastEditors: AskeyNil

*********************************
**                             **
**     　  你只有足够努力     　  **
**       才能看上去毫不费力       **
**                             **
*********************************

'''
class Solution:
    def game(self, guess: [int], answer: [int]) -> int:
        count = 0
        for index in range(3):
            if guess[index] == answer[index]:
                count += 1
        return count
