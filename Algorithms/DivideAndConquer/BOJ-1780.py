from sys import stdin
read = lambda: stdin.readline().rstrip()

def same(x, y, d):
    global p
    for i in range(x, x+d):
        for j in range(y, y+d):
            if p[x][y] != p[i][j]:
                return False

    return True

def divide(x, y, d):
    global p, res

    if same(x, y, d):
        res[p[x][y]+1] += 1
        return

    diff = d // 3
    for i in range(0, 3):
        for j in range(0, 3):
            divide(x + diff*i, y + diff*j, diff)

n = int(read())
p = [list(map(int, read().split())) for _ in range(n)]
res = [0, 0, 0]

divide(0, 0, n)

for i in res:
    print(i)
