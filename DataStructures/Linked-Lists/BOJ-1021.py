from sys import stdin
read = lambda: stdin.readline().rstrip()

n, m = map(int, read().split())
q = [i for i in range(1, n+1)]
position = list(map(int, read().split()))
res = 0

for p in position:
    idx = q.index(p)
    res += min(len(q[idx:]), len(q[:idx]))
    q = q[idx+1:] + q[:idx]

print(res)
