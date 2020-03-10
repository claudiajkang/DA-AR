import sys
sys.setrecursionlimit(10**6)
read = lambda : sys.stdin.readline().strip()

res = [0]*3
n = int(read())
p = [list(map(int, read().split())) for _ in range(n)]


def same(x, y, diff):
    for i in range(x, x+diff):
        for j in range(y, y+diff):
            if p[x][y] != p[i][j]:
                return False
    return True

def solve(x, y, diff):
    if same(x, y, diff):
        res[p[x][y]+1] += 1
        return
    d = diff//3
    for i in range(0, 3):
        for j in range(0, 3):
            solve(x+i*d, y+j*d, d)


solve(0, 0, n)
print('\n'.join(map(str, res)))
