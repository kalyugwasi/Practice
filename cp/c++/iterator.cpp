#define REP(i,a,b) for (auto i=a;i!=b;i++)
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    freopen("output.txt", "w", stdout);
    typedef set<int> si;
    si s = {-1,2,4,-3,5,2,-5,2};
    REP(it,s.begin(),s.end()){
        cout<< *it <<"\n";
    }
    return 0;
}
