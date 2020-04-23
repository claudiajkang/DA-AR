from sys import stdin

t = stdin.readline().rstrip()
p = stdin.readline().rstrip()

tlen = len(t)
plen = len(p)

fail = [0] * plen

j = 0
for i in range(1, plen):
    while j > 0 and p[j] != p[i]:
        j = fail[j - 1]

    if p[j] == p[i]:
        j += 1
        fail[i] = j

j = 0
res = []
for i in range(tlen):
    while j > 0 and p[j] != t[i]:
        j = fail[j - 1]

    if p[j] == t[i]:
        if j == (plen - 1):
            res.append(i - plen + 2)
            j = fail[j]
        else:
            j += 1

print(len(res))
print('\n'.join(map(str, res)))
