from sys import stdin
read = lambda : stdin.readline().rstrip()

T = int(read())
PN = [0 for _ in range(11+1)]

for i in range(12):
    if 1 <= i <= 3:
        PN[i] = [1, 2, 4][i-1]

    else:
        PN[i] = PN[i-1] + PN[i-2] + PN[i-3]

for i in range(T):
    c = int(read())
    print(PN[c])

