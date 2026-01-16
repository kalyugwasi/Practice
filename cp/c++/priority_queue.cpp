#include <bits/stdc++.h>
using namespace std;

void print(priority_queue<int> s) {
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
    freopen("output.txt", "w", stdout);
    typedef priority_queue<int> pq; 
    pq s;
    s.push(3); print(s);
    s.push(2); print(s);
    s.push(5); print(s);
    s.push(9); print(s);
    s.push(4); print(s);
    s.push(4); print(s);
    s.pop(); print(s);
    s.pop(); print(s);
    s.pop(); print(s);
    s.pop(); print(s);
    s.pop(); print(s);
    return 0;
}
