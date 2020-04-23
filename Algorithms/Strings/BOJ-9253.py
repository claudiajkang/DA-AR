from sys import stdin

a = stdin.readline().rstrip()
b = stdin.readline().rstrip()
p = stdin.readline().rstrip()

plen = len(p)

fail = [0] * plen

j = 0
for i in range(1, plen):
    if j > 0 and p[i] != p[j]:
        j = fail[j - 1]

    if p[i] == p[j]:
        j += 1
        fail[i] = j

ares = False
bres = False

j = 0
for i in range(len(a)):
    if j > 0 and p[j] != a[i]:
        j = fail[j - 1]

    if p[j] == a[i]:
        if j == (plen - 1):
            ares = True
            break
        else:
            j += 1

j = 0
for i in range(len(b)):
    if j > 0 and p[j] != b[i]:
        j = fail[j - 1]

    if p[j] == b[i]:
        if j == (plen - 1):
            bres = True
            break
        else:
            j += 1

print("YES" if ares and bres else "NO")
