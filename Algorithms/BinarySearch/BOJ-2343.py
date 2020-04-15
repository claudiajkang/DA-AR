from sys import stdin

read = lambda: map(int, stdin.readline().rstrip().split())

n, m = read()
time = list(read())

lo = 0
hi = sum(time)
maxTime = max(time)

while (lo + 1) < hi:
    mid = (lo + hi) // 2

    flag = False

    if maxTime <= mid:
        flag = True
        s = 0
        limit = m

        for i in range(n):
            s += time[i]
            if mid < s:
                if limit == 1:
                    flag = False
                    break

                limit -= 1
                s = time[i]

    if flag:
        hi = mid
    else:
        lo = mid

print(hi)