/*
 * Description: 车的可用捕获量
 * Author: AskeyNil
 * CreateDate: 2019-09-28 19:30:38
 * LastEditors: AskeyNil
 *
 * *********************************
 * **                             **
 * **     　  你只有足够努力     　  **
 * **       才能看上去毫不费力       **
 * **                             **
 * *********************************
 *
 */

/* class Solution:
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
*/

#include <iostream>
#include <string>
#include <vector>

using namespace std;

class Solution {
  public:
    int numRookCaptures(vector<vector<char>> &board) {
        int x, y, count = 0;
        for (int i = 0; i < 8; i++) {
            for (int j = 0; j < 8; j++) {
                if (board[i][j] == 'R')
                    x = i, y = j;
            }
        }
        vector<vector<int>> direction{{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
        for (auto v : direction) {
            int x1 = x, y1 = y;
            while (true) {
                x1 += v[0], y1 += v[1];
                if (x1 < 0 || x1 > 7 || y1 < 0 || y1 > 7)
                    break;
                if (board[x1][y1] == 'B')
                    break;
                if (board[x1][y1] == 'p') {
                    count += 1;
                    break;
                }
            }
        }
        return count;
    }
};