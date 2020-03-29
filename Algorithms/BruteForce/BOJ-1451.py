from sys import stdin

read = lambda: stdin.readline().rstrip()


def psum(x1, y1, x2, y2):
    global s
    return s[x2][y2] - s[x2][y1 - 1] - s[x1 - 1][y2] + s[x1 - 1][y1 - 1]


n, m = map(int, read().split())

arr = [[0] * (m + 1) for i in range(n + 1)]
s = [[0] * (m + 1) for i in range(n + 1)]

for i in range(1, n + 1):
    arr[i] = [0] + list(map(int, list(read())))

for i in range(1, n + 1):
    for j in range(1, m + 1):
        s[i][j] = s[i - 1][j] + s[i][j - 1] - s[i - 1][j - 1] + arr[i][j]

res = 0

for i in range(1, m - 1):
    for j in range(i + 1, m):
        r1 = psum(1, 1, n, i)
        r2 = psum(1, i + 1, n, j)
        r3 = psum(1, j + 1, n, m)
        if res < (r1 * r2 * r3):
            res = r1 * r2 * r3

for i in range(1, n - 1):
    for j in range(i + 1, n):
        r1 = psum(1, 1, i, m)
        r2 = psum(i + 1, 1, j, m)
        r3 = psum(j + 1, 1, n, m)
        if res < (r1 * r2 * r3):
            res = r1 * r2 * r3

for i in range(1, n):
    for j in range(1, m):
        r1 = psum(1, 1, n, j)
        r2 = psum(1, j + 1, i, m)
        r3 = psum(i + 1, j + 1, n, m)
        if res < (r1 * r2 * r3):
            res = r1 * r2 * r3

for i in range(1, n):
    for j in range(1, m):
        r1 = psum(1, 1, i, j)
        r2 = psum(i + 1, 1, n, j)
        r3 = psum(1, j + 1, n, m)
        if res < (r1 * r2 * r3):
            res = r1 * r2 * r3

for i in range(1, n):
    for j in range(1, m):
        r1 = psum(1, 1, i, m)
        r2 = psum(i + 1, 1, n, j)
        r3 = psum(i + 1, j + 1, n, m)
        if res < (r1 * r2 * r3):
            res = r1 * r2 * r3

for i in range(1, n):
    for j in range(1, m):
        r1 = psum(1, 1, i, j)
        r2 = psum(1, j + 1, i, m)
        r3 = psum(i + 1, 1, n, m)
        if res < (r1 * r2 * r3):
            res = r1 * r2 * r3

print(res)