from functools import partial
print = partial(print, flush=True)
T = int(input())
for i in range(1, T+1):
    A = [int(s) for s in input().split()]
    value = []
    c = 0
    res = "YES"
    for t in range(0, len(A)):
        if A[t] == 0:
            c = c+1
        else:
            for j in range(0, c):
                value.append(i)
            c = 0

    print('Case #%d: %s' % (i, res))
