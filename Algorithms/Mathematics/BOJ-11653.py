import sys

N = int(sys.stdin.readline())
q = N
res = []
idx = 2

while q != 1:
    if q % idx == 0:
        res.append(str(idx))
        q = int(q/idx)
    else:
        idx += 1

print('\n'.join(res))
