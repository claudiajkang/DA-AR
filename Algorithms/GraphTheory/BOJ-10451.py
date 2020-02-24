import sys

T = int(sys.stdin.readline())

for l in range(T):
    N = int(sys.stdin.readline())
    PI = list(map(int, sys.stdin.readline().strip().split()))

    P = [[] for i in range(N + 1)]

    for i in range(1, N + 1):
        tv = PI[i - 1]
        P[i].append(tv)
        if tv == i:
            continue
        P[tv].append(i)

    visited = [False for i in range(N + 1)]
    res = 0

    for i in range(1, N + 1):
        if not visited[i]:
            dstack = [i]
            visited[i] = True

            while dstack:
                cur = dstack.pop()

                if len(P[cur]) == 1 and P[cur][0] == cur:
                    res += 1
                    break

                for j in P[cur]:
                    if not visited[j]:
                        visited[j] = True
                        dstack.append(j)
                    elif j in dstack:
                        res += 1

    print(res)