from sys import stdin
read = lambda: int(stdin.readline().rstrip())

H = [read() for _ in range(9)]
H.sort()

p = []

for i in range(9):
    for j in range(9):
        p.append([i, j])

allsum = sum(H)
for i, j in p:
    r = allsum - H[i] - H[j]
    if r == 100:
        for ii in range(9):
            if ii not in [i, j]:
                print(H[ii])

        break
