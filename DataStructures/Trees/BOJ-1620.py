from sys import stdin
read = lambda: stdin.readline().rstrip()

n, m = map(int, read().split())
p = {}

for i in range(1, n+1):
    v = read()
    p[str(i)] = v
    p[v] = i

for j in range(m):
    v = read()
    print(p[v])
