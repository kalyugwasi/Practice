#define PB push_back
#define PF push_front
#define PopB pop_back
#define PopF pop_front
#include <bits/stdc++.h>
using namespace std;

void print(const deque<int>& d) {
        cout<<"[";
        for (int x : d) cout <<x << ' ';
        cout << "]"<<'\n';
}
int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    freopen("output.txt", "w", stdout);
    typedef deque<int> di;
    di d;
    d.PB(5); print(d);
    d.PB(2); print(d);
    d.PF(3); print(d);
    d.PopB(); print(d);
    d.PopF(); print(d);
    return 0;
}
