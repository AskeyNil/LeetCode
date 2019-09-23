/*
 * Description: 斐波那契数
 * Author: AskeyNil
 * CreateDate: 2019-09-23 07:49:16
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

// 动态规划
class Solution {
  public:
    int fib(int N) {
        if (N == 0)
            return 0;
        if (N == 1 || N == 2)
            return 1;
        int current = 1, previous = 1;
        for (int i = 3; i <= N; i++) {
            current = current + previous;
            previous = current - previous;
        }
        return current;
    }
};