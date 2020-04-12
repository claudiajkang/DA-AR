from sys import stdin

read = lambda: int(stdin.readline().rstrip())

n = read()
pn = {}

for i in range(n):
    a = read()
    if a not in pn.keys():
        pn[a] = 0

    pn[a] += 1

mv = max(pn.values())

for i in sorted(pn.keys()):
    if pn[i] == mv:
        print(i)
        break
