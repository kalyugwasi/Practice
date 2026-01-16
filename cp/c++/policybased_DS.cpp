#include <bits/stdc++.h>
#include <ext/pb_ds/assoc_container.hpp>
#include <ext/pb_ds/tree_policy.hpp>
using namespace std;
using namespace __gnu_pbds;

typedef tree<
    int,
    null_type,
    less<int>,
    greater<int>,
    rb_tree_tag,
    tree_order_statistics_node_update
> indexed_set;

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

    freopen("output.txt", "w", stdout);

    indexed_set s;
    s.insert(3); print(s);
    s.insert(2); print(s);
    s.insert(5); print(s);
    s.insert(7); print(s);
    s.insert(4); print(s);

    auto x = s.find_by_order(2);
    cout << *x << "\n";

    cout << s.order_of_key(1) << "\n";
    cout << s.order_of_key(3) << "\n";
    cout << s.order_of_key(8) << "\n";
    cout << s.order_of_key(28) << "\n";
}
