from functools import partial
print = partial(print, flush=True)
T = int(input())
for i in range(1, T+1):
    N = int(input())
    A = [int(s) for s in input().split()]
    Hindex = [0] * N
    study = [0] * 100001
    ps = "Case #{}:".format(int(i))
    tmph = 2
    f = 0
    ft = 0
    amax = 0
    for i in range(0, len(A)):
        Ai = A[i]
        study[Ai] = study[Ai] + 1
        amax = [amax, Ai][amax <= study[Ai]]
        if i == 0 and A[i] >= 0:
            Hindex[i] = 1
        else:
            for o in range(tmph, amax+1):
                f = f + study[o]
                if f >= tmph:
                    ft = 1
                    break
            if ft > 0:
                Hindex[i] = tmph
                tmph = (Hindex[i - 1] + 1)
                f, ft = 0, 0
            else:
                Hindex[i] = Hindex[i - 1]
        ps = ps + " " + str(Hindex[i])

    print(ps)

def max(a,b):
    if a>=b: return a
    return b