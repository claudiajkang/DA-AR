from sys import stdin
read = lambda: stdin.readline().rstrip()

n = int(read())
p = [[] for i in range(n)]

for i in range(n):
    p[i] = list(map(int, read().split()))

p.sort(key=lambda x: x[0])
p.sort(key=lambda x: x[1])

for i, j in p:
    print(f"{i} {j}")