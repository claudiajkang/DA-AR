from sys import stdin
read = lambda: stdin.readline().rstrip()

n, m = map(int, read().split())
a = list(map(int, read().split()))
p = [0] * (n+1)

p[1] = a[0]
for i in range(1, n):
    p[i+1] = p[i] + a[i]

print(p)
for i in range(m):
    s, e = map(int, read().split())
    print(p[e]-p[s-1])
