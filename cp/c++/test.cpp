#include <bits/stdc++.h>
using namespace std;

const int INF = 1e9;

int solve(int x, vector<int>& coins, vector<int>& dp) {
    if (x < 0) return INF;
    if (x == 0) return 0;
    if (dp[x] != -1) return dp[x];

    int best = INF;
    for (int c : coins) {
        best = min(best, solve(x - c, coins, dp) + 1);
    }

    return dp[x] = best;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);

    int target, n;
    cin >> target >> n;

    vector<int> coins(n);
    for (int i = 0; i < n; i++) {
        cin >> coins[i];
    }

    vector<int> dp(target + 1, -1);
    int ans = solve(target, coins, dp);

    if (ans == INF)
        cout << -1;
    else
        cout << ans <<"\n";
    for (auto i:dp){
        cout<<i<<"\n";
    }

    return 0;
}