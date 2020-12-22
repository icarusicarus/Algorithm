#include <iostream>
#define MAX 301

using namespace std;

int N;
int stairs[MAX];
int dp[MAX][2];

int main() {
    ios_base::sync_with_stdio(false); cin.tie(NULL);
    cin >> N;
    for(int i = 0; i < N; i++) {
        cin >> stairs[i];
    }

    dp[0][0] = stairs[0];
    dp[0][1] = 0;
    dp[1][0] = stairs[1];
    dp[1][1] = stairs[0] + stairs[1];

    for(int i = 2; i < N; i++) {
        dp[i][0] = max(dp[i-2][0], dp[i-2][1]) + stairs[i];
        dp[i][1] = dp[i-1][0] + stairs[i];
    }

    cout << max(dp[N-1][0], dp[N-1][1]);

}