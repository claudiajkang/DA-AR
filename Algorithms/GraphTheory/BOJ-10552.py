from sys import stdin

n, m, p = map(int, stdin.readline().rstrip().split())
channel = [0] * (m + 1)

for i in range(n):
    l, d = map(int, stdin.readline().rstrip().split())
    if channel[d] == 0:
        channel[d] = l

watched = [False] * (m + 1)
cur = p
res = 0

while (not watched[cur]) and (channel[cur] != 0):
    watched[cur] = True
    res += 1
    cur = channel[cur]

print(-1 if watched[cur] else res)
