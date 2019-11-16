import math

T = int(input())
for t in range(T):
    [N, M, Q] = [int(s) for s in input().split()]
    P = [int(s) for s in input().split()]
    R = [int(s) for s in input().split()]
    total = 0
    for r in R:
        total += math.floor(N / r)
        for p in P:
            if p % r == 0:
                total -= 1

    print("Case #{}: {}".format(t + 1, total))