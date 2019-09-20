/*
 * Description: 杨辉三角 II
 * Author: AskeyNil
 * CreateDate: 2019-09-20 08:27:33
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
#include <string>
#include <vector>

using namespace std;

// 递归法
// class Solution {
//    public:
//     vector<int> getRow(int rowIndex) {
//         if (rowIndex == 0) {
//             vector<int> vv;
//             vv.push_back(1);
//             return vv;
//         } else {
//             vector<int> vv = this->getRow(rowIndex - 1);
//             vector<int> vv1;
//             int left = 0;
//             for (auto num : vv) {
//                 vv1.push_back(left + num);
//                 left = num;
//             }
//             vv1.push_back(1);
//             return vv1;
//         }
//     }
// };

// 公式法
class Solution {
   public:
    vector<int> getRow(int rowIndex) {
        vector<int> v{1};
        if (rowIndex == 0) return v;
        for (int i = 0; i < rowIndex; i++) {
            if (i >= rowIndex / 2.0) {
                v.push_back(v[rowIndex - i - 1]);
            } else {
                v.push_back(v[i] * ((long)rowIndex - i) / (i + 1));
            }
        }
        return v;
    }
};

ostream& operator<<(ostream& out, vector<int> v) {
    for (auto i : v) {
        out << i << endl;
    }
    return out;
}

int main(int argc, char const* argv[]) {
    std::cout << Solution().getRow(100) << std::endl;
    return 0;
}
