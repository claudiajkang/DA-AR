from sys import stdin

read = lambda: stdin.readline().rstrip()

t = int(read())
k = [int(read()) for i in range(t)]
pn = [0] * 46

for i in range(1, 46):
    pn[i] = (i * (i + 1)) // 2

pn = pn[1:]

for kk in k:
    flag = False
    for i in pn:
        for j in pn:
            for w in pn:
                if (i + j + w) == kk:
                    flag = True
                    break
            if flag: break
        if flag: break

    print(1 if flag else 0)
