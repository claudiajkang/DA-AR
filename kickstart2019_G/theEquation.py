T = int(input())
for i in range(T):
    [N, M] = [int(s) for s in input().split()]
    A = [int(s) for s in input().split()]
    K = -1
    tk = 0
    if M == 0:
        for k in A:
            for a in A:
                tk += (a ^ a)
            if tk == 0:
                K = k
            tk = 0
    else:
        for k in range(0, M):
            for a in A:
                tk += (a ^ k)
            if K <= k and tk <= M:
                K = k
            tk = 0
    print("Case #{}: {}".format(i+1, K))

