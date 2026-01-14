#define REP(i,a,b) for (int i=a;i<b;i++)
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    typedef vector<int> vi;
    vi array = {-1,2,4,-3,5,2,-5,2};
    int best=0,sum=0,n = array.size();
    REP(k,0,n){
        sum = max(array[k],sum+array[k]);
        best = max(best,sum);
    }
    cout<< best << "\n";
    return 0;
}
