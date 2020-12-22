#include <iostream>
#define MAX 31

using namespace std;

int N, n, m;
int comb[MAX][MAX] = {0, };

int main() {
    ios_base::sync_with_stdio(false); cin.tie(NULL);
    cin >> N;

    comb[1][0] = 1;    
    comb[1][1] = 1;
    for (int i = 2; i < MAX; i++){
        comb[i][0] = 1;
        for (int j = 1; j < MAX; j++){
            comb[i][j] = comb[i-1][j-1] + comb[i-1][j];
        }
        comb[i][i] = 1;
    }

    for(int i = 0; i < N; i++) {
        cin >> n >> m;
        cout << comb[m][n] << '\n';
    }

}