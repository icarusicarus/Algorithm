#include <iostream>
#define MAX 12

using namespace std;

int N, n;
int sum[MAX];

int main() {
    ios_base::sync_with_stdio(false); cin.tie(NULL);
    cin >> N;
    sum[0] = 0;
    sum[1] = 1;
    sum[2] = 2;
    sum[3] = 4;
    for(int i = 4; i < MAX; i++) {
        sum[i] = sum[i-1] + sum[i-2] + sum[i-3];
    }
    for(int i = 0; i < N; i++) {
        cin >> n;
        cout << sum[n] << '\n';
    }
}