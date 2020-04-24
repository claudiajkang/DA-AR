from sys import stdin, setrecursionlimit

setrecursionlimit(10 ** 6)
read = lambda: stdin.readline().rstrip()


def same(h, w, d):
    global g

    for i in range(h, h + d):
        for j in range(w, w + d):
            if g[i][j] != g[h][w]:
                return False

    return True


def divide(h, w, d):
    global g, res

    if same(h, w, d):
        res[g[h][w]] += 1
        return

    diff = d // 3
    for i in range(0, 3):
        for j in range(0, 3):
            divide(h + (diff * i), w + (diff * j), diff)


n = int(read())
g = [list(map(int, read().split())) for i in range(n)]
res = {-1: 0, 0: 0, 1: 0}

divide(0, 0, n)

for i in [-1, 0, 1]:
    print(res[i])
