from sys import stdin
from itertools import permutations
read = lambda: stdin.readline().rstrip()

h = [int(read()) for i in range(9)]

res = []

l = permutations(h, 7)

for i in list(l):
    if sum(i) == 100:
        res = i
        break

print('\n'.join(map(str, sorted(res))))