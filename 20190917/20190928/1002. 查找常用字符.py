'''
Description: 查找常用字符
Author: AskeyNil
CreateDate: 2019-09-28 20:06:09
LastEditors: AskeyNil

*********************************
**                             **
**     　  你只有足够努力     　  **
**       才能看上去毫不费力       **
**                             **
*********************************

'''


class Solution:
    def commonChars(self, A: [str]) -> [str]:
        # 统计法
        counts = []
        for string in A:
            counts.append({})
            for char in string:
                if char in counts[-1]:
                    counts[-1][char] += 1
                else:
                    counts[-1][char] = 1
        result = []
        # 统计完了 遍历第一个字典
        for key in counts[0]:
            number = counts[0][key]
            is_add = True
            for dic in counts[0:]:
                if key not in dic:
                    is_add = False
                    break
                else:
                    if dic[key] < number:
                        number = dic[key]
            if is_add:
                for _ in range(number):
                    result.append(key)
        return result
