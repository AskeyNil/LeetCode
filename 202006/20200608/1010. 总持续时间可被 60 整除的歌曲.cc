#include <vector>
#include <iostream>

using namespace std;

class Solution {
public:
    int numPairsDivisibleBy60(const vector<int> &time) {
        vector<int> v(60, 0);
        for (int value : time)
            v[value % 60] += 1;
        int sum = 0;
        for (auto i = 1; i < 30; i++)
            sum += v[i] * v[60 - i];
        sum += v[0] * (v[0] - 1) / 2;
        sum += v[30] * (v[30] - 1) / 2;
        return sum;
    }
};

int main(int argc, char const *argv[]) {
    cout << Solution().numPairsDivisibleBy60({100, 100}) << endl;
    return 0;
}
