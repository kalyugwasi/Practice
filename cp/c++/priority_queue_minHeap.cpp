#include <bits/stdc++.h>
using namespace std;

typedef priority_queue<int,vector<int>,greater<int>> pq; 

void print(pq s){
    if (s.empty()){
        cout<<"[ ]\n";
        return;
    }
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
    pq s;
    s.push(3); print(s);
    s.push(2); print(s);
    s.push(5); print(s);
    s.push(7); print(s);
    s.push(4); print(s);
    s.push(4); print(s);
    s.pop(); print(s);
    s.pop(); print(s);
    s.pop(); print(s);
    s.pop(); print(s);
    s.pop(); print(s);
    return 0;
}
