num = 0
rows = []
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def dfs(cnt, x, y):
    rows[x][y] = '0'
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < num and 0 <= ny < num and rows[nx][ny] == '1':
            cnt = dfs(cnt+1, nx, ny)
    return cnt

if __name__ == "__main__":
    num = int(input())
    for i in range(num):
        tmp = list(input())
        rows.append(tmp)
    houses = []
    for i in range(num):
        for j in range(num):
            if rows[i][j] == '1':
                houses.append(dfs(1, i, j))
    print(len(houses))
    for i in sorted(houses):
        print(i)