#include <iostream>
#define MAX 21

using namespace std;

int N;
int dp[MAX];

int main(){
	ios_base::sync_with_stdio(false); cin.tie(NULL);
    cin >> N;
    int t, p;
    for(int i = 0; i < N; i++) {
        cin >> t >> p;
        if(dp[i] > dp[i+1]) {
            dp[i+1] = dp[i];
        }
        if(dp[i+t] < dp[i]+p) {
            dp[i+t] = dp[i] + p;
        }
    }

    cout << dp[N];
    
}