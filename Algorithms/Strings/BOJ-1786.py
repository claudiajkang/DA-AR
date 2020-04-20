from collections import deque
from sys import stdin

read = lambda: stdin.readline().rstrip()

s = read()
p = read()
slen = len(s)
plen = len(p)

fail = [0] * len(p)

j = 0
for i in range(1, plen):
    while (j > 0) and p[i] != p[j]:
        j = fail[j - 1]

    if p[i] == p[j]:
        j += 1
        fail[i] = j

j = 0
res = deque()
for i in range(slen):
    while j > 0 and s[i] != p[j]:
        j = fail[j - 1]

    if s[i] == p[j]:
        if j == plen - 1:
            res.append(i - plen + 2)
            j = fail[j]
        else:
            j += 1

print(len(res))
for i in res:
    print(i)
