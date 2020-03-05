from sys import stdin
read = lambda : int(stdin.readline())

N = read()
pn = {}

for i in range(N):
    v = read()
    if v not in pn:
        pn[v] = 0

    pn[v] += 1

mv = max(pn.values())

for i in sorted(pn.keys()):
    if pn[i] == mv:
        print(i)
        break