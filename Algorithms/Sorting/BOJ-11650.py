from sys import stdin
read = lambda : stdin.readline().rstrip()
N = int(read())
P = []

for i in range(1, N+1):
    x, y = list(map(int, read().split()))
    P.append([x, y])

for ii, jj in sorted(P):
    print("%d %d" % (ii, jj))