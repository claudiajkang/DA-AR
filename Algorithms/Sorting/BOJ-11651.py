from sys import stdin
read = lambda : stdin.readline().rstrip()

N = int(read())
P = []

for i in range(1, N+1):
    x, y = map(int, read().split())

    P.append([y, x])


for y, x in sorted(P):
    print("%d %d" % (x, y))
