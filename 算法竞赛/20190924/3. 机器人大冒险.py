'''
Description: 机器人大冒险
Author: AskeyNil
CreateDate: 2019-09-24 22:29:59
LastEditors: AskeyNil

*********************************
**                             **
**     　  你只有足够努力     　  **
**       才能看上去毫不费力       **
**                             **
*********************************

'''


class Solution:
    def robot(self, command: str, obstacles: [[int]], x: int, y: int) -> bool:

        dic = {"U": (0, 1), "R": (1, 0)}
        x1 = 0
        y1 = 0
        obs = [x1 + y1 * (x + 1) for x1, y1 in obstacles]
        obs.sort()
        count = len(obs)
        index = 0
        while True:
            for c in command:
                x1, y1 = x1 + dic[c][0], y1 + dic[c][1]
                print(x1, y1)
                cur_obs = x1 + y1 * (x + 1)
                if index < count:
                    while cur_obs >= obs[index]:
                        if cur_obs == obs[index]:
                            return False
                        else:
                            index += 1
                if x1 == x and y1 == y:
                    return True
                if x1 > x or y1 > y:
                    return False


print(Solution().robot("URRRRU", [[32, 12], [50, 27], [57, 29]], 100, 100))
