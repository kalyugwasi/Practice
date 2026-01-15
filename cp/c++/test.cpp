#define F first
#define S second
#define PB push_back
#define MP make_pair
#define REP(i,a,b) for (auto i=a;i!=b;i++)
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    typedef vector<int> vi;
    typedef set<int> si;
    si s = {-1,2,4,-3,5,2,-5,2};
    REP(it,s.begin(),s.end()){
        cout<< *it <<"\n";
    }
    return 0;
}
