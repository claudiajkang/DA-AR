from sys import stdin

A, P = map(int, stdin.readline().split())
D = [str(A)]
idx = 1
while True:
    v = 0
    for i in D[idx-1]:
        v += pow(int(i), P)

    if str(v) in D:
        idx = D.index(str(v))
        break

    D.append(str(v))
    idx += 1

print(len(D[:idx]))
