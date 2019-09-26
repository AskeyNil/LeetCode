/*
 * Description: 卡牌分组
 * Author: AskeyNil
 * CreateDate: 2019-09-26 22:33:56
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

#include <iostream>
#include <map>
#include <string>
#include <vector>

using namespace std;

class Solution {
  public:
    bool hasGroupsSizeX(vector<int> &deck) {
        map<int, int> dic;
        for (int num : deck) {
            dic[num] += 1;
        }
        int g = -1;
        for (auto v : dic) {
            if (g == -1) // g 给赋值第一个
                g = v.second;
            else
                g = gcd(g, v.second); // 一次判断最大公约数
        }
        return g >= 2; // 最大公约数只要大于 2 本题就是正确的
    }
    // 辗转相除法 获取最大公约数
    int gcd(int x, int y) { return x == 0 ? y : gcd(y % x, x); }
};

int main(int argc, char const *argv[]) {
    vector<int> v{1, 2, 3, 4, 4, 3, 2, 1};
    Solution().hasGroupsSizeX(v);
    return 0;
}
