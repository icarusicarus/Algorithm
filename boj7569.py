import sys
M = 0
N = 0
H = 0
cnt = 0
tomato = list()
dx = [0, 0, -1, 1, 0, 0] #위, 아래, 왼, 오, 앞, 뒤 순서
dy = [1, -1, 0, 0, 0, 0]
dz = [0, 0, 0, 0, -1, 1]

def tomato_grow():
    for i in range(H):
        for j in range(N):
            for k in range(M):
                el = tomato[i][j][k]
                if (el == 0):
                    pass
                elif (el == 1):
                    for l in range(6):
                        nx = k+dx[l]
                        ny = j+dy[l]
                        nz = i+dz[l]
                        if (0 <= nz < H and 0 <= ny < N and 0 <= nx < M and tomato[nz][ny][nx] == 0):
                            tomato[nz][ny][nx] = 1
                elif (el == -1):
                    pass                  
                else:
                    break

def counter():
    global H
    global M
    global N
    cnt_one = 0
    cnt_zero = 0
    cnt_neg = 0
    for i in range(H):
        for j in range(N):
            for k in range(M):
                el = tomato[i][j][k]
                if (el == 0):
                    cnt_zero += 1
                elif (el == 1):
                    cnt_one += 1
                elif (el == -1):
                    cnt_neg += 1                    
                else:
                    break
    return cnt_one, cnt_zero, cnt_neg

if __name__ == '__main__':
    input = sys.stdin.readline
    M, N, H = map(int, input().split())
    for i in range(H):
        row = []
        for j in range(N):
            tmp = [int(x) for x in input().split()]
            row.append(tmp)
        tomato.append(row)

    pre_one = 0

    _, zero, _ = counter()
    if (zero == 0):
        print(1)
        quit()

    while (True):
        cnt += 1
        tomato_grow()
        one, zero, neg = counter()
        if (pre_one == one):
            print(-1)
            break
        if (zero == 0):
            print(cnt)
            break
        pre_one = one
