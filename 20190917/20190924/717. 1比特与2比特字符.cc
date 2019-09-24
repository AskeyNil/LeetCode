/*
 * Description: 1比特与2比特字符
 * Author: AskeyNil
 * CreateDate: 2019-09-24 10:39:46
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

// 扫描
class Solution {
  public:
    bool isOneBitCharacter(vector<int> &bits) {
        int size = bits.size(), index = 0;
        while (index < size - 1) {
            if (bits[index] == 1)
                index += 2;
            else
                index += 1;
        }
        return index == size - 1;
    }
};