#define PB push_back
#define PF push_front
#define PopB pop_back
#define PopF pop_front
#define MP make_pair
#define REP(i,a,b) for (auto i=a;i!=b;i++)
#include <bits/stdc++.h>
using namespace std;

void print(priority_queue<int> s) {
    if (s.empty()){
        cout<<"[ ]";
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
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    typedef deque<int> di;
    typedef stack<int> si;
    typedef queue<int> qi;
    typedef priority_queue<int> pq; 
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
