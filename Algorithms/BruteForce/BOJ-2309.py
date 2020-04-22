from itertools import permutations
from sys import stdin

read = lambda: stdin.readline().rstrip()

h = [int(read()) for i in range(9)]
h.sort()

tlist = list(permutations(h, 7))

for tt in tlist:
    s = 0
    for j in range(7):
        s += tt[j]

    if s == 100:
        print('\n'.join(map(str, tt)))
        break
