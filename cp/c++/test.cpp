#define PB push_back
#define PF push_front
#define PopB pop_back
#define PopF pop_front
#include <bits/stdc++.h>
using namespace std;
typedef deque<int> di;

void print(const deque<int>& d) {
        cout<<"[";
        for (int x : d) cout <<x << ' ';
        cout << "]"<<'\n';
}
int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    freopen("input.txt","r",stdin);
    freopen("output.txt", "w", stdout);
    di d;
    int x;
    while (cin >> x) {
        d.push_back(x);
    }
    cout<<d.size();
    d.PB(2); print(d);
    d.PB(2); print(d);
    d.PF(3); print(d);
    d.PopB(); print(d);
    d.PopF(); print(d);
    return 0;
}
