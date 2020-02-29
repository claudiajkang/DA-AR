from sys import stdin
  
MN = 1000000
PN = [True] * (MN+1)
PN[0], PN[1] = False, False

for i in range(2, MN+1):
    if i * i > MN:
        break
    else:
        for j in range(2, MN // i + 1):
            PN[i * j] = False
        if i % 2 == 0: PN[i] = False


for l in stdin:
    l = int(l)
    if l == 0:
        break

    for i in range(l, 2, -1):
        if PN[i] and PN[l-i]:
            print("%d = %d + %d" % (l, l-i, i))
            break
