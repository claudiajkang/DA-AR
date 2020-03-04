from sys import stdin
read = lambda : stdin.readline().rstrip()

N = int(read())
PP = {}

for i in range(1, N+1):
    N, NAME = read().split()
    N = int(N)

    if N not in PP:
        PP[N] = []

    PP[N].append(NAME)

for i in sorted(PP.keys()):
    for j in PP[i]:
        print("%d %s" % (i, j))

    
