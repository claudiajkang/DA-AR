from sys import stdin

read = lambda: stdin.readline().rstrip()

t = read()
p = read()

tlen = len(t)
plen = len(p)

fail = [0] * plen

j = 0
for i in range(1, plen):
    if j > 0 and p[i] != p[j]:
        j = fail[j - 1]

    if p[i] == p[j]:
        j += 1
        fail[i] = j

j = 0
res = []
for i in range(tlen):
    if j > 0 and p[j] != t[i]:
        j = fail[j - 1]

    if p[j] == t[i]:
        if j == (plen - 1):
            res.append(i - plen + 2)
            j = fail[j]

        else:
            j += 1

print(len(res))

for i in res:
    print(i)
