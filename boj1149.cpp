#include <iostream>
#define MAX 1001

using namespace std;

int N;
int rgb[MAX][3];
int dp[MAX][3];

int main() {
    ios_base::sync_with_stdio(false); cin.tie(NULL);
    cin >> N;

    for(int i = 0; i < N; i++) {
        cin >> rgb[i][0] >> rgb[i][1] >> rgb[i][2];
    }

    for(int i = 1; i < N; i++) {
        dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + rgb[i][0];
        dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + rgb[i][1];
        dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + rgb[i][2];
    }

    cout << min(dp[N][0], min(dp[N][1], dp[N][2]));
}