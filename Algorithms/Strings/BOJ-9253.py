from sys import stdin
read = lambda: stdin.readline().rstrip()

a = read()
b = read()
p = read()

alen = len(a)
blen = len(b)
plen = len(p)

fail = [0] * plen

j = 0
for i in range(1, plen):
    while j > 0 and p[i] != p[j]:
        j = fail[j-1]

    if p[i] == p[j]:
        j += 1
        fail[i] = j

j = 0
suc = [False, False]

for i in range(alen):
    while j > 0 and a[i] != p[j]:
        j = fail[j-1]

    if a[i] == p[j]:
        if j == (plen - 1):
            suc[0] = True
            j = fail[j]

        else:
            j += 1

for i in range(blen):
    while j > 0 and b[i] != p[j]:
        j = fail[j-1]

    if b[i] == p[j]:
        if j == (plen - 1):
            suc[1] = True
            j = fail[j]

        else:
            j += 1

if suc[0] and suc[1] : print("YES")
else: print("NO")