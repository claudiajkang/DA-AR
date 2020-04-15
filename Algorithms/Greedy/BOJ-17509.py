from sys import stdin

read = lambda: list(map(int, stdin.readline().rstrip().split()))

g = [[] for i in range(11)]

for i in range(11):
    g[i] = read()

g.sort(key=lambda x: x[1])
g.sort(key=lambda x: x[0])

s = 0
time = 0

for i in range(11):
    time += g[i][0]
    s += (time + 20 * g[i][1])

print(s)
