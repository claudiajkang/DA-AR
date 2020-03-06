from sys import stdin
read = lambda: stdin.readline().rstrip()

def rc(dis):
    global h, n
    count = 1
    cur = h[0]

    for i in range(1, n):
        if cur + dis <= h[i]:
            count += 1
            cur = h[i]

    return count

n, c = map(int, read().split())
h = [int(read()) for _ in range(n)]
h.sort()

start = 0
end = h[-1]
res = 0

while start <= end:
    distance = (start + end) // 2
    r = rc(distance)

    if r >= c:
        res = distance
        start = distance + 1

    else:
        end = distance - 1

print(res)

