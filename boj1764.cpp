#include <iostream>
#include <string.h>
#include <vector>
#include <set>
#include <algorithm>

using namespace std;

int N, M, cnt = 0;
vector<string> ans;
set<string> noHear;

int main(){
	ios_base::sync_with_stdio(false); cin.tie(NULL);
    cin >> N >> M;

    string tmp;
    for(int i = 0; i < N; i++) {
        cin >> tmp;
        noHear.insert(tmp); 
    }

    for(int i = 0; i < N; i++) {
        cin >> tmp;
        if(noHear.find(tmp) != noHear.end()) {
            ans.push_back(tmp);
        }
    }

    sort(ans.begin(), ans.end());
    cout << ans.size() << "\n";

    for(int i = 0; ans.size(); i++) cout << ans[i] << "\n";
}