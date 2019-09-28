'''
Description: 车的可用捕获量
Author: AskeyNil
CreateDate: 2019-09-28 19:30:33
LastEditors: AskeyNil

*********************************
**                             **
**     　  你只有足够努力     　  **
**       才能看上去毫不费力       **
**                             **
*********************************

'''


class Solution:
    def numRookCaptures(self, board: [[str]]) -> int:
        # 首先找到 白色车的位置
        for i, line in enumerate(board):
            for j, item in enumerate(line):
                if item == "R":
                    R_index = (i, j)
        # 定义 4 个方向向量
        direction = ((1, 0), (-1, 0), (0, 1), (0, -1))
        count = 0
        for direc in direction:
            index = R_index
            while True:
                index = index[0] + direc[0], index[1] + direc[1]
                # 判断越界
                if index[0] < 0 or index[0] > 7 or index[1] < 0 or index[1] > 7:
                    break
                if board[index[0]][index[1]] == "B":
                    break
                if board[index[0]][index[1]] == "p":
                    count += 1
                    break
        return count
