import sys
sys.setrecursionlimit(10**6)
read = lambda : sys.stdin.readline().strip()
cnt = [0]*3
n = int(read())
matrix = [list(map(int, read().split())) for _ in range(n)]


def same(x, y, n):
    for i in range(x, x+n):
        for j in range(y, y+n):
            if matrix[x][y] != matrix[i][j]:
                return False
    return True


def solve(x, y, n):
    if same(x, y, n):
        cnt[matrix[x][y]+1] += 1
        return
    m = n//3
    for i in range(0, 3):
        for j in range(0, 3):
            solve(x+i*m, y+j*m, m)


solve(0, 0, n)
for i in cnt:
    print(i)
