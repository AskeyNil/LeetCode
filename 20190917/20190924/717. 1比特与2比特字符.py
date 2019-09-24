'''
Description: 1比特与2比特字符
Author: AskeyNil
CreateDate: 2019-09-24 10:39:35
LastEditors: AskeyNil

*********************************
**                             **
**     　  你只有足够努力     　  **
**       才能看上去毫不费力       **
**                             **
*********************************

'''


# 扫描
class Solution:
    def isOneBitCharacter(self, bits: [int]) -> bool:
        length = len(bits)
        while index < length - 1:
            if bits[index] == 1:
                index += 2
            else:
                index += 1
        return index == 0
