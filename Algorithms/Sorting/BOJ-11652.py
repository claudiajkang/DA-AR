from sys import stdin
read = lambda : int(stdin.readline())

N = read()
PN = {}

for i in range(N):
    v = read()
    if v not in PN.keys():
        PN[v] = 0
    PN[v] += 1

mv = max(PN.values())

for i in sorted(PN.keys()):
    if PN[i] == mv:
        print(i)
        break
