T = int(input())
for i in range(T):
    [N, M, Q] = [int(s) for s in input().split()]
    P = [int(s) for s in input().split()]
    R = [int(s) for s in input().split()]
    ans = 0
    for r in R:
        ans += int(N/r)
        for p in P:
            if p % r == 0:
                ans -= 1

    print("Case #{}: {}".format(i+1, ans))