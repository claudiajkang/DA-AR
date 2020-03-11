from sys import stdin

read = lambda: stdin.readline().rstrip()


def count(d):
    global h, n

    cur = h[0]
    c = 1
    for i in range(1, n):
        if cur + d <= h[i]:
            cur = h[i]
            c += 1

    return c


n, c = map(int, read().split())
h = [int(read()) for _ in range(n)]
h.sort()

start = 0
end = h[-1]
res = 0

while start <= end:
    dis = (start + end) // 2
    r = count(dis)

    if r >= c:
        res = dis
        start = dis + 1
    else:
        end = dis - 1

print(res)
