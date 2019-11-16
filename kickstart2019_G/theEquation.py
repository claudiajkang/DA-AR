from functools import partial
print = partial(print, flush=True)
T = int(input())
for i in range(1, T + 1):
    [N, M] = [int(s) for s in input().split()]
    A = [list(bin(int(s)).replace("0b", "")) for s in input().split()]
    size = 55
    One, Zero = [0] * size, [0] * size
    mlen = len(bin(M).replace("0b", ""))
    Amax = 0
    for a in A:
        a.reverse()
        a = [int(n) for n in a]
        alen = len(a)
        Amax = max(Amax, alen)
        for j in range(0, alen):
            One[j] = One[j] + a[j]
            Zero[j] = Zero[j] + int(not a[j])
        if alen < mlen:
            for j in range(alen, mlen):
               Zero[j] = Zero[j] + 1
    v = 0
    tm = M
    K = 0
    for k in range(Amax-1, -1, -1):
        l = 1 << k
        maxval, minval, mi = 0, 0, 0

        if Zero[i] >= One[i]:
            maxval, minval = Zero[i], One[i]
            mi = 1
        else:
            maxval, minval = One[i], Zero[i]

        maxval = maxval * l

        if maxval <= tm:
            tm = tm - maxval
            K = K + (mi * l)
            continue

        minval = minval * l

        if minval <= tm:
            tm = tm - minval
            K = K + (int(not mi) * l)
            continue
    print('Case #%d: %d' % (i, K))



def max(a, b):
    if a > b: return a
    return b

def min(a, b):
    if a < b: return a
    return b

