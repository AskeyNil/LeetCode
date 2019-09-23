/*
 * Description: 种花问题
 * Author: AskeyNil
 * CreateDate: 2019-09-23 11:51:10
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
#include <vector>

using namespace std;

class Solution {
  public:
    bool canPlaceFlowers(vector<int> &flowerbed, int n) {
        int reset = 1;
        for (auto bed : flowerbed) {
            if (bed == 1)
                reset = 0;
            else {
                if (reset == 2) {
                    n -= 1;
                    reset = 1;
                } else {
                    reset += 1;
                }
            }
        }
        if (reset == 2) {
            n -= 1;
        }
        return n <= 0;
    }
};