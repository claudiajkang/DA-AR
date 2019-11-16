T = int(input())

for i in range(T):
    N, M, Q = map(int, input().split())
    BOOK = [1] * (N+1)

    P = list(map(int, input().split()))
    R = list(map(int, input().split()))

    sum = 0

    for i in range(M):
        v = P[i]
        BOOK[v] = 0

    if N > len(P):
        for j in range(Q):
            sum = sum + int(N/R[j])

            for k in P:
                if k % R[j] == 0:
                    sum = sum - 1

    ps = "Case #{}: {}".format(i+1,sum)
    print(ps)