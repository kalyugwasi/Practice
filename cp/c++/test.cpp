#define PB push_back;
#define PF push_front;
#include <bits/stdc++.h>
using namespace std;

typedef ;

void print(const indexed_set& s) {
    if (s.empty()) {
        cout << "[ ]\n";
        return;
    }
    cout << "[ ";
    for (int x : s) cout << x << " ";
    cout << "]\n";
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    freopen("input.txt","r",stdin);
    freopen("output.txt", "w", stdout);
    
}
