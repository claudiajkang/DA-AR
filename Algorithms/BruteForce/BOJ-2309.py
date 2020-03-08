from sys import stdin
read = lambda: int(stdin.readline())

h = [read() for _ in range(9)]
h.sort()

allsum = sum(h)
f = 0
for i in range(9):
    for j in range(9):
        if i == j:
            continue
        s = allsum - h[i] - h[j]
        if s == 100:
            f = 1
            for k in range(9):
                if k not in [i, j]:
                    print(h[k])

            break

    if f:
        break
