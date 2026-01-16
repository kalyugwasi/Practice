#include <bits/stdc++.h>
using namespace std;
void print(stack<int> s) {
    cout << "[ ";
    while (!s.empty()) {
        cout << s.top() << ' ';
        s.pop();
    }
    cout << "]\n";
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    typedef stack<int> si;
    si s;
    s.push(3); print(s);
    s.push(2); print(s);
    s.push(5); print(s);
    s.pop(); print(s);
    return 0;
}
