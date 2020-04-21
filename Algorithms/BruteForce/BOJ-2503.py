from sys import stdin, setrecursionlimit
setrecursionlimit(10**6)
read = lambda: stdin.readline().rstrip()


def solve(num):
    global t, sb, n, res

    flag = [False] * n

    for i in range(n):
        cmp_num = tn[i]
        temp = [0, 0]
        for j in range(3):
            if cmp_num[j] == num[j]:
                temp[0] += 1
                continue

            if cmp_num[j] in num:
                temp[1] += 1

        if temp == sb[i]:
            flag[i] = True

    res += 0 if flag.count(False) else 1


n = int(read())
tn = [[] for i in range(n)]
sb = [[] for k in range(n)]

for i in range(n):
    a, b, c = map(int, read().split())
    tn[i] = list(str(a))
    sb[i] = [b, c]

res = 0

for ii in range(101, 1001):
    t = str(ii)
    if '0' not in t and len(set(t)) == 3:
        solve(list(t))

print(res)