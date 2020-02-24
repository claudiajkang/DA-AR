import sys

A, P = sys.stdin.readline().strip().split()
DP = [A]
P = int(P)
idx = 1
tidx = 0

while True:
    tv = 0
    for i in DP[idx-1]:
        tv += pow(int(i), P)
    try:
        tidx = DP.index(str(tv))
    except ValueError:
        DP.append(str(tv))
        idx += 1
    else:
        print(tidx)
        break
