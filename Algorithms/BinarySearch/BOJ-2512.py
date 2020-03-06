from sys import stdin

read = lambda: stdin.readline().rstrip()

N = int(read())
LM = list(map(int, read().split()))
M = int(read())

if sum(LM) <= M:
    print(max(LM))

else:
    l = 0
    r = 1000000000
    mid = 0
    s = 0

    while l <= r:
        mid = (l + r) // 2
        s = 0
        for i in LM:
            if i <= mid:
                s += i
            else:
                s += mid

        if s <= M:
            l = mid + 1
        else:
            r = mid - 1

    if s > M:
        print(mid - 1)

    else:
        print(mid)

