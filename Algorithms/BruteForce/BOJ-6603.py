from itertools import combinations
from sys import stdin

read = lambda: stdin.readline().rstrip()

init = False

while True:
    s = list(map(int, read().split()))
    if len(s) == 1 and s[0] == 0:
        break

    if init:
        print()

    s = s[1:]
    s.sort()
    l = list(set(combinations(s, 6)))
    l.sort()

    for i in l:
        print(' '.join(map(str, i)))

    init = True
