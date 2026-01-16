#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    bitset<10> a(string("0010110110"));
    bitset<10> b(string("1011011000"));
    cout<< b.count()<<"\n";
    cout<< (a&b) << "\n" << (a|b) << "\n" << (a^b) ;
    return 0;
}
