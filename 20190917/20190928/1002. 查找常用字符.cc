/*
 * Description: 查找常用字符
 * Author: AskeyNil
 * CreateDate: 2019-09-28 20:06:02
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
    vector<string> commonChars(vector<string> &A) {
        vector<map<string, int>> counts;
        for (string &str : A) {
            map<string, int> m;
            for (char &c : str) {
                string s{c};
                m[s] += 1;
            }
            counts.push_back(m);
        }
        vector<string> result;
        // 遍历第一个字典
        for (auto &key : counts[0]) {
            int number = key.second;
            bool is_add = true;
            for (int i = 1; i < counts.size(); i++) {
                auto &value = counts[i];
                if (value.find(key.first) == value.end()) {
                    is_add = false;
                    break;
                } else {
                    if (value[key.first] < number) {
                        number = value[key.first];
                    }
                }
            }
            if (is_add) {
                for (int j = 0; j < number; j++) {
                    result.push_back(key.first);
                }
            }
        }
        return result;
    }
};
