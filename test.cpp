#include <iostream>
#include <string>
#include <vector>

using namespace std;

bool checker(int n) {
    int sum = 0;
    int count_9 = 0;
    string s = to_string(n);
    for (char c : s) {
        sum += c - '0';
        if (c == '9') {
            count_9++;
        }
    }
    return sum == 9 * count_9;
}

int fuck_hanif_30_pro(int n) {
    int i = 1;
    while (true) {
        if (checker(n)) {
            return n;
        } else {
            string bin_i = to_string(i, 2);
            replace(bin_i.begin(), bin_i.end(), '1', '9');
            int num = stoi(bin_i);
            if (num % n == 0) {
                return num;
            }
            i++;
        }
    }
}

int main() {
    int n;
    cin >> n;
    cout << fuck_hanif_30_pro(n) << endl;
    return 0;
}