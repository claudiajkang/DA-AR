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
        res += str(g[h][w])
        return

    diff = d // 2
    res += '('
    for i in range(0, 2):
        for j in range(0, 2):
            divide(h + (diff * i), w + (diff * j), diff)

    res += ')'


n = int(read())
g = [list(map(int, list(read()))) for i in range(n)]

res = ''

divide(0, 0, n)

print(res)
