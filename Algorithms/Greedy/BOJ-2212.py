from sys import stdin

read = lambda: stdin.readline().rstrip()

n = int(read())
k = int(read())
l = list(map(int, read().split()))
l.sort()

d = []

for i in range(n - 1):
    d.append(l[i + 1] - l[i])
d.sort(reverse=True)

print(sum(d[k - 1:]))
