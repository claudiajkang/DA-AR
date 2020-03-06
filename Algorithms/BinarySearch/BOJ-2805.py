from sys import stdin
read = lambda : stdin.readline().rstrip()

N, M = map(int, read().split())
t = sorted(list(map(int, read().split())), reverse=True)
l, r = 1, max(t)

while l <= r:
    mid = (l+r) // 2

    s = 0
    for i in t:
        if i >= mid:
            s += i - mid

    if s >= M:
        l = mid + 1
    else:
        r = mid - 1
print(r)

