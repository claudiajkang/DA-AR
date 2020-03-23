from sys import stdin
read = lambda: stdin.readline().rstrip()

n, m = map(int, read().split())
q = [i for i in range(1, n+1)]
res = 0

for find in map(int, read().split()):
    idx = q.index(find)
    res += min(len(q[idx:]), len(q[:idx]))
    q = q[idx+1:] + q[:idx]

print(res)