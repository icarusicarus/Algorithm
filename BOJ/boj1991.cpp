#include <iostream>
#define MAX 26

using namespace std;

int N;
char tree[MAX][2];

void preorder(int r) {
    cout << char(r + 'A');
    if(tree[r][0] != '.') preorder(tree[r][0] - 'A');
    if(tree[r][1] != '.') preorder(tree[r][1] - 'A');
}

void inorder(int r) {
    if(tree[r][0] != '.') inorder(tree[r][0] - 'A');
    cout << char(r + 'A');
    if(tree[r][1] != '.') inorder(tree[r][1] - 'A');
}

void postorder(int r) {
    if(tree[r][0] != '.') postorder(tree[r][0] - 'A');
    if(tree[r][1] != '.') postorder(tree[r][1] - 'A');
    cout << char(r + 'A');
}

int main() {
    ios_base::sync_with_stdio(false); cin.tie(NULL);
    cin >> N;

    char tmp;
    for(int i = 0; i < N; i++) {
        cin >> tmp;
        int n = tmp - 'A'; 
        cin >> tree[n][0] >> tree[n][1];
    }

    preorder(0);
    cout << '\n';
    inorder(0);
    cout << '\n';
    postorder(0); 
}